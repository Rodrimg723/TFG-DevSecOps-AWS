# 🛡️ Infraestructura Cloud Automatizada & DevSecOps (TFG ASIR)

![DevSecOps Banner](docs/images/banner.png)

Este repositorio contiene la implementación completa de una **Infraestructura Cloud Segura por Diseño (DevSecOps)** desplegada en **AWS** de forma completamente automatizada mediante **Infraestructura como Código (IaC)** y **Gestión de Configuración**.

El proyecto demuestra cómo migrar del paradigma de administración tradicional ("Servidores Mascota") al paradigma de automatización moderno ("Servidores Ganado"), implementando políticas avanzadas de ciberseguridad, prevención activa de intrusiones y observabilidad en tiempo real.

---

## 🛠️ Tecnologías Utilizadas

Un stack tecnológico robusto y moderno enfocado en la automatización y la seguridad:

| Área | Tecnologías |
|---|---|
| **Proveedor Cloud** | ![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=flat-square&logo=amazon-aws&logoColor=white) |
| **Infraestructura como Código** | ![Terraform](https://img.shields.io/badge/Terraform-7B12EE?style=flat-square&logo=terraform&logoColor=white) |
| **Gestión de Configuración** | ![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white) |
| **Virtualización y Contenedores** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) |
| **Proxy Inverso y SSL** | ![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=flat-square&logo=traefik&logoColor=white) |
| **Seguridad Activa (IDS/IPS)** | ![CrowdSec](https://img.shields.io/badge/CrowdSec-FF4F00?style=flat-square&logo=crowdsec&logoColor=white) |
| **Métricas y Observabilidad** | ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) |

---

## 📐 Arquitectura del Sistema

La arquitectura está diseñada bajo el principio de **Defensa en Profundidad**, combinando firewalls perimetrales en la nube con firewalls a nivel de host, proxies seguros y agentes de seguridad activa en contenedores aislados.

```mermaid
graph TD
    %% Estilo de nodos
    classDef cloud fill:#232f3e,stroke:#3b4859,stroke-width:2px,color:#fff;
    classDef security fill:#a61c1c,stroke:#e6522c,stroke-width:2px,color:#fff;
    classDef container fill:#1d5f8a,stroke:#2496ed,stroke-width:2px,color:#fff;
    classDef client fill:#3b5998,stroke:#8b9dc3,stroke-width:2px,color:#fff;

    %% Elementos Externos
    Client[👤 Usuario / Atacante]:::client -->|Petición HTTPS| Internet((🌐 Internet))

    subgraph AWS [VPC - AWS Cloud]
        direction TB
        
        %% Security Group
        subgraph SG [Security Group Perimetral]
            direction LR
            P22[Puerto 22 SSH]
            P80[Puerto 80 HTTP]
            P443[Puerto 443 HTTPS]
            P3000[Puerto 3000 Grafana]
        end
        
        %% Servidor EC2
        subgraph EC2 [Instancia EC2: Ubuntu Server 22.04]
            direction TB
            UFW[🛡️ Firewall Interno: UFW]
            
            %% Docker
            subgraph Docker [Red Docker: web]
                Traefik[🐳 Traefik Proxy Inverso]:::container
                DVWA[🎯 DVWA App Víctima]:::container
                Bouncer[🧩 CrowdSec Bouncer]:::security
                CrowdSec[🔥 CrowdSec Engine IDS]:::security
                Prometheus[📊 Prometheus Engine]:::container
                Grafana[📈 Grafana Dashboard]:::container
            end
        end
    end

    %% Conexiones
    Internet --> SG
    P80 --> UFW
    P443 --> UFW
    P22 --> UFW
    P3000 --> UFW
    
    %% Flujo interno de la red Docker
    UFW --> Traefik
    Traefik <-->|Forward Auth| Bouncer
    Bouncer <-->|Verifica IP Banned| CrowdSec
    Traefik -->|Rutea tráfico seguro| DVWA
    
    %% Flujo logs y monitorización
    Traefik -->|Genera access.log| CrowdSec
    Prometheus -->|Scrapea Métricas| Traefik
    Prometheus -->|Scrapea Métricas| CrowdSec
    Grafana -->|Visualiza| Prometheus

    %% Asignación de estilos
    class AWS,SG,EC2 cloud;
    class UFW,Bouncer,CrowdSec security;
    class Docker,Traefik,DVWA,Prometheus,Grafana container;
```

---

