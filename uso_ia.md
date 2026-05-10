en este documento se detalla como se realizo el desarrollo con ia.

la  eva especificamente esta en static/js & templates

Link del repo: https://github.com/cisternasfelipe/swarm-of-agents

primer punto, si bien sabemos que el uso generativo total de codigo hecho por ia esta autorizado por el docente, en esta evaluacion se valora el entendimiento de los fundamentos los cuales me ayudaran mas a futuro a manejar de mejor manera la ia teniendo nocion y entendimiento de lo que hago.

la herramienta usada fue claude en su version web. fue configurado como tutor socratico, este en vez de generar codigo me guío el razonamiento mediante preguntas para que construyera cada funcion por mi mismo.

el prompt para que la ia se comportara de tal manera fue: {Se breve cuando no sea necesario alargar una respuesta, si una respuesta es larga debe ser larga por que es necesario que sea larga no por relleno. Aplicas un enfoque socratico enseñas al usuario haciendo que el logre llegar a las respuestas a travez de preguntas}

de esta manera se consiguieron bastantes hitos, de los cuales detallare 5:

1. Estructura HTML — parti de un formulario plano y razone zona por zona usando ia: sidebar, navbar, chat-section, input-bar. Cada div fue justificado antes de escribirlo.

2. renderMessage() — identifique que necesitaba un arreglo interactions[] como fuente de verdad antes del DOM, luego construi la función con createElement, className, textContent vs innerHTML para seguridad XSS, y scrollTop = scrollHeight para auto-scroll.

3. handleKey() — descubri que event.key y event.shiftKey son propiedades separadas, que "ENTER" vs "Enter" importa, y que Shift+Enter necesita preventDefault() + agregar \n manualmente es importante hacerlo con "".

4. toggleSidebar() — logre identificar que desktop y móvil necesitan comportamientos distintos (width: 0 vs left: -260px), y use window.innerWidth para detectar el contexto en runtime.

5. Animación CSS — llegue a la conclusion que display: none no se puede animar, y por eso max-height: 0 → 120px con transition es la solución correcta para el panel de system prompt.