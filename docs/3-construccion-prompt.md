
```
Te paso a continuación un historial de conversaciones de una persona.

Quiero que rellenes la siguiente plantilla de perfil SOLO con la información que puedas inferir de forma clara y directa a partir del texto.

Si no puedes extraer un dato con certeza, deja el campo en blanco o escribe “unknown”.

Ejemplo de campo desconocido:  
"catchphrase": "unknown"

Por favor, responde únicamente con el JSON completo de la plantilla, sin añadir explicaciones ni texto adicional.

Plantilla de perfil:
[AQUÍ PEGAS EL JSON VACÍO DE LA PLANTILLA CON TODOS LOS CAMPOS]

Historial de conversación:
[AQUÍ PEGAS TODO EL TEXTO DE CONVERSACIÓN]
```

## Flujo por prompts para mucho texto (chunks)

### FASE 1: Extracción de evidencias por chunk

1. **Divide** el historial de conversación en trozos manejables (por ejemplo, de 5.000 a 10.000 tokens).
2. **Para cada chunk**, pásale un prompt al LLM tipo:
    
    ```
    A continuación tienes un extracto de una conversación. 
    Para cada uno de los siguientes campos de perfil, extrae todas las frases, citas, palabras o fragmentos que puedan ayudar a inferir ese campo.
    Si para algún campo no hay información relevante en este extracto, deja el campo vacío.
    
    [Pega aquí la lista de campos]
    
    Extracto de conversación:
    [Chunk de conversación]
    ```

### FASE 2: Agregación de evidencias

3. **Recoge todas las evidencias** extraídas de cada chunk y **fusiónalas** para cada campo (une listas, elimina duplicados).

### FASE 3: Perfilado final

4. **Con todas las evidencias reunidas**, pásale un prompt final al LLM como este:
    ```
    Tienes a continuación una recopilación de frases, palabras y evidencias relevantes extraídas de múltiples partes de un historial de conversación. 
    Utiliza únicamente estas evidencias para rellenar la siguiente plantilla de perfil. 
    Si para algún campo no hay suficiente información escribe “unknown”.
    
    Evidencias por campo:
    [Pega aquí el JSON de evidencias finales por campo]
    
    Plantilla de perfil:
    [Pega aquí la plantilla JSON vacía]
    ```
