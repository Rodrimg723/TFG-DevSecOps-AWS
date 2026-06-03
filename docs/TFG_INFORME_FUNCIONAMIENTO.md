# 🏢 Informe Detallado de Funcionamiento: Infraestructura Cloud DevSecOps

## 1. Visión General del Proyecto
El proyecto implementa una arquitectura basada en el paradigma **DevSecOps** (Development, Security, and Operations). Su objetivo principal es automatizar por completo el despliegue de una infraestructura en la nube (AWS), configurar el servidor de forma idéntica en cada ejecución y levantar una serie de microservicios contenerizados que incluyen seguridad perimetral activa y monitorización en tiempo real.

En lugar de tratar al servidor como una "mascota" (configurado a mano y difícil de replicar), se trata como "ganado", utilizando **Infraestructura como Código (IaC)** para que pueda ser destruido y recreado en minutos sin intervención manual.

El flujo de despliegue se divide en tres fases principales:
1. **Provisionamiento** (Terraform)
2. **Configuración y Hardening** (Ansible)
3. **Orquestación de Servicios** (Docker Compose)

---

## 2. Fase 1: Provisionamiento de Hardware (Terraform)
La infraestructura comienza a nivel "físico" (virtualizado) en los centros de datos de Amazon Web Services (AWS), concretamente en la región `us-east-1` (Norte de Virginia). Todo esto se define a través del archivo `main.tf`.

*   **Instancia EC2 (El núcleo):** Terraform solicita a AWS la creación de una máquina virtual (EC2) de tipo `t2.small` (1 vCPU, 2GB RAM). Esta máquina arranca siempre con la última imagen oficial (**AMI**) de Ubuntu Server 22.04 LTS, garantizando un entorno base actualizado y limpio.
*   **Security Group (Firewall Perimetral Cloud):** Se configura un firewall a nivel de red de AWS que actúa como la primera barrera de defensa. Siguiendo el principio de mínimo privilegio, **todo el tráfico de entrada está bloqueado por defecto**, exceptuando:
    *   **Puerto 22 (SSH):** Para la gestión de Ansible y el administrador.
    *   **Puertos 80 (HTTP) y 443 (HTTPS):** Para el servicio web público (Traefik).
    *   **Puertos 8080 y 3000:** Excepciones para los paneles de panel de control de Traefik y Grafana.
*   **Claves SSH:** Para evitar contraseñas débiles, la máquina es inyectada en el arranque con la clave pública `vockey` (típica de entornos AWS Academy), permitiendo el acceso administrativo seguro sin contraseña.

Al finalizar esta fase, Terraform devuelve la IP Pública de la nueva máquina.

---

## 3. Fase 2: Configuración y Hardening (Ansible)
Una vez la máquina física está encendida y accesible, toma el relevo **Ansible**, que se conecta automáticamente a través de la IP generada por Terraform vía SSH. Ansible ejecuta su `playbook.yml` de forma secuencial e idempotente (siempre deja el servidor en el mismo estado final):

*   **Actualizaciones Base:** Actualiza los respositorios (`apt update/upgrade`) e instala herramientas vitales como Git o htop.
*   **Hardening del Sistema (Seguridad a nivel OS):**
    *   **UFW (Uncomplicated Firewall):** Ansible levanta un segundo firewall dentro del propio Ubuntu como defensa en profundidad. Restringe todas las conexiones excepto las estrictamente necesarias identificadas en el Security Group de AWS.
    *   **Blindaje SSH:** Edita `/etc/ssh/sshd_config` para rechazar explícitamente el uso de contraseñas (`PasswordAuthentication no`), mitigando instantáneamente los ataques automatizados de fuerza bruta vía SSH.
*   **Instalación del Motor:** Se configuran los repositorios oficiales y las claves GPG para instalar **Docker Engine** y **Docker Compose**.
*   **Transferencia y Despliegue:** Ansible crea el directorio `/opt/devsecops`, copia automáticamente todo el código fuente desde el repositorio al servidor, y, como último paso, ejecuta `docker compose up -d` para dar vida a los servicios.

---

