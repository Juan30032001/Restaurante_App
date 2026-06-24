class Cliente:
    def __init__(self, nombre: str, correo: str, telefono: str, es_miembro: bool):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.es_miembro = es_miembro

    def __str__(self):
        tipo = "Miembro" if self.es_miembro else "Cliente ocasional"
        return f"{self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono} | {tipo}"