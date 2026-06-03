# 🎤 Discurso de Presentación: TFG Infraestructura Cloud
**Tiempo estimado:** 15-20 minutos.
**Tono:** Profesional, seguro de ti mismo, técnico pero divulgativo. Imagina que se lo presentas a un cliente importante o al CTO de una empresa.

> **💡 CONSEJO ANTES DE EMPEZAR:** No leas la pantalla. Usa este guion para memorizar los puntos clave y mira a los profesores/tribunal a los ojos. Habla despacio, sobre todo en las partes técnicas. Cuando lleguen los diagramas, usa las manos para señalar o guiar su mirada.

---

### [Slide 1: Portada]
*(Sonríe, espera un segundo en silencio a que te presten atención antes de hablar).*
**"Buenos días al tribunal. Mi nombre es Rodrigo y a continuación voy a presentar mi Trabajo de Fin de Grado titulado 'Infraestructura Cloud Automatizada y Segura', enfocado en la metodología DevSecOps."**

### [Slide 2: Índice]
**"Para estructurar esta presentación, seguiremos este orden: comenzaremos viendo el contexto y por qué era necesario este proyecto. Pasaremos a los objetivos marcados, analizaremos las tecnologías escogidas y el diseño de la arquitectura. Finalmente, veremos el desarrollo técnico, los resultados obtenidos en vivo y acabaremos con las conclusiones y posibles mejoras futuras."**

### [Slide 3: Introducción]
*(Transición de sección. Haz una micropausa).*

### [Slide 4: Contexto del proyecto]
**"Para entender este proyecto, hay que entender cómo ha cambiado el paradigma de la informática. Históricamente, tratábamos a los servidores como 'Mascotas': únicos, configurados a mano, y si se rompían, llorábamos y pasábamos días arreglándolos. 
Hoy, en entornos profesionales y en la nube, los servidores son 'Ganado': recursos efímeros y reemplazables. Si uno falla, se destruye y el sistema crea otro idéntico. 
Bajo este contexto, mi proyecto simula el despliegue crítico de una aplicación en Amazon Web Services, integrando la metodología DevSecOps: que significa, esencialmente, que la seguridad deja de ser un parche de última hora y se convierte en el pilar central desde el inicio del diseño."**

### [Slide 5: Necesidad detectada]
**"¿Qué problema solucionamos con esto? Básicamente, tres grandes males de la administración tradicional:**
1. **La configuración manual**, que acaba generando diferencias y errores inexplicables.
2. **La lentitud**, tardando días en provisionar entornos que la empresa necesita para ayer.
3. **La seguridad reactiva**, lanzando servidores expuestos que son vulnerables desde el minuto cero."

**"La solución que presento pasa por utilizar Infraestructura como Código (IaC), donde todo el servidor se escribe en líneas de texto, con escudos de defensa activos por defecto."**

### [Slide 6: Motivación]
**"A nivel personal, este TFG es la pieza que encaja todo lo aprendido en el ciclo de ASIR: Sistemas, Redes y Seguridad. A nivel profesional, dominar este stack técnico —como Terraform o Docker— es lo que demandan las empresas punteras hoy en día. Quería demostrar que soy capaz de desplegar algo real, moderno y listo para producción."**

### [Slide 7: Objetivos del Proyecto]
*(Transición de sección).*

### [Slide 8: Objetivos generales y específicos]
**"El objetivo principal ha sido diseñar y levantar una infraestructura cloud en Alta Disponibilidad y Seguridad en AWS, usando EXCLUSIVAMENTE código. 
Para ello, tracé objetivos específicos: eliminar la consola web usando Terraform, lograr que la máquina se configure de forma idéntica cada vez con Ansible, aislar las aplicaciones con Docker, frenar los ataques en tiempo real con CrowdSec, y finalmente, ver qué está pasando por dentro usando Grafana."**

### [Slide 9: Alcance del Proyecto]
**"El alcance es el ciclo de vida completo: Planificamos la arquitectura, escribimos el código, hicimos el despliegue automático en la nube y, para asegurarnos de que todo esto no es solo humo, lo sometimos a pruebas de ataque real (Pentesting) para validar nuestras defensas."**

### [Slide 10: Análisis y Planificación]
*(Transición de sección).*

