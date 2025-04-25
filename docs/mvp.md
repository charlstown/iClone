
## Alcance del MVP
Para este primer MVP, **simplificamos al máximo el proceso**. Por eso:

- **No haremos preprocesamiento ni limpieza de los datos**  
    → Los historiales de conversación se usarán tal cual, sin filtrar ni normalizar.
- **No calcularemos la completitud del perfil**  
    → En esta fase, no se medirá el porcentaje de campos rellenados ni la confianza en los resultados.

Esto nos permite avanzar rápido y ver si el proceso general funciona, dejando para futuras versiones la mejora de la calidad de los datos y la medición de completitud del perfil.

El objetivo es validar el flujo básico de extracción de los datos, generación del perfil mediante LLM y almacenamiento del resultado. En futuras iteraciones, se valorará incluir tanto el preprocesamiento como el cálculo automático de la completitud del perfil para mejorar la robustez y comparabilidad de los resultados.

## Arquitectura funcional

### 1. Extracción e importación de datos

- **Objetivo:**  
    Obtener los historiales de conversación en un formato legible por el sistema.
    
- **Tareas detalladas:**
    
    - Recopilar los archivos exportados de WhatsApp, emails u otros chats en formato texto (por ejemplo, `.txt` o `.eml`).
    - Guardar los archivos en una carpeta específica del proyecto.
    - Verificar que los archivos contienen los mensajes de interés (sin transformación adicional).
### 2. [Definición de la plantilla de perfil](https://github.com/charlstown/iClone/blob/main/docs/2-definicion-plantilla)

- **Objetivo:**  
    Establecer una estructura clara y uniforme para los atributos del perfil de usuario.
    
- **Tareas detalladas:**
    
    - Definir los campos clave que compondrán el perfil (por ejemplo: nombre, temas frecuentes, tono, etc.) y documentarlos.
    - Crear un archivo `perfil_schema.json` con los atributos definidos.
    - Garantizar que esta plantilla será la misma para todos los usuarios a analizar.
### 3. [Construcción del prompt](https://github.com/charlstown/iClone/blob/main/docs/3-construccion-prompt)

- **Objetivo:**  
    Preparar el mensaje que se enviará al LLM para que genere el perfil a partir de los datos proporcionados.
    
- **Tareas detalladas:**
    
    - Redactar un prompt claro donde se explique qué debe hacer el modelo (rellenar el JSON con los datos de la conversación).
    - Incluir en el prompt la plantilla del perfil y el texto de la conversación.
    - Instruir al LLM para que deje en blanco o marque como “desconocido” cualquier campo que no pueda inferir.
### 4. Envío de datos y generación del perfil

- **Objetivo:**  
    Ejecutar la petición al LLM y obtener la respuesta con el perfil generado.
    
- **Tareas detalladas:**
    
    - Programar un script en Python que lea el historial y la plantilla de perfil.        
    - Construir el prompt y enviarlo a la API del LLM (por ejemplo, OpenAI GPT).
    - Recibir y procesar la respuesta del modelo, asegurando que el resultado es un JSON válido.
### 5. Almacenamiento del perfil generado

- **Objetivo:**  
    Guardar de forma estructurada el perfil generado por el LLM.
- **Tareas detalladas:**
    - Validar que el JSON de salida cumple con el schema definido.
    - Guardar el perfil generado en un archivo (`perfil_usuario.json`) en la carpeta de resultados.
  
### 6. [Validación manual del perfil generado (prueba de simulación)](https://github.com/charlstown/iClone/blob/main/docs/6-validacion-manual)

- **Objetivo:**  
    Comprobar que el perfil generado puede ser utilizado por un LLM para simular razonablemente la forma de responder de la persona original.
    
- **Tareas detalladas:**
    
    - Tomar el JSON del perfil generado.
    - Preparar un prompt para el LLM del tipo:
        
        > “Responde como si fueras una persona con el siguiente perfil: [perfil_JSON]. Pregunta: [aquí tu mensaje]”
        
    - Realizar varias preguntas o situaciones y analizar si las respuestas del LLM se parecen al estilo y contenido de las respuestas originales.
    - (Opcional) Usar fragmentos de conversaciones originales y comparar la respuesta generada por el LLM con la real.
    - Documentar los resultados de la prueba, anotando observaciones sobre la similitud o diferencias con la personalidad original.
