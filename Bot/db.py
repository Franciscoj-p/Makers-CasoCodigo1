import sqlite3
from datetime import datetime

DB_PATH = "../ecommerce-backend/src/database/app.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def ejecutar_sql(sql: str, params=None):
    """devuelve lista de diccionarios"""
    with get_connection() as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        filas = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description] if cursor.description else []

    resultados = [dict(zip(columnas, fila)) for fila in filas]
    return resultados

# registrar historial
def registrar_historial(mensaje: str, sql: str):
    sql_insert = """
    INSERT INTO historial (mensaje, sql, fecha)
    VALUES (?, ?, ?)
    """
    ejecutar_sql(sql_insert, (mensaje, sql, datetime.now()))