# Explicación de la Automatización con Ansible

Este documento detalla qué hace cada tarea en el playbook `ansible/playbook.yml` para configurar automáticamente el servidor remoto.

## Estructura de Archivos

*   **`playbook.yml`**: Define la lista secuencial de "acciones" a realizar en el servidor.
*   **`inventory.ini`**: Lista los servidores donde Ansible debe conectarse.

## Análisis de `playbook.yml`

### 1. Cabecera (Play Definition)
```yaml
- name: DevSecOps Infrastructure Setup
  hosts: webservers
  become: true
  vars:
    project_dir: /opt/devsecops
```
*   **`hosts: webservers`**: Indica que este playbook se ejecutará solo en las máquinas definidas bajo el grupo `[webservers]` del inventario.
*   **`become: true`**: Ejecuta todas las tareas como superusuario (root/sudo), necesario para instalar paquetes.
*   **`vars`**: Define una variable `project_dir` para no repetir la ruta `/opt/devsecops` en todo el archivo.

### 2. Tareas (Tasks)

#### Actualización del Sistema
*   **`apt upgrade`**: Actualiza el índice de paquetes y el sistema operativo para aplicar parches de seguridad.
*   **`Install required packages`**: Instala herramientas básicas (`curl`, `git`, `htop`, etc.) necesarias para la gestión diaria.

#### Hardening (Seguridad del SO)
*   **`Configure UFW`**: Configura el firewall interno de Ubuntu (Uncomplicated Firewall). Bloquea todo por defecto (`deny incoming`) y solo permite:
    *   **OpenSSH**: Para no perder la conexión.
    *   **Puertos 80/443**: Tráfico web.
    *   **Puerto 8080/3000**: Paneles de administración (Traefik/Grafana).
*   **`Configure SSH`**: Edita `/etc/ssh/sshd_config` para deshabilitar la autenticación por contraseña (`PasswordAuthentication no`). Esto fuerza el uso de claves SSH, mucho más seguro.

#### Instalación de Docker
Esta sección sigue los pasos oficiales de Docker para Ubuntu:
1.  **Keyrings**: Crea directorio para guardar la clave GPG de Docker.
2.  **Download GPG Key**: Descarga la firma digital de Docker para verificar que el software es legítimo.
3.  **Add Repository**: Añade el repositorio oficial de Docker a las fuentes de actualizaciones (`sources.list`).
4.  **Install Docker Engine**: Instala el motor de contenedores (`docker-ce`) y sus plugins (`docker-compose-plugin`).
5.  **User Group**: Añade al usuario `ubuntu` al grupo `docker` para poder ejecutar comandos docker sin `sudo` (comodidad).

#### Despliegue de Aplicaciones (App Deployment)
Esta es la parte donde Ansible "entrega" tu proyecto al servidor:
1.  **`Ensure project directory exists`**: Crea la carpeta `/opt/devsecops` con los permisos correctos.
2.  **`Copy Docker files`**: Copia **todo** el contenido de tu carpeta local `docker/` a la carpeta remota. Esto incluye el `docker-compose.yml` y las configuraciones de seguridad/monitorización.
3.  **`Start Docker Compose`**: Ejecuta el comando final para levantar los contenedores:
    ```bash
    docker compose up -d
    ```
    El flag `-d` (detach) hace que corran en segundo plano.

### 3. Handlers
```yaml
  handlers:
    - name: Restart SSH
      service: name=ssh state=restarted
```
*   **Qué hace:** Los handlers son tareas especiales que solo se ejecutan si otra tarea "notifica" un cambio. En este caso, si modificamos la configuración SSH (línea 52), Ansible reiniciará el servicio SSH al final para aplicar los cambios.
