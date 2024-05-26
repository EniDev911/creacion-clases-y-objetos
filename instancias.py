from te import Te

if __name__ == "__main__":
	t1 = Te()
	t2 = Te()
	tipo_t1 = type(t1)
	tipo_t2 = type(t2)
	print(tipo_t1)
	print(tipo_t2)

	if tipo_t1 == tipo_t2:
		print("Ambos objetos son del mismo tipo")
	else:
		print("Los objetos no son del mismo tipo")
