def validar_id(id_valor):
    if not isinstance(id_valor, int) or id_valor <= 0:
        raise ValueError("ID debe ser número entero positivo")
    return id_valor

def validar_nombre(nombre):
    if not nombre or len(nombre) < 2:
        raise ValueError("Nombre debe tener al menos 2 caracteres")
    return nombre

def validar_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email inválido")
    return email.lower()

def validar_producto(producto):
    if 'productName' not in producto or 'quantity' not in producto or 'price' not in producto:
        raise ValueError("Producto debe tener: productName, quantity, price")
    if producto['quantity'] <= 0 or producto['price'] <= 0:
        raise ValueError("Quantity y price deben ser mayores a 0")
    return producto