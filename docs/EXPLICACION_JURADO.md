# 🚀 Guía Rápida y Letal para el Tribunal (8-10 Minutos)

Para ajustar el discurso a **8-10 minutos**, la estrategia es clara: **volar en las introducciones e índices**, y **pausar y lucirte en la arquitectura (el gorila/recepcionista) y los resultados (despliegue zero-touch)**. 

No leas este documento palabra por palabra, úsalo como bala para disparar los conceptos clave. Demuestra seguridad.

---

### [Diapositivas 1-3: Portada, Índice e Introducción] *(15 segundos)*
"Buenos días. Soy Rodrigo y voy a presentar mi TFG: 'Infraestructura Cloud Automatizada y Segura'. Vamos a ir directos al núcleo de cómo he implementado una arquitectura DevSecOps real y funcional."

### [Diapositiva 4-5: Contexto y Problema] *(30 segundos)*
"Históricamente, los servidores eran **'Mascotas'**: se montaban a mano, se les dedicaban horas y si enfermaban, pasábamos días arreglándolos. Además, salían a internet desnudos, siendo vulnerables desde el minuto cero.
Hoy, propongo tratar a los servidores como **'Ganado'**. Si uno falla, no lo curo: mi código lo destruye y crea uno nuevo, idéntico y con los escudos ya levantados, en minutos. Esto soluciona la lentitud y el error humano."

### [Diapositivas 6-9: Motivación, Objetivos y Alcance] *(30 segundos)*
"Mi objetivo ha sido demostrar dominio técnico creando una infraestructura 'Zero-Touch' (sin tocar la consola). He planificado la red, escrito la Infraestructura como Código, desplegado en AWS y, finalmente, la he atacado a propósito (Pentesting) para validar su blindaje."

### [Diapositivas 10-12: Análisis y Requisitos] *(30 segundos)*
"Decidí descartar servidores físicos y scripts básicos. El requisito era desplegar en la nube una máquina que rechace todo el tráfico excepto web cifrado (HTTPS), y que detecte y bloquee instantáneamente comportamientos anómalos."

### [Diapositiva 13: Tecnologías Seleccionadas] *(40 segundos)* *(Aquí empiezas a lucirte)*
"Para construir esto utilicé herramientas estándar de la industria:
- **AWS** es nuestro terreno físico.
- **Terraform** es la 'Constructora' que levanta el edificio vacío mediante código.
- **Ansible** son los 'Obreros' que instalan la electricidad y cambian cerraduras.
- Y **Docker** nos permite dividir el edificio en 'Habitaciones insonorizadas'. Si hackean un programa, no afecta al resto."

### [Diapositiva 14-16: Planificación y Arquitectura] *(30 segundos)*
"Tras 8 semanas de trabajo, el diseño final tiene 3 capas de defensa: El muro de Amazon (Security Group), el firewall de Ubuntu, y una red interna aislada en Docker."

### [Diapositiva 17-18: Diagramas Lógicos - EL PLATO FUERTE] *(1.5 a 2 minutos)* *(Habla más despacio y con contundencia)*
"Este es el corazón del proyecto. Aquí es donde la seguridad pasa de pasiva a activa.
Tenemos un equipo de seguridad trabajando en milisegundos:
1. **Traefik (El Recepcionista):** Es la única entrada. Solo permite conexiones con certificado SSL válido.
2. **DVWA (La Caja Fuerte):** He instalado una aplicación trampa, llena de vulnerabilidades a propósito, para usarla de cebo.
3. **CrowdSec (El Jefe de Seguridad):** Está oculto analizando todas las peticiones web en tiempo real.
4. **El Bouncer (El Gorila):** Es el intermediario.

Cuando un hacker intenta atacar nuestra caja fuerte trampa (DVWA), el Jefe de Seguridad detecta el patrón en los registros, avisa al Gorila por el pinganillo, y el Gorila le ordena al Recepcionista cerrarle la puerta en la cara al atacante con un Error 403. **El atacante es bloqueado antes de tocar la aplicación.** Y además, compartimos esa IP bloqueada con una red mundial para proteger a otros servidores."

### [Diapositiva 19-20: Interfaz de Grafana] *(30 segundos)*
"Para ver esta 'magia' invisible, instalé **Grafana**, que es mi Sala de Monitores. Aquí veo gráficos en tiempo real de cuántos ataques estamos recibiendo, de qué países vienen, y cómo el sistema los repele automáticamente."

### [Diapositivas 21-24: Desarrollo y Dificultades] *(40 segundos)*
"El desarrollo lo hice programando en Linux (WSL2), enfrentándome a una curva de aprendizaje casi vertical. Superé problemas de permisos en AWS, rotación constante de IPs y límites criptográficos, logrando parametrizar mi código para que fuera capaz de autodescubrir su configuración en cada encendido."

### [Diapositiva 25-28: Resultados] *(1 minuto)* *(Énfasis absoluto en lo que has conseguido)*
"¿Qué hemos conseguido? 
Primero: **Aprovisionamiento Zero-Touch**. Literalmente, ejecuto un comando y me voy a tomar un café. En 2 minutos, tengo un servidor en Estados Unidos, seguro, sin un solo error humano.
Segundo: **Seguridad 'Shift-Left'**. Las aplicaciones nacen protegidas.
Tercero: **Defensa Activa demostrada**. Lanzamos ataques reales de estrés y penetración y pudimos ver en directo cómo nuestra infraestructura absorbía el impacto y bloqueaba a los atacantes."

### [Diapositivas 29-31: Conclusiones y Retos] *(30 segundos)*
"En conclusión, he validado una arquitectura DevSecOps real y he demostrado dominio en tecnologías que normalmente escapan al ciclo básico, como IaC y contenedores."

### [Diapositivas 32-34: Líneas futuras] *(30 segundos)*
"El siguiente paso a nivel empresarial sería meter esto en Kubernetes para tener Auto-Escalado frente a millones de usuarios, y pipelines CI/CD para que el servidor se actualice solo cada vez que un desarrollador suba código, mandándome las alertas a Teams o Slack."

### [Diapositiva 35: Final] *(15 segundos)*
"Este proyecto refleja no solo lo aprendido en ASIR, sino el estándar de despliegue de las empresas punteras. Muchas gracias por su atención, quedo a su disposición para cualquier pregunta."

---

### 💡 Tips para clavar los 8 minutos:
1. **Pasa rápido las slides de "relleno"**: Diapositivas como el Índice, Alcance o Planificación pásalas casi sin respirar. Tu tribunal evaluará lo que sabes cuando hables de **Terraform, Docker y CrowdSec**.
2. **Véndete bien en los "Resultados"**: La frase *"Literalmente, ejecuto un comando y me voy a tomar un café. En 2 minutos tengo un servidor en Estados Unidos..."* demuestra mucha autoridad técnica y confianza. Haz que suene tan impresionante como realmente es.
