# Explicación de la Infraestructura con Terraform

Este documento detalla el propósito de cada bloque de código en el archivo `terraform/main.tf` y cómo se orquesta la infraestructura en AWS.

## Estructura de Archivos

*   **`main.tf`**: Archivo principal donde se definen los recursos (servidor, seguridad, red).
*   **`outputs.tf`**: Define qué información nos mostrará Terraform al terminar (ej: la IP pública del servidor).
*   **`.terraform/`**: Directorio interno de Terraform (no tocar).

## Análisis de `main.tf`

### 1. Proveedor (Provider)
```hcl
provider "aws" {
  region = "us-east-1"
}
```
*   **Qué hace:** Indica a Terraform que vamos a trabajar con Amazon Web Services (AWS) en la región de "Norte de Virginia" (`us-east-1`). Esta región es la estándar y suele ser la más barata/compatible.

### 2. Red por Defecto (Data Source)
```hcl
data "aws_vpc" "default" {
  default = true
}
```
*   **Qué hace:** Busca la "Nube Privada Virtual" (VPC) que viene por defecto en tu cuenta de AWS. No creamos una nueva para simplificar, usamos la que ya existe.

### 3. Grupo de Seguridad (Security Group)
```hcl
resource "aws_security_group" "main" { ... }
```
*   **Qué hace:** Actúa como un *firewall* virtual para tu servidor. Define qué tráfico puede entrar (Ingress) y salir (Egress).

#### Reglas de Entrada (Ingress):
*   **Puerto 22 (SSH):** Permite tu conexión para administrar el servidor.
*   **Puerto 80 (HTTP):** Para tráfico web normal (Traefik entrada http).
*   **Puerto 443 (HTTPS):** Para tráfico web seguro (Traefik entrada https).
*   **Puerto 8080 (Traefik Dashboard):** Panel de control de Traefik.
*   **Puerto 3000 (Grafana):** Panel de monitorización.

> **Nota de Seguridad:** Actualmente las reglas permiten el acceso desde `0.0.0.0/0` (cualquier IP del mundo). En un entorno real de producción, el puerto 22 y 3000 deberían restringirse a "Tu IP".

#### Reglas de Salida (Egress):
*   Permite todo el tráfico de salida (`0.0.0.0/0`), necesario para que el servidor descargue actualizaciones, imágenes de Docker, etc.

### 4. Imagen del Sistema (AMI)
```hcl
data "aws_ami" "ubuntu" { ... }
```
*   **Qué hace:** Busca automáticamente la última versión disponible de **Ubuntu Server 22.04 LTS**. Esto asegura que siempre despliegues un sistema actualizado.

### 5. Instancia EC2 (El Servidor)
```hcl
resource "aws_instance" "server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.small"
  key_name      = "vockey"
  vpc_security_group_ids = [aws_security_group.main.id]
  ...
}
```
*   **`ami`**: Usa la imagen de Ubuntu encontrada en el paso anterior.
*   **`instance_type = "t2.small"`**: Define la potencia del servidor. `t2.small` tiene 1 vCPU y 2GB de RAM, suficiente para este proyecto.
*   **`key_name = "vockey"`**: Asocia la clave SSH llamada "vockey" (típica de AWS Academy) para que puedas conectarte sin contraseña.
*   **`vpc_security_group_ids`**: Aplica el firewall que definimos antes.

## Análisis de `outputs.tf`

```hcl
output "instance_public_ip" { ... }
```
*   **Qué hace:** Al terminar el despliegue, imprime en pantalla la dirección IP pública del nuevo servidor. Necesitarás esta IP para configurar Ansible y para acceder a tu web.
