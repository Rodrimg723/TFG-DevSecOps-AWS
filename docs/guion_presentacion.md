# Guion para la Presentación del TFG: Infraestructura Cloud Automatizada y Segura

> **Consejo antes de empezar:** No memorices palabra por palabra. Utiliza este texto como una guía para saber qué decir y qué ideas clave transmitir en cada diapositiva. Respira despacio, mantén el contacto visual y confía en el trabajo que has hecho.

---

## Diapositiva 1: Portada
**Acción:** (Esperar a que se haga el silencio y sonreír).
**Discurso:** "Hola a todos, buenos días/tardes. Mi nombre es Rodrigo y a continuación voy a presentar mi Trabajo de Fin de Grado titulado 'Infraestructura Cloud Automatizada y Segura bajo metodología DevSecOps'. Este proyecto representa la culminación técnica de mis estudios en el ciclo de Administración de Sistemas Informáticos en Red."

## Diapositiva 2: Introducción al Proyecto
**Acción:** (Cambiar diapositiva).
**Discurso:** "Para empezar a entender este proyecto, hay que entender cómo ha evolucionado nuestro sector. Hemos pasado de tratar a los servidores como 'mascotas', a los que cuidábamos uno a uno, a tratarlos como 'ganado': recursos que son efímeros y reemplazables. En este proyecto replico un escenario real: el despliegue de una infraestructura completa en la nube (AWS), pero aplicando la cultura DevSecOps. Es decir, he integrado la seguridad de forma activa desde la primera línea de código para que el despliegue no solo sea rápido y repetible, sino seguro por defecto."

## Diapositiva 3: El Problema Detectado
**Acción:** (Cambiar diapositiva y poner tono ligeramente más serio).
**Discurso:** "La motivación de este proyecto surge de un problema clásico que se ve en las empresas. Los despliegues tradicionales y manuales generan lo que llamamos 'Drift', esa terrible frase de 'en mi máquina sí funciona' porque los servidores acaban desconfigurados. Además, es un proceso lento que lleva días y, lo más crítico: la seguridad suele dejarse para el final, cuando el servidor ya está expuesto en internet y vulnerable a ataques."

## Diapositiva 4: La Solución: DevSecOps
**Acción:** (Cambiar diapositiva con actitud resolutiva).
**Discurso:** "Frente a este problema, la solución es la Infraestructura como Código (IaC) en la que todo el entorno se despliega mediante scripts, y la seguridad es proactiva. Si un servidor falla o es atacado, no se repara a mano: se destruye y se redespliega desde cero en minutos gracias al código. Para mí ha sido la oportunidad perfecta de juntar todo lo aprendido en redes, sistemas y seguridad utilizando las herramientas demandadas actualmente en el mercado."

## Diapositiva 5: Objetivos del Proyecto
**Acción:** (Señalar ligeramente hacia la pantalla de vez en cuando).
**Discurso:** "Mi objetivo general ha sido desplegar esta infraestructura de alta disponibilidad en AWS. Y para conseguirlo, me marqué objetivos muy claros en 5 frentes:
1. Infraestructura como código utilizando Terraform.
2. Configuración y aprovisionamiento automático con Ansible.
3. El despliegue de las aplicaciones contenerizadas mediante Docker.
4. Una capa de seguridad activa con un IPS colaborativo, en este caso CrowdSec.
5. Y una capa de observabilidad completa y monitorización mediante Grafana."

## Diapositiva 6: Alcance del Proyecto
**Acción:** (Cambiar diapositiva).
**Discurso:** "Para conseguir estos objetivos, el proyecto se dividió en 4 grandes fases que simulan un ciclo DevSecOps profesional: Primero, una etapa de diseño y arquitectura de redes. Segundo, la programación de los módulos en Terraform y Ansible. Tercero, el despliegue sobre AWS Academy. Y por último y más importante, la etapa de validación, simulando ataques y poniendo a prueba el sistema."

## Diapositiva 7: Análisis de Tecnologías
**Acción:** (Cambiar diapositiva).
**Discurso:** "A nivel de tecnologías, he apostado por estándares de la industria. AWS porque es el líder del mercado y nos ofrece la mejor base. Opté por Terraform para levantar la infraestructura porque es un lenguaje agnóstico que me permite portar el código a otros proveedores si fuera necesario, y finalmente Docker Compose porque es perfecto para orquestar la magnitud de los servicios de nuestro entorno."