## 🔒 Bucle de Seguridad Activa: Detección y Mitigación (IPS)

A diferencia de las soluciones pasivas, este sistema detecta comportamientos sospechosos en tiempo real mediante **CrowdSec** y los bloquea directamente en el punto de entrada (**Traefik**) antes de que impacten en la aplicación interna.

```mermaid
sequenceDiagram
    autonumber
    actor Atacante as 👤 Atacante / Escáner
    participant Traefik as 🐳 Traefik (Proxy Inverso)
    participant Bouncer as 🧩 CrowdSec Bouncer
    participant DVWA as 🎯 DVWA (App Víctima)
    participant CrowdSec as 🔥 CrowdSec Engine (IDS)

    %% Paso 1: Petición Normal o Inicial
    Atacante->>Traefik: Envía petición HTTP/HTTPS
    Note over Traefik,Bouncer: Traefik consulta middlewares de seguridad
    Traefik->>Bouncer: ForwardAuth: ¿Esta IP está autorizada?
    Bouncer->>CrowdSec: Consulta tabla de decisiones (LAPI)
    CrowdSec-->>Bouncer: IP limpia (Sin incidencias)
    Bouncer-->>Traefik: Autorizado (HTTP 200 OK)
    Traefik->>DVWA: ProxyPass a la aplicación
    DVWA-->>Traefik: Devuelve código web
    Traefik-->>Atacante: Muestra la web

    %% Paso 2: Ataque e Identificación
    Note over Atacante,CrowdSec: [Simulación de Ataque Web / Inyección / Fuerza Bruta]
    Atacante->>Traefik: Realiza múltiples peticiones sospechosas
    Traefik->>CrowdSec: Escribe registros de acceso en `access.log` (Volumen compartido)
    Note over CrowdSec: CrowdSec analiza logs y detecta patrones maliciosos (Colección HTTP)
    CrowdSec->>CrowdSec: Agrega la IP atacante a la lista negra local (Decisión de bloqueo)

    %% Paso 3: Bloqueo Automático
    Note over Atacante,Traefik: [Siguiente petición del atacante]
    Atacante->>Traefik: Intenta acceder de nuevo
    Traefik->>Bouncer: ForwardAuth: ¿Esta IP está autorizada?
    Bouncer->>CrowdSec: Consulta tabla de decisiones
    CrowdSec-->>Bouncer: IP Bloqueada por CrowdSec (Ban activo)
    Bouncer->>Traefik: Rechazado (HTTP 403 Forbidden)
```

---

## 📂 Estructura del Repositorio

La organización del código sigue los estándares de la industria para la gestión de proyectos de infraestructura y seguridad:

```bash
.
├── ansible/                  # Automatización de la configuración del SO y Docker
│   ├── inventory.ini         # Definición de hosts de destino (IPs del servidor)
│   └── playbook.yml          # Tareas de aprovisionamiento, hardening y despliegue
├── terraform/                # Definición de Infraestructura como Código (IaC)
│   ├── main.tf               # Aprovisionamiento de VPC, Security Groups e Instancia EC2
│   ├── outputs.tf            # Variables de salida (IP Pública de la instancia)
│   └── provider.tf           # Configuración del proveedor de AWS
├── docker/                   # Definición y configuración de contenedores microservicios
│   ├── docker-compose.yml    # Orquestación de Traefik, CrowdSec, DVWA y Observabilidad
│   ├── security/             # Configuraciones específicas de CrowdSec (logs, acquis)
│   └── observability/        # Configuraciones y dashboards de Prometheus y Grafana
├── scripts/                  # Scripts auxiliares y herramientas de pentesting
│   ├── attack.py             # Script de simulación de ataques multihilo (User-Agent Nikto)
│   └── setup_wsl.sh          # Ayudante para preparar el entorno en Windows (WSL)
├── docs/                     # Documentación técnica, guías y recursos gráficos
│   └── images/               # Recursos gráficos y multimedia del README
├── .gitignore                # Reglas de exclusión de Git (prevención de fugas de claves)
├── LICENSE                   # Licencia de código abierto MIT
└── README.md                 # Guía general de presentación
```

---

## 🚀 Despliegue Automatizado en 3 Pasos

El despliegue está diseñado bajo la filosofía **Zero-Touch**. Sigue estos pasos secuenciales:

<details>
<summary>📋 Requisitos Previos</summary>