### [Slide 11: Investigación previa]
**"Antes de tirar la primera línea de código, tuve que tomar decisiones arquitectónicas de peso. 
Descarté servidores físicos locales (On-Premise) en favor de la flexibilidad del Cloud. Descarté los scripts en Bash tradicionales en favor de la Infraestructura como Código. Y, por último, decidí que las aplicaciones correrían en contenedores en lugar de en máquinas virtuales pesadas por su ligereza."**

### [Slide 12: Requisitos funcionales y técnicos]
**"El entorno que vamos a desplegar consiste en una instancia pequeña de Ubuntu en AWS. 
Pero lo importante no es la potencia, sino sus reglas: una red muy restrictiva, acceso web obligatoriamente cifrado con HTTPS válido de Let's Encrypt, y bloqueos automáticos en el momento en que se detecte el más mínimo comportamiento anómalo por parte de un visitante."**

### [Slide 13: Tecnologías seleccionadas]
**"El stack técnico definitivo es este:"**
*(Ve señalando o enumerando con confianza)*
**"AWS para la infraestructura física subyacente. Terraform para provisionarla. Ansible para configurarla por dentro porque no requiere agentes instalados. Y Docker Compose para la orquestación. No escogí Kubernetes porque para la magnitud actual del proyecto añadiría una complejidad técnica y un coste innecesario, siendo Docker perfecto para la labor."**

### [Slide 14: Planificación]
**"Para asegurar el éxito en las 8 semanas que teníamos, estructuré todo en un diagrama de Gantt, dividiendo el trabajo en fases claras: Diseño, Implementación en AWS, Configuración de Docker/Ansible, Pruebas de estrés y la Documentación que hoy presento."**

### [Slide 15: Diseño del Sistema]
*(Transición de sección).*

### [Slide 16: Arquitectura General]
**"Vamos a ver cómo encajan estas piezas. La arquitectura tiene 3 capas:
A nivel AWS, el Security Group corta casi todo. A nivel Ubuntu, un sistema minimalista sin basura. Y a nivel Docker, contenedores aislados que no exponen nada al mundo, salvo Traefik, nuestro proxy inverso, que es la única puerta de entrada y de salida."**

### [Slide 17: Diagrama Lógico (Entrada)]
**"En este diagrama lógico lo vemos claro. Imaginemos a un usuario o un atacante. Hace una petición por internet. Pasa los firewalls de Amazon y llega a Traefik por el puerto 443. Traefik hace de recepcionista. Pero, antes de dejar pasar a la visita hacia la aplicación web..."**

### [Slide 18: Diagrama Lógico (Defensa)]
**"...entra en juego nuestro Bouncer. CrowdSec es como nuestro guardaespaldas. Analiza de reojo a ese visitante. Si detecta que ese visitante está intentando escanear vulnerabilidades, inyectar SQL, o es una IP rusa conocida por ataques, CrowdSec mete a esa persona en la lista negra. Traefik le cierra la puerta en las narices con un Error 403. Y en cuestión de milisegundos, todo esto aparece dibujado en nuestros paneles de Grafana."**

### [Slide 19: Interfaz]
**"Aquí podéis ver la cara de ese sistema. A la izquierda, el router de Traefik. A la derecha, nuestro centro de mando en Grafana. No tenemos líneas de comandos aburridas, tenemos datos puros e interactivamente monitorizados."**

### [Slide 20: Usabilidad]
**"El foco fue la usabilidad. Para el administrador: control 100% visual y web. Para el usuario final: navegación fluida sin alertas molestas gracias al SSL renovado automáticamente. Para mí, el creador: una complejidad abrumadora escondida detrás de un despliegue transparente que se lanza pulsando un botón."**

### [Slide 21: Desarrollo]
*(Transición de sección).*

### [Slide 22: Entorno y Herramientas]
**"A nivel de desarrollo, mi base de operaciones fue Visual Studio Code utilizando WSL2 (el subsistema de Linux en Windows). Trabajando principalmente con archivos `main.tf` para Terraform y un gran `playbook.yml` para las rutinas de Ansible."**

