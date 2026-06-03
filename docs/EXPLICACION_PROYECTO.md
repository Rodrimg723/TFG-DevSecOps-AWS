# 🚀 Infraestructura Cloud Automatizada y Segura (DevSecOps)
## Documento Explicativo del Proyecto

Este documento proporciona una explicación clara, estructurada y perfecta sobre el Trabajo de Fin de Grado (TFG) de **Rodrigo**, del ciclo formativo de **Administración de Sistemas Informáticos en Red (ASIR)**. Sirve como guía definitiva para comprender la totalidad del proyecto, desde la problemática inicial hasta la solución técnica implementada.

---

### 1. El Problema: El Mundo Tradicional
Tradicionalmente, cuando una empresa necesita un servidor web, un administrador de sistemas realiza el proceso de forma **manual**:
1. Crea una máquina virtual.
2. Se conecta a ella.
3. Instala los programas necesarios comando a comando.
4. Abre los puertos.

Este enfoque crea lo que se conoce como **"Servidores Mascota"**. Son únicos, se les coge cariño, pero si se rompen, reconstruirlos es un proceso lento, doloroso y propenso a errores humanos (lo que se conoce como *Configuration Drift* o "funciona en mi máquina pero no en producción"). 

Además, la seguridad solía ser un parche de última hora: los servidores se conectaban a internet sin protección activa, siendo vulnerables desde el primer minuto a ataques automatizados (bots y escáneres).

### 2. La Solución: DevSecOps y el "Ganado"
El proyecto propone cambiar de paradigma y tratar a los servidores como **"Ganado"**. Si un servidor falla, no se repara a mano: se destruye y se crea uno idéntico en cuestión de minutos de forma automatizada. 

Para lograrlo, se implementa la filosofía **DevSecOps** (Desarrollo, Seguridad y Operaciones), que integra la seguridad desde el inicio del diseño de la infraestructura, no al final. 

La solución técnica se basa en **Infraestructura como Código (IaC)**. Toda la red, los servidores, los firewalls y las aplicaciones se definen en líneas de código. Al ejecutar ese código, la infraestructura se levanta sola ("Zero-Touch").

---

### 3. Fases del Proyecto y Tecnologías Clave

El despliegue está dividido en tres fases principales totalmente secuenciales y automatizadas:

#### Fase 1: Provisionamiento (La "Chapa" Virtual) - **Terraform** & **AWS**
Se utiliza **Terraform** para hablar con la nube de Amazon (**AWS**). Terraform lee un archivo de configuración (`main.tf`) y le dice a AWS:
* *"Créame un servidor (EC2 `t2.small` con Ubuntu 22.04)."*
* *"Créame un firewall perimetral (Security Group) que bloquee todo excepto el tráfico web (80/443) y el de administración segura (22)."*
En segundos, tenemos la máquina física virtualizada y encendida, con una IP pública, sin haber hecho ni un solo clic en la consola de Amazon.

#### Fase 2: Configuración (El Cerebro del Servidor) - **Ansible**
Una vez la máquina está encendida, entra en juego **Ansible**. Ansible se conecta al nuevo servidor y lo configura automáticamente:
* Actualiza el sistema operativo.
* Instala las herramientas base (como Docker).
* Levanta un segundo firewall interno (UFW) como "defensa en profundidad".
* Deshabilita el acceso por contraseña (obligando a usar claves criptográficas para evitar ataques de fuerza bruta por SSH).
Ansible garantiza que el servidor siempre quede en el mismo estado perfecto, sin importar cuántas veces lo ejecutemos.

#### Fase 3: Despliegue de Servicios y Seguridad - **Docker** & **CrowdSec**
Finalmente, las aplicaciones se levantan utilizando **Docker** (contenedores). En lugar de instalar los programas mezclados en el servidor, cada programa vive en su propio contenedor aislado. El ecosistema levantado incluye:

1. **Traefik (El Portero de Discoteca):** Es el Proxy Inverso. Es la única puerta de entrada. Recibe todo el tráfico de internet, cifra las conexiones con certificados SSL automáticos (Let's Encrypt para que salga el candadito HTTPS) y envía al usuario al contenedor correcto.
2. **Aplicación Vulnerable (DVWA):** Es la aplicación "víctima". Se despliega intencionalmente llena de fallos para poder realizar pruebas de ataques (Pentesting).
3. **CrowdSec (El Guardaespaldas Activo):** Es un Sistema de Prevención de Intrusiones (IPS). Se dedica a leer los registros (logs) de Traefik. Si detecta que una IP de internet está haciendo cosas raras (como buscar vulnerabilidades en nuestra aplicación víctima), CrowdSec la detecta en milisegundos y le dice a Traefik que bloquee esa IP. El atacante recibe un error `403 Forbidden` instantáneo y se queda fuera. Además, comparte esa IP bloqueada con una red comunitaria global.
4. **Prometheus y Grafana (Las Cámaras de Seguridad):** Prometheus recopila constantemente métricas del sistema (uso de CPU, tráfico, ataques). Grafana coge esos datos crudos y los pinta en paneles visuales (dashboards) súper estéticos y en tiempo real. 

---

### 4. El Flujo de Trabajo en Acción (Resumen)

Si un pirata informático intenta atacar la infraestructura:
1. El atacante lanza un escaneo automático contra la IP del servidor.
2. **AWS** deja pasar el tráfico porque va al puerto 443 (Web).
3. **Traefik** recibe la petición, pero **CrowdSec** está vigilando.
4. **CrowdSec** identifica las firmas del ataque en los logs.
5. Inmediatamente, la IP entra en la lista negra. **Traefik** corta la conexión. El atacante no llega ni a tocar la aplicación.
6. El administrador, desde su casa, abre su panel de **Grafana** y ve un pico en el gráfico que dice: *"1 ataque de fuerza bruta bloqueado procedente de Holanda"*.

### 5. Conclusión del Proyecto

El proyecto logra **automatización total**. Lo que antes llevaba a un técnico 4 horas de configuración manual propensa a errores, ahora se despliega en **menos de 5 minutos** ejecutando un par de scripts. 

Pero lo más importante: **es seguro por diseño**. No es un servidor expuesto y vulnerable esperando a ser protegido; nace con capas de blindaje activo (AWS SG, UFW local, IPS CrowdSec) y es completamente observable a través de Grafana. 

El resultado es una arquitectura altamente profesional, resiliente y de nivel empresarial (DevSecOps), que demuestra el dominio integral de sistemas, redes, nube y ciberseguridad.
