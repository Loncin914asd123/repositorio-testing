biblioteca = {
    "001": {"titulo": "Cien años de soledad"},
    "002": {"titulo": "1984"},
    "003": {"titulo": "Don Quijote de la Mancha"},
    "004": {"titulo": "El Principito"}
}

def buscar_libro_por_id(id_buscado):
    return biblioteca.get(id_buscado)

libro = buscar_libro_por_id("001")
print(libro)