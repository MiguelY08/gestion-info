"""Validaciones para campos de cliente y producto"""

import re


def validate_id(client_id):
    """Valida que el ID sea un entero positivo"""
    if not isinstance(client_id, int) or client_id <= 0:
        raise ValueError("ID debe ser un entero positivo")
    return True


def validate_name(name):
    """Valida que el nombre tenga al menos 2 caracteres"""
    if not isinstance(name, str) or len(name.strip()) < 2:
        raise ValueError("Nombre debe tener al menos 2 caracteres")
    return True


def validate_email(email):
    """Valida formato de email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError("Email inválido")
    return True


def validate_product_name(name):
    """Valida nombre de producto"""
    if not isinstance(name, str) or len(name.strip()) < 1:
        raise ValueError("Nombre de producto no puede estar vacío")
    return True


def validate_quantity(quantity):
    """Valida que la cantidad sea un número positivo"""
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Cantidad debe ser un número positivo")
    return True


def validate_price(price):
    """Valida que el precio sea un número positivo"""
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Precio debe ser un número no negativo")
    return True