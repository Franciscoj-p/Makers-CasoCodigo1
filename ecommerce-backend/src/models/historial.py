from flask_sqlalchemy import SQLAlchemy
from src.models.user import db
from datetime import datetime

class Historial(db.Model):
    __tablename__ = 'historial'
    
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.Text, nullable=False)
    sql = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'mensaje': self.mensaje,
            'sql': self.sql,
            'fecha': self.fecha.isoformat() if self.fecha else None
        }

