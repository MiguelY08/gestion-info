from validate import validar_id, validar_nombre, validar_email, validar_producto

class ClienteService:
    def __init__(self):
        self.clientes = []  # Lista de diccionarios
        self.ids_usados = set()  # Set para IDs únicos
        self.emails_usados = set()  # Set para emails únicos
        self.duplicados = []  # Lista de duplicados encontrados
    
    def agregar_cliente(self, id_cliente, nombre, email, productos=None):
        """Agrega un cliente con validación de unicidad"""
        # Validar campos
        id_validado = validar_id(id_cliente)
        nombre_validado = validar_nombre(nombre)
        email_validado = validar_email(email)
        
        # Verificar unicidad
        if id_validado in self.ids_usados:
            duplicado = f"ID duplicado: {id_validado} (Cliente: {nombre_validado})"
            self.duplicados.append(duplicado)
            return None
        
        if email_validado in self.emails_usados:
            duplicado = f"Email duplicado: {email_validado} (Cliente: {nombre_validado})"
            self.duplicados.append(duplicado)
            return None
        
        # Validar productos
        productos_validados = []
        if productos:
            for prod in productos:
                validar_producto(prod)
                productos_validados.append(prod)
        
        # Crear cliente
        cliente = {
            'id': id_validado,
            'name': nombre_validado,
            'email': email_validado,
            'products': productos_validados
        }
        
        # Guardar
        self.clientes.append(cliente)
        self.ids_usados.add(id_validado)
        self.emails_usados.add(email_validado)
        
        return cliente
    
    def listar_clientes(self):
        """Retorna lista de clientes"""
        return self.clientes
    
    def obtener_total_cliente(self, id_cliente):
        """Calcula total de compras de un cliente"""
        for cliente in self.clientes:
            if cliente['id'] == id_cliente:
                total = sum(p['quantity'] * p['price'] for p in cliente['products'])
                return total
        return 0
    
    def obtener_duplicados(self):
        """Retorna lista de duplicados encontrados"""
        return self.duplicados