from flask import Blueprint, jsonify
from src.models.producto import Producto

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    try:
        productos = Producto.query.all()
        return jsonify([producto.to_dict() for producto in productos])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

