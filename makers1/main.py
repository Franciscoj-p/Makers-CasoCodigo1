from db import crear_tabla, insertar_producto, buscar_producto
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

if __name__ == "__main__":
    crear_tabla()

    #insertar_producto("Lenovo ThinkPad", 2500, 10)

    #resultados = buscar_producto("Lenovo")
    #for r in resultados:
    #   print(f"ID: {r[0]} | Nombre: {r[1]} | Precio: {r[2]} | Stock: {r[3]}")
    #client = genai.Client(api_key ="AIzaSyBX0D_zZgogy-Tn_zki5xEvDZdK-ESTMok")
    #TELEGRAM_TOKEN = "8229202118:AAFgBDvy03dbBv3ndfX_PEk7Jh3eRUpLXvg"