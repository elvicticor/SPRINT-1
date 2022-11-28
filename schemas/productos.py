



def productoEntity( producto ) -> dict:
	return {
		"_id": str( producto["_id"] ),
		"nombre": producto["nombre"],
		"precio": producto["precio"]
	}

def productosEntity( productos ) -> dict:
	resultado = []
	for producto in productos:
		resultado.append( productoEntity(producto) )
	return resultado