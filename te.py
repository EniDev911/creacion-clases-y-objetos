class Te():

	duracion = 365
	sabor = ("Té negro","Té verde","Aguas de hierba")
	formato = (300 ,500)
	
	@staticmethod
	def obtener_precio(formato):
		"""
		1 = 300gr
		2 = 500gr
		"""
		return {
			formato == 1: 3000,
			formato == 2: 5000
		}.get(True, "Opción no válida")
	
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
	print(Te.obtener_precio(2))
	print(Te.preparacion(1))
