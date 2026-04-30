"""Integración con pandas para exportar registros y crear clientes genéricos."""

import pandas as pd
from pathlib import Path


def create_client_record(*args, **kwargs):
    """Crea un registro de cliente usando *args y **kwargs."""
    if args:
        if len(args) < 3:
            raise ValueError("Se requieren id, nombre y email en args")
        client_id, nombre, email = args[:3]
    else:
        client_id = kwargs.get('id')
        nombre = kwargs.get('nombre')
        email = kwargs.get('email')

    if client_id is None or nombre is None or email is None:
        raise ValueError("Se requieren id, nombre y email para crear el registro")

    return {
        'id': client_id,
        'nombre': nombre,
        'email': email,
        'productos': kwargs.get('productos', [])
    }


def build_client_dataframe(clients, sort_by='nombre', ascending=True, filter_email_domain=None, **kwargs):
    """Genera un DataFrame a partir de una lista de clientes."""
    if not clients:
        return pd.DataFrame(columns=['id', 'nombre', 'email', 'productos', 'cantidad_productos', 'valor_total'])

    rows = []
    for client in clients:
        productos = client.get('productos', []) or []
        cantidad_productos = len(productos)
        valor_total = sum(p.get('cantidad', 0) * p.get('precio', 0) for p in productos)
        rows.append({
            'id': client['id'],
            'nombre': client['nombre'],
            'email': client['email'],
            'productos': ", ".join(p.get('nombre', '') for p in productos),
            'cantidad_productos': cantidad_productos,
            'valor_total': valor_total
        })

    df = pd.DataFrame(rows)

    if filter_email_domain:
        df = df[df['email'].str.endswith(f"@{filter_email_domain}")]

    if sort_by not in df.columns:
        raise ValueError(f"Columna de ordenación inválida: {sort_by}")

    return df.sort_values(by=sort_by, ascending=ascending).reset_index(drop=True)


def export_clients_to_csv(clients, filepath=None, **kwargs):
    """Exporta registros de clientes a CSV usando pandas."""
    filepath = filepath or Path('data') / 'clientes_reporte.csv'
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    df = build_client_dataframe(clients, **kwargs)
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"Reporte generado con pandas: {filepath}")
    return str(filepath)
