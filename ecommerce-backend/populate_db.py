import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.main import app
from src.models.producto import Producto
from src.models.historial import Historial
from src.models.user import db
from datetime import datetime, timedelta
import random

def populate_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Sample products data
        productos_data = [
            {'nombre': 'MacBook Pro 14"', 'tipo': 'laptop', 'precio': 8500000, 'stock': 5},
            {'nombre': 'Dell XPS 13', 'tipo': 'laptop', 'precio': 4200000, 'stock': 12},
            {'nombre': 'HP Pavilion Gaming', 'tipo': 'laptop', 'precio': 3800000, 'stock': 8},
            {'nombre': 'Lenovo ThinkPad X1', 'tipo': 'laptop', 'precio': 6200000, 'stock': 3},
            {'nombre': 'ASUS ROG Strix', 'tipo': 'laptop', 'precio': 7500000, 'stock': 2},
            {'nombre': 'Samsung 27" 4K', 'tipo': 'monitor', 'precio': 1200000, 'stock': 15},
            {'nombre': 'LG UltraWide 34"', 'tipo': 'monitor', 'precio': 1800000, 'stock': 7},
            {'nombre': 'Dell UltraSharp 24"', 'tipo': 'monitor', 'precio': 950000, 'stock': 20},
            {'nombre': 'ASUS ProArt 32"', 'tipo': 'monitor', 'precio': 2500000, 'stock': 4},
            {'nombre': 'Logitech MX Master 3', 'tipo': 'mouse', 'precio': 350000, 'stock': 25},
            {'nombre': 'Razer DeathAdder V3', 'tipo': 'mouse', 'precio': 280000, 'stock': 18},
            {'nombre': 'Apple Magic Mouse', 'tipo': 'mouse', 'precio': 420000, 'stock': 10},
            {'nombre': 'Corsair K95 RGB', 'tipo': 'teclado', 'precio': 650000, 'stock': 6},
            {'nombre': 'Keychron K2', 'tipo': 'teclado', 'precio': 480000, 'stock': 14},
            {'nombre': 'Apple Magic Keyboard', 'tipo': 'teclado', 'precio': 520000, 'stock': 9}
        ]
        
        # Add products to database
        for producto_data in productos_data:
            producto = Producto(**producto_data)
            db.session.add(producto)
        
        # Sample historial data
        mensajes_sample = [
            "¿Cuántos laptops tenemos en stock?",
            "Mostrar productos con precio menor a 1000000",
            "¿Cuál es el producto más caro?",
            "Listar todos los monitores disponibles",
            "¿Qué productos tienen stock bajo?",
            "Mostrar laptops ordenados por precio",
            "¿Cuántos productos hay por categoría?",
            "Buscar productos de la marca Apple",
            "¿Cuál es el precio promedio de los laptops?",
            "Mostrar productos con stock mayor a 10"
        ]
        
        sql_queries_sample = [
            "SELECT COUNT(*) FROM productos WHERE tipo = 'laptop'",
            "SELECT * FROM productos WHERE precio < 1000000",
            "SELECT * FROM productos ORDER BY precio DESC LIMIT 1",
            "SELECT * FROM productos WHERE tipo = 'monitor'",
            "SELECT * FROM productos WHERE stock < 5",
            "SELECT * FROM productos WHERE tipo = 'laptop' ORDER BY precio",
            "SELECT tipo, COUNT(*) FROM productos GROUP BY tipo",
            "SELECT * FROM productos WHERE nombre LIKE '%Apple%'",
            "SELECT AVG(precio) FROM productos WHERE tipo = 'laptop'",
            "SELECT * FROM productos WHERE stock > 10"
        ]
        
        # Generate historial entries for the last 30 days
        base_date = datetime.now() - timedelta(days=30)
        for i in range(150):  # Generate 150 entries
            fecha = base_date + timedelta(
                days=random.randint(0, 30),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            )
            mensaje = random.choice(mensajes_sample)
            sql = random.choice(sql_queries_sample)
            
            historial = Historial(mensaje=mensaje, sql=sql, fecha=fecha)
            db.session.add(historial)
        
        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    populate_database()

