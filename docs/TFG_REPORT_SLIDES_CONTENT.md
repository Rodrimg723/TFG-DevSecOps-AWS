# Contenido Resumido para Diapositivas (Puntos 1 al 4)

## Diapositiva 1: Portada
**(Título de la presentación)**
*   **Proyecto:** Infraestructura Cloud Automatizada y Segura (DevSecOps)
*   **Autor:** Rodrigo [Apellidos]
*   **Estudios:** ASIR - [Nombre del Centro]
*   **Curso:** 2025/2026

---

## Diapositiva 2: Introducción
**Contexto del Proyecto**
*   **Nuevo paradigma:** Servidores "Mascotas" ➡️ "Ganado" (efímeros y reemplazables).
*   **Enfoque DevSecOps:** Integración de seguridad desde el inicio.
*   **Escenario:** Despliegue en nube pública (AWS) rápido, repetible y seguro.

---

## Diapositiva 3: El Problema Detectado
**¿Por qué es necesario este proyecto?**
1.  **Configuración manual (Drift):** Fallos inesperados entre entornos ("funciona en mi máquina").
2.  **Lentitud:** Días para provisionar un entorno nuevo.
3.  **Seguridad reactiva:** Servidores expuestos a internet vulnerables desde el primer minuto.
*   **Solución central:** Infraestructura como Código (IaC) con seguridad activa (WAF/IPS) por defecto.

---

## Diapositiva 4: Objetivos del Proyecto
**Meta General y Pilares**
*   **Objetivo principal:** Diseñar infraestructura de Alta Disponibilidad y Seguridad en AWS 100% mediante código.
*   **Pilares específicos:**
    1.  **IaC (Terraform):** Eliminar configuración manual.
    2.  **Automatización (Ansible):** Servidores idénticos siempre.
    3.  **Contenedores (Docker):** Aislamiento de servicios web.
    4.  **Seguridad IPS (CrowdSec):** Bloqueo en tiempo real.
    5.  **Monitorización (Grafana):** Visualización del estado.

---

## Diapositiva 5: Alcance del Proyecto
**Ciclo Completo DevSecOps**
*   **Planificación:** Diseño de red y seguridad.
*   **Código:** Manifiestos IaC (Terraform/Ansible).
*   **Despliegue:** AWS Academy.
*   **Validación:** Pruebas Pentesing controladas.

---

## Diapositiva 6: Análisis y Tecnologías
**¿Por qué estas herramientas?**
*   **AWS:** Estándar de la industria, gran ecosistema.
*   **Terraform:** Agnóstico del proveedor (multi-cloud).
*   **Ansible:** *Agentless* (sin agentes) y fácil sintaxis (YAML).
*   **Docker Compose:** Ideal y ágil para orquestar 5-10 contenedores.
*   **Traefik & CrowdSec:** Proxy reverso con SSL automático + Seguridad colaborativa activa.

---

## Diapositiva 7: Requisitos Técnicos
**Características de la Infraestructura**
*   **Hardware Virtual:** Instancia pequeña EC2 de AWS (Ubuntu 22.04).
*   **Red / Firewall:** Reglas estrictas en AWS (entrada solo puertos 22, 80 y 443).
*   **Seguridad y Criptografía:**
    *   SSH por claves públicas.
    *   Certificados SSL (HTTPS) vigentes.
    *   Baneo automático de IP por escaneos.

---

## Diapositiva 8: Planificación
**Cronograma (8 semanas)**
*   **Fase 1 (Semanas 1-2):** Investigación y diseño de Arquitectura.
*   **Fase 2 (Semanas 3-6):** Desarrollo de código (Terraform, Ansible, Docker).
*   **Fase 3 (Semanas 7-8):** Pruebas de fuego (Pentesting) y documentación final.

---

## Diapositiva 9: Diseño del Sistema - Arquitectura General
**Defensa en Profundidad & Mínimo Privilegio**
*   **AWS:** Security Group restrictivo (solo puertos 22, 80 y 443).
*   **Ubuntu:** Sistema base sin servicios extra.
*   **Docker:** Contenedores aislados. Traefik como única puerta de entrada.
> **[📷 SUGERENCIA DE IMAGEN]:** Captura de pantalla de la consola de AWS (Security Group) mostrando las reglas de entrada.

---