* Tener configuradas las credenciales de AWS (`aws configure` o variables de entorno de AWS Academy).
* Terraform instalado en tu máquina local.
* Ansible instalado en tu máquina local o en WSL.
* Clave privada SSH (`vockey.pem` / `vockey` o `labsuser.pem`) accesible.
</details>

### Paso 1: Infraestructura como Código (Terraform)
Accede a la carpeta de Terraform, inicializa los proveedores y despliega la infraestructura en AWS.
```bash
cd terraform
terraform init
terraform apply -auto-approve
```
*Al finalizar, Terraform imprimirá la dirección IP pública del servidor:* `server_public_ip = "X.X.X.X"`.

### Paso 2: Configuración del Sistema y Hardening (Ansible)
Edita el archivo `ansible/inventory.ini` reemplazando la dirección IP por la obtenida en el paso anterior. Luego ejecuta el playbook:
```bash
cd ../ansible
ansible-playbook -i inventory.ini playbook.yml
```
Este script configurará las dependencias, instalará Docker, endurecerá el SSH, y levantará el firewall local. Además, **de forma 100% automatizada**, recuperará la IP del servidor para configurar las reglas de dominio dinámico en Traefik y registrará el CrowdSec Bouncer con una clave estática segura.

### Paso 3: Verificación y Servicios Activos
Los servicios se levantarán de manera automática a través del playbook de Ansible en contenedores Docker aislados. Puedes verificar que la aplicación víctima está activa accediendo a las siguientes URLs:
* **DVWA (Segura con HTTPS)**: `https://<IP-PUBLICA>.nip.io/dvwa`
* **whoami (Validación HTTPS)**: `https://<IP-PUBLICA>.nip.io/whoami`
* **Grafana (Monitoreo)**: `http://<IP-PUBLICA>:3000` (Credenciales: `admin` / `admin`)

*Nota: La primera vez que accedas a la URL HTTPS, Let's Encrypt puede tardar entre 10 y 30 segundos en negociar el certificado digital. Si ves un error de carga, espera unos segundos y refresca.*

---

## 🔬 Demostración de Seguridad en Acción

### 1. Simulación de un ataque web
Para verificar que el sistema de detección y prevención activa (CrowdSec IPS) funciona, podemos simular un ataque de escaneo web rápido contra la aplicación víctima (DVWA) desde una máquina externa.

Puedes hacerlo de dos formas:

**Opción A: Ejecutar el script Python automatizado (Recomendada)**
Ejecuta el script proporcionado en la carpeta de herramientas pasándole la IP pública del servidor:
```bash
python scripts/attack.py <IP-PUBLICA>
```

**Opción B: Mediante bucle curl en Linux**
```bash
# Simular un ataque web usando curl inyectando patrones maliciosos en la URL
for i in {1..30}; do curl -H "Host: <IP-PUBLICA>.nip.io" -s -o /dev/null -w "%{http_code}\n" "http://<IP-PUBLICA>/dvwa/?id=../../etc/passwd"; done
```

### 2. Comportamiento esperado
1. **Las primeras peticiones** devolverán un código de respuesta regular (`200 OK` o `302 Redirect`).
2. **Tras superar el umbral de seguridad**, CrowdSec analiza los registros del log de Traefik, detecta el intento de Local File Inclusion (LFI) o escaneo automatizado y añade la IP al bouncer.
3. **Las peticiones posteriores** recibirán instantáneamente un código **`403 Forbidden`** de Traefik, bloqueando al atacante del sistema por completo.

```bash
# Salida de consola esperada tras activarse el bloqueo
HTTP/1.1 403 Forbidden
Content-Type: text/plain; charset=utf-8
Connection: close

Forbidden
```

### 3. Visualización en Grafana
Al acceder al panel de control de Grafana, el administrador podrá ver métricas detalladas en tiempo real:
* Tráfico procesado por Traefik.
* IPs activas escaneando el sistema.
* Número de decisiones tomadas por CrowdSec y las IPs actualmente bloqueadas a nivel global y local.

---

## 🧼 Destrucción y Limpieza
Para evitar costes innecesarios en la cuenta de AWS una vez completada la prueba, destruye la infraestructura con una sola orden:
```bash
cd terraform
terraform destroy -auto-approve
```

---

## 📄 Licencia
Este proyecto es de código abierto y está bajo la licencia [MIT](LICENSE).

---
*Proyecto realizado como Trabajo de Fin de Grado (TFG) para el Ciclo de Administración de Sistemas Informáticos en Red (ASIR).*
*Desarrollado con dedicación por **Rodrigo**.*
