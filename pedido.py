from te import Te

sabor = int(input(
"""Hola, ingrese una opción para el tipo de té
1. Té negro
2. Té verde
3. Aguas de hierba
> """))

formato = int(input(
"""Hola, ingrese una opción para el formato del té
1. 300gr
2. 500gr
> """))


print("Detalles del pedido:")
print("Sabor:", Te.sabor[sabor - 1])
print("Formato:", Te.formato[formato - 1], "gr")
print("Precio:", "$", Te.obtener_precio(formato))
print("Recomendación:", Te.preparacion(sabor))