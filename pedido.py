from te import Te

sabor = int(input(
"""Hola, ingrese una opción para el tipo de té
1. Té negro
2. Té verde
3. Aguas de hierba
> """)) - 1

formato = int(input(
"""Hola, ingrese una opción para el formato del té
1. 300gr
2. 500gr
> """)) -1


print("Detalles del pedido:")
print("Sabor:", Te.sabor[sabor])
print("Formato:", Te.formato[formato])
# print("Precio:", Te.obtener_precio(formato))