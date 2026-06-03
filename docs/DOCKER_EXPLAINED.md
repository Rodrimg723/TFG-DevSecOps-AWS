# Explicación del Despliegue de Servicios con Docker Compose

Este documento detalla la arquitectura de microservicios definida en `docker/docker-compose.yml`, explicando cada componente y su función en la seguridad y monitoreo.

## Estructura de Archivos

*   **`docker-compose.yml`**: Orquestación de contenedores principal.
*   **`observability/`**: Configuraciones de Prometheus y Grafana.
*   **`security/`**: Reglas de CrowdSec y configuración del bouncer.

## Análisis de `docker-compose.yml`

### 1. Traefik (Proxy Inverso & Gateway)
```yaml
  traefik:
    image: traefik:latest
    command: ...
    ports: "80:80", "443:443", "8080:8080"
```
*   **Rol:** Puerta de entrada única a tu infraestructura. Recibe todas las peticiones de internet y las distribuye a los contenedores correspondientes (routing).
*   **Características clave habilitadas:**
    *   **Dashboard (`--api.insecure=true`)**: Panel visual en el puerto 8080 para ver rutas y servicios (en producción debería protegerse).
    *   **Métricas (`--metrics.prometheus=true`)**: Expone datos de rendimiento para que Prometheus los recoja.
    *   **Logs de Acceso**: Escribe qué IPs visitan qué páginas en un archivo compartido con CrowdSec.

### 2. CrowdSec (Seguridad - IDS/IPS)
Este es el "cerebro" de la seguridad.
```yaml
  crowdsec:
    image: crowdsecurity/crowdsec
    environment:
      - COLLECTIONS=crowdsecurity/traefik ...
    volumes:
      - ...:/var/log/traefik:ro
```
*   **Rol:** Sistema de Detección de Intrusiones (IDS).
*   **Funcionamiento:** Lee los logs que genera Traefik (`/var/log/traefik`). Si detecta un patrón de ataque (ej: escaneo de vulnerabilidades, fuerza bruta), "decide" bloquear esa IP.
*   **Collections:** Le hemos dicho que use colecciones específicas para entender logs HTTP y de Traefik.

### 3. Traefik Bouncer (El "Gorila" de la Discoteca)
```yaml
  bouncer-traefik:
    image: fbonalair/traefik-crowdsec-bouncer
```
*   **Rol:** Sistema de Prevención (IPS).
*   **Funcionamiento:** Traefik le pregunta a este bouncer "¿Puedo dejar pasar a esta IP?" antes de cada petición. El bouncer consulta a CrowdSec. Si CrowdSec ha baneado la IP, el bouncer le dice a Traefik que devuelva un "403 Forbidden".

### 4. Stack de Observabilidad
Para ver qué está pasando.

#### Prometheus
*   **Rol:** Base de datos de métricas. Se conecta a Traefik cada X segundos y le pregunta "¿Cuántas peticiones has recibido? ¿Cuántos errores 500?". Guarda esos números.

#### Grafana
*   **Rol:** Visualización. Lee los datos de Prometheus y los pinta en gráficos bonitos que puedes entender (Dashboards en puerto `3000`).

### 5. Servicios de Prueba (Targets)

#### DVWA (Damn Vulnerable Web App)
```yaml
  dvwa:
    image: vulnerables/web-dvwa
    labels:
      - "traefik.http.routers.dvwa.rule=PathPrefix(`/dvwa`)"
      - "traefik.http.routers.dvwa.middlewares=crowdsec..."
```
*   **Rol:** Aplicación web llena de fallos de seguridad a propósito.
*   **Uso:** La usamos para atacar nuestra propia infraestructura y comprobar si CrowdSec nos detecta y bloquea.
*   **Labels:** Las etiquetas `traefik...` son "mágicas". Le dicen a Traefik: "Si alguien pide `/dvwa`, mándalo aquí, PERO pasa primero por el middleware `crowdsec`".

#### Whoami
*   **Rol:** Servicio muy ligero que solo devuelve tu IP y datos del contenedor.
*   **Uso:** Para comprobar que el enrutamiento básico funciona sin gastar recursos.

## Redes y Volúmenes
*   **Red `web`:** Todos los contenedores están en una red interna aislada. Solo Traefik expone puertos al mundo real.
*   **Volúmenes:** Persistencia de datos (ej: base de datos de CrowdSec) para que no se pierdan al reiniciar contenedores.