## Diapositiva 8: Stack DevSecOps
**Acción:** (Mencionar la tabla brevemente, sin leerla entera).
**Discurso:** "De forma rápida, aquí podéis ver cómo se engranan el resto de piezas. Ansible me garantiza que el servidor se configura siempre igual. Traefik me soluciona el enrutamiento de red y la inyección de certificados SSL de manera transparente. CrowdSec bloquea automáticamente las intrusiones aprendiendo de ataques globales, y Grafana me dibuja de forma visual qué está pasando en las tripas de la máquina."

## Diapositiva 9: Requisitos de la Infraestructura
**Acción:** (Cambiar diapositiva y mostrar seguridad técnica).
**Discurso:** "Todo este software corre bajo unos requisitos muy estrictos. La arquitectura se basa en una instancia EC2 dentro de una red pública (VPC). Cuenta con Security Groups nativos de AWS que operan como firewall de capa 4, restringiendo todo menos el puerto web y el de administración. Los accesos están fortificados: sin contraseña, solo mediante claves. El IPS bloquea IPs hostiles de forma automática y todo el tráfico viaja cifrado en HTTPS."

## Diapositiva 10: Planificación
**Acción:** (Cambiar diapositiva).
**Discurso:** "Por último, todo este esfuerzo se articuló en 8 semanas de trabajo continuo. Como se aprecia, fuimos desde el diseño teórico, pasando por el código, el despliegue final y rematando con simulaciones de estrés y documentación. Esto me ha permitido llevar un control riguroso de cada hito y llegar a un resultado final del que, tras muchas pruebas, estoy muy satisfecho."

## Diapositiva 11: Dificultades Técnicas y Soluciones
**Acción:** (Pausar ligeramente, dando entender que esto es fruto de la experiencia de campo).
**Discurso:** "Evidentemente, un proyecto así no ha estado exento de problemas en el mundo real. Me gustaría destacar tres grandes obstáculos que conseguí resolver:

1. **La obtención automática de certificados SSL con `.nip.io`:** Let's Encrypt aplicaba límites de tasa (rate limiting) severos al ser un dominio compartido para pruebas. La solución fue configurar el reto **HTTP-01** en Traefik y persistir los certificados en volúmenes Docker para evitar bloqueos por reintentos.
2. **El dinamismo de la IP en AWS:** La IP pública de la instancia EC2 cambiaba en cada despliegue. Tuve que automatizar la extracción de esta IP con 'Outputs' de Terraform para inyectarla directamente a Ansible y auto-configurar los dominios de las aplicaciones.
3. **Restricciones del Firewall (Security Groups):** El reto de Let's Encrypt exigía enviar peticiones exclusivas por el puerto 80 (HTTP). Modifiqué Terraform para abrir dicho puerto en AWS y configuré Traefik para redirigir forzosamente todo este tráfico a HTTPS (443), permitiendo solo la validación del certificado.
4. **Bloqueos de estado en Terraform:** Durante el desarrollo, cancelaciones inesperadas dejaron el entorno bloqueado impidiendo nuevos despliegues. Lo solucioné aprendiendo a limpiar manualmente los archivos de bloqueo (`.terraform.lock.hcl` y tfstate).
5. **Permisos de ejecución de Docker con Ansible:** Al provisionar los contenedores, los playbooks fallaban por falta de privilegios del usuario SSH. Lo resolví añadiendo una tarea de Ansible sistemática que agrega al usuario `ubuntu` al grupo `docker`.
6. **Sesiones efímeras en AWS Academy:** Al ser un entorno de laboratorio educativo, la sesión expiraba de forma recurrente. Me adapté implementando una rutina de actualización constante de las credenciales de AWS antes de levantar el entorno nuevamente."

## Cierre
**Acción:** (Cambiar a diapositiva final si hubiera o simplemente sonreír).
**Discurso:** "Con esto concluyen las dificultades destacadas y la presentación. A continuación daré paso a la demostración práctica del despliegue. Muchas gracias por su atención."
