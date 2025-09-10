from flask import Blueprint, jsonify
from src.models.historial import Historial
from sqlalchemy import func, desc
from datetime import datetime, timedelta

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics/queries-per-day', methods=['GET'])
def get_queries_per_day():
    try:
        # Get queries grouped by date
        queries = Historial.query.with_entities(
            func.date(Historial.fecha).label('date'),
            func.count(Historial.id).label('count')
        ).group_by(func.date(Historial.fecha)).order_by('date').all()
        
        result = [{'date': str(query.date), 'count': query.count} for query in queries]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/analytics/frequent-questions', methods=['GET'])
def get_frequent_questions():
    try:
        # Get top 10 most frequent questions
        questions = Historial.query.with_entities(
            Historial.mensaje,
            func.count(Historial.mensaje).label('count')
        ).group_by(Historial.mensaje).order_by(desc('count')).limit(10).all()
        
        result = [{'mensaje': q.mensaje, 'count': q.count} for q in questions]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/analytics/common-queries', methods=['GET'])
def get_common_queries():
    try:
        # Get most common SQL queries
        queries = Historial.query.with_entities(
            Historial.sql,
            func.count(Historial.sql).label('count')
        ).group_by(Historial.sql).order_by(desc('count')).limit(10).all()
        
        result = [{'sql': q.sql, 'count': q.count} for q in queries]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

