# Guía Maestra de Verificación del Proyecto DevSecOps

Sigue esta lista paso a paso para asegurar que tu infraestructura funciona perfectamente. Si pasas todos los puntos, tu TFG está listo para demostración.

## 🚀 Cómo Conectarte al Servidor (Paso 0)

Para las comprobaciones internas (logs, htop, docker), necesitarás una terminal conectada al servidor AWS.

**Abre una terminal en VS Code (WSL) y ejecuta:**
```bash
ssh -i ~/.ssh/vockey.pem ubuntu@52.207.227.254
```
*(Si te pregunta "Are you sure you want to continue connecting?", escribe `yes`)*

---

## 1. Verificación de Infraestructura (Terraform)
Acciones a realizar desde tu **terminal local (WSL)**.

Primero, ve a la carpeta correcta:
```bash
cd /mnt/c/Users/rodri/.gemini/antigravity/scratch/terraform
```

- [ ] **Sintaxis Correcta**: Ejecuta `terraform validate`. Debe devolver "Success!".
- [ ] **Planificación Limpia**: Ejecuta `terraform plan`. No debe dar errores de autenticación o sintaxis.
- [ ] **Despliegue Exitoso**: Si ejecutas `terraform apply`, debe terminar mostrando `instance_public_ip = "54.163.198.56"`.
- [ ] **Comprobación AWS**: Entra en la consola de AWS -> EC2. Debes ver una instancia llamada "DevSecOps-Server" en estado "Running".
- [ ] **Comprobación Seguridad**: En la pestaña "Security" de la instancia, verifica que los puertos 22, 80, 443, 3000, 8080 están abiertos.

## 2. Verificación de Configuración (Ansible)
**¡IMPORTANTE!**: Estas acciones se realizán desde tu **TERMINAL LOCAL (WSL)**.
❌ **NO** debes estar conectado por SSH dentro del servidor (`ubuntu@ip...`). Si lo estás, escribe `exit` primero.

1.  Asegúrate de estar en la carpeta correcta en tu PC:
    ```bash
    cd /mnt/c/Users/rodri/.gemini/antigravity/scratch/ansible
    ```
2.  **Ejecución de Playbook**: Ejecuta:
    ```bash
    ansible-playbook -i inventory.ini playbook.yml
    ```
    - [ ] No debe haber tareas fallidas (failed=0).
    - [ ] Tareas clave como "Install Docker" y "Start Docker Compose" deben figurar como `changed` u `ok`.
3.  **Idempotencia**: Si vuelves a ejecutar el playbook, todo debe salir en verde (`ok`) y nada en amarillo (`changed`), excepto quizás comandos shell.

## 3. Verificación de Servicios (Docker & Traefik)
Acciones a realizar desde un navegador web visitando `http://<IP_PUBLICA>`.

- [ ] **Router Básico**: Visita `http://<IP_PUBLICA>/whoami`.
    - [ ] Debe cargar una página de texto plano con detalles del sistema.
    - [ ] **Éxito:** Significa que Traefik está enrutando bien.
- [ ] **Dashboard Traefik**: Visita `http://<IP_PUBLICA>:8080/dashboard/`.
    - [ ] Debe cargar el panel azul oscuro de Traefik.
    - [ ] Debe cargar el panel azul oscuro de Traefik.
    - [ ] En la pestaña HTTP Routers, debes ver algo parecido a esto:
        -   `dvwa@docker`
        -   `whoami@docker`
        -   `prometheus@internal` (Este es el que monitoriza Traefik).
- [ ] **Aplicación Vulnerable**: Visita `http://<IP_PUBLICA>/dvwa/login.php`.
    - [ ] **IMPORTANTE:** Si ves una pantalla que dice "Database Setup", baja hasta el final y pulsa el botón **"Create / Reset Database"**.
    - [ ] Después, te llevará al LOGIN de color rojo (User: `admin`, Pass: `password`).
    - [ ] Entra y navega un poco para confirmar que la aplicación responde.

## 4. Verificación de Seguridad (CrowdSec)
La prueba de fuego.

- [ ] **Simulación de Ataque**:
    1.  Desde tu navegador (o una terminal con `curl`), intenta acceder a una ruta prohibida repetidamente en DVWA o usa una herramienta de escaneo como `nikto` (si la tienes):
        ```bash
        # Ejemplo simple: intenta acceder a un archivo sensible muchas veces
        for i in {1..20}; do curl http://<IP_PUBLICA>/dvwa/.env; done
        ```
    2.  O usa un simulador de fuerza bruta en el login de DVWA.
- [ ] **Verificación de Bloqueo**:
    - [ ] Después de unos segundos, intenta entrar a `http://<IP_PUBLICA>/whoami`.
    - [ ] **Resultado Esperado:** Deberías recibir un error **"403 Forbidden"**.
    - [ ] Esto confirma que CrowdSec detectó el ataque y le dijo a Traefik que bloqueara tu IP para *todos* los servicios.
- [ ] **Verificación en Logs**:
    - [ ] Entra al servidor por SSH.
    - [ ] Ejecuta: `docker exec crowdsec cscli decisions list`.
    - [ ] Deberías ver tu IP pública en la lista de baneados.

## 5. Verificación de Observabilidad (Grafana)
Ahora vamos a ver los "ojos" de tu seguridad en `http://52.207.227.254:3000`.

### 5.1. Generar Tráfico (para que se vea algo)
Ejecuta esto en tu terminal local repetidamente o simplemente recarga la web varias veces:
```bash
# Simula tráfico normal
for i in {1..5}; do curl -I http://52.207.227.254/whoami; done

# Simula ataque (dará 403 Forbidden si CrowdSec funciona)
curl -I http://52.207.227.254/dvwa/vulnerabilities/sqli/?id=1%27
```

### 5.2. Entrar en Grafana
1.  **Login:** Usuario `admin`, Password `admin` (puedes saltar el cambio de contraseña).
2.  **Ir al Dashboard:** Ve a **Dashboards** (icono de 4 cuadrados) -> **General** -> **DeepSecOps Overview**.

### 5.3. Qué buscar en el Dashboard
Verás dos paneles clave que demuestran tu TFG funcionando:

*   **Traefik Requests (Gráfica de Líneas):**
    *   Muestra el tráfico en tiempo real.
    *   **Líneas Verdes (2xx):** Tráfico legítimo (tus recargas a `whoami`).
    *   **Líneas Rojas (4xx):** Errores o bloqueos (tus intentos de ataque a `dvwa`).
*   **CrowdSec Blocks (Contador):**
    *   Muestra el número total de ataques bloqueados.
    *   **Importante:** Si intentaste atacar DVWA y te dio error 403, **este número debe ser mayor que 0**.
    *   Es la prueba visual de que tu IPS está protegiendo el servidor activamente.

---

## Qué hacer si algo falla

*   **Si Terraform falla:** Revisa las credenciales de AWS (`aws configure`) y que no haya recursos duplicados.
*   **Si Ansible falla:** Revisa que la IP en `inventory.ini` sea la correcta y que la clave `.pem` tenga permisos `400` (solo lectura).
*   **Si el Bloqueo no funciona:** Asegúrate de que el contenedor `bouncer-traefik` tiene la API Key correcta conectada con `crowdsec` (esto se configura automáticamente en nuestro setup, pero verifícalo en los logs: `docker logs bouncer-traefik`).
