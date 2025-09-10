from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from google import genai
from google.genai import types
import db
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key =os.getenv('GeminiKey'))
TELEGRAM_TOKEN = os.getenv('TelegramKey')

SYSTEM_PROMPT_QUERY = """
Eres un asistente de ventas que analiza preguntas de los usuarios.
Tu objetivo es decidir si se requiere consultar la base de datos del inventario 'productos'.

La tabla 'productos' tiene la siguiente estructura:

id INTEGER NOT NULL, 
nombre TEXT NOT NULL, 
tipo TEXT NOT NULL, 
precio FLOAT NOT NULL, 
stock INTEGER NOT NULL, PRIMARY KEY (id)

- Si el mensaje es un saludo, comentario o algo que no necesita consulta a la base de datos, responde en formato JSON:
{
  "consulta": false,
  "respuesta": "<respuesta natural>"
}

- Si el mensaje requiere consultar la base de datos, responde en formato JSON:
{
  "consulta": true,
  "sql": "<consulta SQL válida usando la tabla productos>"
}

Ejemplos:

Entrada: "Hola, ¿cómo estás?"
Salida:
{
  "consulta": false,
  "respuesta": "Hola! Estoy bien, ¿y tú?"
}

Entrada: "Cuánto valen los teclados?"
Salida:
{
  "consulta": true,
  "sql": "SELECT nombre, precio FROM productos WHERE tipo = 'teclado';"
}

Entrada: "¿Hay laptops Lenovo en stock?"
Salida:
{
  "consulta": true,
  "sql": "SELECT * FROM productos WHERE nombre LIKE '%Lenovo%' AND tipo = 'laptop' AND stock > 0;"
}

Entrada: "Muestra todos los monitores"
Salida:
{
  "consulta": true,
  "sql": "SELECT * FROM productos WHERE tipo = 'monitor';"
}
"""

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text

    try:
        # Paso 1: Decidir si hay consulta
        response_query = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT_QUERY,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            response_mime_type="application/json"
        ),
        contents=mensaje
    )


        respuesta_query = response_query.text.strip()
        data = json.loads(respuesta_query)
        print("JSON recibido de Gemini:", data)

        if not data.get("consulta", False):
            # sin consulta
            await update.message.reply_text(data.get("respuesta", ""))

        else:
            # consulta
            sql = data.get("sql", "")
            print("SQL generado:", sql)
            resultados = db.ejecutar_sql(sql)
            db.registrar_historial(mensaje, sql)
            print("Resultados de la consulta:", resultados)


            # Paso 2: Pasar consulta + mensaje original a Gemini
            response_final = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Pregunta: {mensaje}\nResultados de la consulta: {resultados}\n"
                         "Eres un agente de ventas, genera una respuesta natural para el usuario usando como base los resultados de la consulta en el inventario."
            )
            respuesta_final = response_final.text.strip()

            await update.message.reply_text(respuesta_final)

    except Exception as e:
        print("ERROR DETECTADO:", e) 
        await update.message.reply_text(f"Hubo un error al generar la respuesta: {e}")


# iniciar el bot
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

if __name__ == "__main__":
    print("Bot corriendo...")
    app.run_polling()