## Diapositiva 10: Diseño del Sistema - Diagrama Lógico y Flujo
**Anatomía de una Petición (Cómo actúa la seguridad)**
1.  **Entrada Perimetral:** Una petición (ej. atacante escaneando vulnerabilidades) llega de Internet y atraviesa los firewalls base (AWS Security Group + UFW) hacia el puerto 443.
2.  **Recepción y Consulta:** El proxy Traefik recibe la petición web. Antes de redirigirla a la aplicación objetivo (ej. DVWA), el "Bouncer" entra en acción.
3.  **Detección Activa:** CrowdSec, que analiza constantemente los logs de Traefik, detecta el comportamiento anómalo y las firmas maliciosas de la petición.
4.  **Bloqueo Efectivo:** CrowdSec añade la IP del atacante a su lista negra. El Bouncer ordena a Traefik denegar el acceso instantáneamente (Error 403 Forbidden) protegiendo la app.
5.  **Monitorización:** Todo el incidente de seguridad es recolectado por Prometheus y se refleja visualmente en los paneles de Grafana.

> **[🎨 SUGERENCIA VISUAL PARA LA DIAPOSITIVA]:** Un diagrama de flujo paso a paso con flechas e iconos:
> 👨‍💻 *Atacante* ➡️ ☁️ *AWS (Firewalls)* ➡️ 🚦 *Traefik* ↔️ 🛡️ *CrowdSec (Bloqueo)* ❌ 📦 *App (DVWA)*
> *Recomendación:* En PowerPoint, usa animaciones de "Aparecer" para que cada punto del 1 al 5 salga secuencialmente. Así podrás contar la "historia" del bloqueo en directo.
>
> **[🤖 PROMPT PARA IA - DIAGRAMA CONCEPTUAL]:** *"A sleek modern workflow diagram. A malicious user sending a request to a cloud server, crossing an AWS firewall, reaching a Traefik proxy. The proxy communicates with a CrowdSec security shield that blocks the request with a red '403'. Another arrow points to a Grafana monitoring dashboard. Flat design, corporate tech style, vector art."*

---

## Diapositiva 11: Diseño del Sistema - Interfaz y Usabilidad
**Experiencia de Usuario y Gestión Administrador**
*   **Para el Administrador (Single Pane of Glass):** Gestión 100% visual y centralizada. No hace falta entrar por consola (SSH) para ver el estado del sistema; todo se supervisa mediante entornos web (Grafana y Traefik).
*   **Para el Usuario Final (Confianza Zero-Trust):** Navegación transparente con certificados SSL (Let's Encrypt) auto-renovables. Evita por completo los mensajes de "Sitio no seguro" en el navegador.
*   **Para el Despliegue (Dev):** Usabilidad basada en la simplicidad ("1-Click Deploy"). Toda la complejidad queda oculta tras la ejecución automatizada de Ansible y Terraform.

> **[📷 SUGERENCIA DE IMÁGENES PARA LA DIAPOSITIVA]:** 
> *   **Captura 1 (El candado HTTPS):** Una captura muy recortada de la barra del navegador mostrando la URL de tu aplicación (ej. https://tu-sitio.com/dvwa) con el **candado de seguridad desplegado**, donde se lea claramente "Conexión segura - Certificado válido emitido por Let's Encrypt". 
> *   **Captura 2 (Panel Traefik):** Un recorte del *Dashboard* de Traefik donde se vea la sección "HTTP Routers" con los recuadros verdes que demuestran visualmente que el enrutamiento y la salud de los servicios es correcta (Success).

---

## Diapositiva 12: Desarrollo - Entorno y Herramientas (I)
**Infraestructura y Configuración Base**
*   **IDE Local:** Visual Studio Code (WSL2).
*   **Terraform:** Provisión de la instancia EC2 (`main.tf`).
*   **Ansible:** Preparación automática del servidor (`playbook.yml`). 
> **[📷 SUGERENCIA DE IMAGEN]:** 
> 1. Captura de VS Code mostrando un fragmento de código de Terraform (`main.tf`).
> 2. Captura de terminal ejecutando Ansible con las tareas en "changed" (amarillo) y "ok" (verde).

---

## Diapositiva 13: Desarrollo - Orquestación (II)
**Stack de Contenedores (Docker Compose)**
*   **Traefik:** Proxy Inverso SSL.
*   **CrowdSec:** IPS (Prevención de ataques).
*   **App / DVWA:** Aplicaciones (protegidas).
*   **Prometheus / Grafana:** Observabilidad.
> **[📷 SUGERENCIA DE IMAGEN]:** Fragmento breve de código del archivo `docker-compose.yml` destacando algún servicio.

---

## Diapositiva 14: Desarrollo - Dificultades y Soluciones
 
> **[🎨 SUGERENCIA VISUAL]:** Uso de iconos vectoriales (Warning o candados, checks verdes de solución) al lado de cada punto para que sea más esquemático y visual.