### [Slide 23: Orquestación]
**"El corazón de las aplicaciones es el Docker Compose. Ahí definí los 5 servicios que conviven: Traefik (proxy), CrowdSec (Seguridad), Whoami (para pruebas lógicas), DVWA (nuestra aplicación vulnerable diseñada como cebo) y Prometheus/Grafana (para observarlo todo)."**

### [Slide 24: Dificultades y Soluciones]
**"Pero como en todo proyecto real, no fue un camino de rosas.
Me enfrenté a bloqueos de Amazon Academy que me obligaban a actualizar credenciales constantemente. Tuve dolores de cabeza con los límites de generación de certificados SSL gratuitos que me penalizaban si hacía pruebas de más. Y problemas de permisos de sistema y IPs dinámicas. Solucioné esto parametrizando mi código, haciéndolo lo suficientemente inteligente para detectar su propia IP cada vez que la máquina arrancaba de cero."**

### [Slide 25: Resultados]
*(Transición de sección).*

### [Slide 26: Aprovisionamiento "Zero-Touch"]
**"Y llegamos a los resultados. ¿Qué hemos conseguido? Un aprovisionamiento Zero-Touch. Literalmente no toco la máquina. Ejecuto un script y en menos de 2 minutos tengo un servidor en Estados Unidos, con su IP, sus claves y su red, levantado sin cometer un solo error humano."**

### [Slide 27: Orquestación de Servicios]
**"Además de la infraestructura base, logramos que los microservicios se desplieguen y conecten entre sí solos, implementando eso que llamamos 'Shift-Left': aplicar el hardening o blindaje al principio, antes de que el servidor vea la luz de internet."**

### [Slide 28: Monitorización y Defensa Activa]
**"Pero mi resultado favorito es la Defensa Activa. Al simular ataques reales contra el entorno logramos mitigaciones en directo. En Grafana podíamos ver cómo, de repente, IPs de Rusia o de Países Bajos intentaban escanear mis puertos, y CrowdSec los baneaba sin que yo levantara un dedo. Tenemos una máquina que se defiende sola."**

### [Slide 29: Conclusiones]
*(Transición de sección).*

### [Slide 30: Evaluación de Objetivos]
**"Si volvemos a la lista de objetivos iniciales, podemos marcarlos todos en verde.
Hemos validado una arquitectura DevSecOps real. He demostrado dominio técnico de herramientas corporativas. Y hemos comprobado que el entorno aguanta el estrés y el asedio, además de ser capaz de regenerarse si fuera destruido."**

### [Slide 31: Retos y Limitaciones]
**"Ha sido un reto inmenso. La curva de aprendizaje de unir tantas herramientas que no conocía ha sido vertical. Además, la limitación de estar en un entorno académico y no en una cuenta 'Premium' de AWS me limitó a la hora de poder simular ataques de denegación de servicio (DDoS) masivos."**

### [Slide 32: Líneas futuras]
*(Transición de sección).*

### [Slide 33: Automatización Continua]
**"Este TFG no es el final de la infraestructura, es la base sólida. En el futuro, el siguiente paso sería integrarlo en una pipeline de CI/CD (con GitHub Actions por ejemplo), donde ni siquiera tenga que lanzar el código desde mi ordenador local, sino que se haga solo al subir código al repositorio, e integre alertas directas a mi Slack o Teams."**

### [Slide 34: Escalabilidad]
**"A nivel empresarial masivo, este sistema está listo para evolucionar. El paso lógico sería llevar nuestros contenedores de Docker a clusters de Kubernetes para escalar los servidores a demanda, e implementar arquitecturas Multi-Zona de AWS para asegurar que, si un data center entero de Amazon arde en llamas, nuestra aplicación no caiga ni un segundo."**

### [Slide 35: Final y Preguntas]
*(Cambia tu postura, relájate y sonríe).*
**"Con esto concluye la presentación de la infraestructura. Esta metodología es el estándar actual del mercado y estoy muy orgulloso de haber podido llevarlo a cabo desde cero. Muchas gracias a todos por vuestra atención. Quedo a vuestra entera disposición para cualquier pregunta técnica o duda que queráis plantearme."**

---
*(La última diapositiva habla de "Homemate", es probable que sea una plantilla o un error de combinación de PDF de otro proyecto de DAM. Simplemente ignórala en tu defensa y detén la presentación en tu turno de preguntas).*
