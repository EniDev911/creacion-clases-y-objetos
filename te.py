class Te():
	
	sabor = ("Té negro","Té verde","Aguas de hierba")
	
	formato = ("300gr","500gr")

	duracion = 365
	
	@staticmethod
	def obtener_precio(formato):
		"""
		1 = 300gr
		2 = 500gr
		"""
		return {
			formato == 1: "$3.000", 
			formato == 2: "$5.000"
		}.get(True, "Formato no válido")
	
	@staticmethod
	def preparacion(sabor):
		"""
		1 = Té negro
		2 = Té verde
		3 = Agua de hierbas
		"""
		return {
			sabor == 1: "Preraración en 3 minutos, consumir al desayuno", 
			sabor == 2: "Preraración en 5 minutos, consumir al medio día", 
			sabor == 3: "Preraración en 6 minutos, consumir al atardecer"
		}.get(True, "Valor no válido")


if __name__ == "__main__":
	te = Te()
	print(Te.preparacion(1))
