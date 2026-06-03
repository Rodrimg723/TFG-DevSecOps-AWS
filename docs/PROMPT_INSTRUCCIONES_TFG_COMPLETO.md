---
title: "Prompt Maestro para generar el TFG (Memoria de 30-40 páginas)"
description: "Copia y pega este texto en Gemini Advanced, ChatGPT Plus o Claude 3 Opus. Como es un documento largo de 30-40 páginas, la IA se cortará si le pides todo de golpe. El truco es decirle que lo haga **por capítulos**."
---

# PROMPT MAESTRO PARA GENERAR EL TFG COMPLETO

**(⬇️ COPIA DESDE AQUÍ Y PÉGALO EN GEMINI / CHATGPT ⬇️)**

Actúa como un **Experto Redactor Técnico** y tutor de un Proyecto de Fin de Grado (TFG) para el ciclo superior de Administración de Sistemas Informáticos en Red (ASIR).

Mi objetivo es redactar la memoria final técnica de mi TFG. El documento debe tener una extensión estimada de entre 30 y 40 páginas, con un tono riguroso, corporativo, académico y muy técnico.

El proyecto se titula: **"Infraestructura Cloud Automatizada y Segura (DevSecOps)"**

Resumen del proyecto: 
Es una simulación de un escenario real donde una empresa necesita desplegar una aplicación web crítica en AWS. La solución implementada es una infraestructura moderna basada en la nube (AWS Academy), desplegada mediante Código (Terraform), configurada automáticamente (Ansible) y contenerizada (Docker Compose con Traefik como proxy inverso). Además, incluye una capa de seguridad activa comunitaria (CrowdSec IPS) y monitorización del sistema (Prometheus + Grafana).

**TUS INSTRUCCIONES ESTRICTAS (REGLAS DE GENERACIÓN):**

1. **Extensión y Profundidad:** No quiero resúmenes rápidos. Quiero hojas enteras de texto técnico profundo, con explicaciones detalladas de "cómo", "por qué", y "qué alternativas se descartaron". Debes incluir fragmentos de código ficticios o reales de configuración (YAML, HCL, Bash) para justificar las decisiones.
2. **Indicadores de Imágenes y Capturas:** A lo largo de todo el texto, debes dejar "huecos" explícitando qué captura de pantalla debo poner yo después. Usa el formato rojo o negrita (ej. `[📸 INSERTAR CAPTURA: Captura del panel EC2 de AWS mostrando la instancia en ejecución]`).
3. **Diagramas y Prompts:** Quiero que el documento tenga riqueza visual. Además de las capturas (que yo haré de mi terminal/AWS), debes incluir:
   * Código de diagramas en formato **Mermaid.js** (mapas de arquitectura, flujo de peticiones, diagrama de Gantt, topologías de red). 
   * **Prompts para Banano Pro / IAs de Generación de imágenes.** Allá donde un concepto sea muy abstracto, déjame un prompt explícito, indicando (fondo blanco, clean UI, etc) para que yo genere una ilustración explicativa y la inserte.
4. **Metodología de Generación:** Como no puedes generar 40 páginas de golpe sin cortarte, **NO ESCRIBAS NADA TODAVÍA**. 

Tu primera tarea es analizar este índice propuesto y confirmarme si estás listo para empezar de uno en uno:

**ÍNDICE PROPUESTO:**
* Capítulo 1: Introducción, justificación y objetivos (El problema de la infraestructura manual vs el paradigma DevSecOps "Mallas de servicios").
* Capítulo 2: Estado del arte y marco teórico comparativo (Cloud vs On-Prem, IaC, Contenedores, IPS).
* Capítulo 3: Planificación, recursos y cronograma de hitos.
* Capítulo 4: Diseño de la arquitectura lógica y física en AWS (Redes, VPC, Security Groups).
* Capítulo 5: Implementación técnica profunda detallada (Paso a paso: Terraform -> Ansible -> Traefik -> CrowdSec -> Aplicación).
* Capítulo 6: Pruebas de funcionamiento, estrés y validación de seguridad (Pentesting simulado bloqueado por CrowdSec).
* Capítulo 7: Monitorización, Conclusiones finales y vías de desarrollo futuro.
* Bibliografía y Referencias.

**¿ENTENDIDO?** Si has entendido todo, responde únicamente con: "¡Modo Redactor Académico Activado! Dime 'Empieza con el Capítulo 1' para generar tus primeras 3-5 páginas de profundidad técnica."

**(⬆️ HASTA AQUÍ EL PROMPT PRINCIPAL ⬆️)**

---

### CÓMO UTILIZAR ESTO CON LA IA:

1. Cópiate todo el bloque de texto superior y mándaselo a tu IA de confianza.
2. La IA te contestará algo corto confirmando que ha entendido todo.
3. Tú le dirás: **"Empieza con el Capítulo 1, escríbelo con máxima profundidad de detalles técnicos, hazlo de unas 4 páginas de largo."**
4. Te generará ese capítulo entero y se parará. Copias el texto a tu Word/Google Docs.
5. Luego le dices: **"Perfecto, el Capítulo 1 está genial. Ahora genera el Capítulo 2 aplicando la misma regla de extensión y profundidad."**
6. Y así sucesivamente hasta el Capítulo 7. 

Con este método irás rellenando las 30-40 páginas sin que la inteligencia artificial colapse a la mitad de la respuesta, y el texto estará repleto de huecos para tus capturas, prompts para generar diagramas bonitos y bloques de código Mermaid.