## 4. Fase 3: Despliegue de Servicios (Docker Compose)
Toda la lógica de aplicación está contenerizada. El clúster local de Docker se encarga de separar roles en distintos contenedores, unidos por una red virtual interna (`web`), garantizando que los servicios no expongan puertos aleatorios al exterior. 

El stack se compone de cinco patas fundamentales:

### A. El Enrutador: Traefik (Reverse Proxy)
Traefik es la **única puerta de entrada** de internet al entorno Docker. Escucha en los puertos 80 y 443. 
*   **Enrutamiento Dinámico:** Cuando llega una petición, Traefik lee a qué dominio o subruta (ej. `/dvwa`) se dirige y redirige el tráfico al contenedor interno adecuado.
*   **Gestor SSL:** Se encarga de negociar y auto-renovar certificados SSL/TLS con Let's Encrypt para asegurar conexiones HTTPS cifradas.
*   **Observabilidad:** Genera logs de acceso exhaustivos y expone métricas en formato Prometheus sobre todo el tráfico entrante.

### B. El Centro de Seguridad: CrowdSec (IDS / IPS)
Esta es la capa de defensa activa y colaborativa.
*   **Análisis (IDS):** El contenedor de CrowdSec ("el cerebro") está continuamente leyendo los logs de acceso generados por Traefik. Busca patrones de ataques web, ataques DDoS y escaneos de vulnerabilidades.
*   **Bloqueo (IPS):** Funciona junto con **Traefik Bouncer**. Antes de que Traefik envíe una página web a un usuario, le pregunta al bouncer. Si CrowdSec ha visto a esa IP haciendo un escaneo (o si la IP está en la lista negra mundial colaborativa de la comunidad CrowdSec), el bouncer le ordena a Traefik cortar la conexión inmediatamente y devolver un crudo Error 403 (Forbidden).

### C. La Monitorización: Prometheus + Grafana
La infraestructura necesita ser visible y medible ("observabilidad").
*   **Prometheus:** Actúa como un recolector de métricas (Time-Series Database). Se conecta regularmente a Traefik y a la propia máquina para preguntar sobre usos de CPU, memoria, red y cantidad de peticiones/errores HTTP.
*   **Grafana:** Es la cara visual de los datos. Lee la información en bruto de Prometheus y dibuja paneles o *dashboards* estéticos en tiempo real accesibles en el puerto 3000, mostrando no solo el rendimiento del servidor sino un mapa de calor o recuentos de ataques bloqueados.

### D. Las Aplicaciones Objetivo (Targets de Prueba)
Para poder demostrar el funcionamiento de los sistemas anteriores, se levantan aplicaciones ligeras:
*   **Whoami:** Se utiliza para pruebas sanas de conectividad. Simplemente devuelve información sobre quién hace la petición.
*   **DVWA (Damn Vulnerable Web App):** Una aplicación deliberadamente plagada de vulnerabilidades de seguridad (*Inyección SQL, Cross-Site Scripting, etc*). En este TFG se usa para realizar pruebas de penetración (pentesting). Al atacar DVWA con herramientas como `Nikto` o intentos continuos de explotar algo, CrowdSec logra detectar el comportamiento anómalo en los logs de Traefik y banea al atacante, demostrando así la robustez del sistema de seguridad automatizado.

---

## 5. Resumen del Flujo de una Petición 
Para entender la sinergia, este es el viaje de una petición web de un atacante:
1. El atacante hace una petición HTTP escaneando vulnerabilidades a la IP pública de AWS.
2. El escaneo pasa el Security Group de AWS y el UFW local de Ubuntu al ir dirigido al puerto 443.
3. Lo recibe **Traefik**. Antes de enviarlo al servidor DVWA, Traefik le pasa la IP del atacante al **Bouncer de CrowdSec**.
4. Simultáneamente, **CrowdSec** está leyendo los logs recientes de Traefik. Detecta rápidamente que esta petición contiene firmas maliciosas.
5. CrowdSec añade la IP del atacante a su base de datos bloqueada.
6. En el siguiente intento, el **Bouncer** le manda a Traefik detener al atacante.
7. El atacante recibe un acceso denegado estricto (HTTP 403), protegiendo exitosamente a la aplicación alojada.
8. Todo este incidente queda registrado y dibujado visualmente en los paneles de **Grafana** (obtenidos vía **Prometheus**).
