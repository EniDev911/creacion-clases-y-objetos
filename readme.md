<a href="https://colab.research.google.com/gist/EniDev911/c40736b700359a3d3e23d25fa5651fc1/creacion-clases-y-objeto.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

### Requerimiento 1

Crear en un archivo llamado `te.py` una clase que permita instanciar objetos de tipo **Te**. Para ello, debe considerar un nombre adecuado para la clase, y el o los atributos de clase.

> **Recordar**: Un atributo de clase es aquel que se define a nivel de clase, y que todas las *instancias* tendrán el mismo valor.

Como sabemos los todos los té deben tener ciertos valores, en nuestra clase lo podemos declarar los siguientes **atributo estático**:


> **Ojo**: Ya que debe ser un atributo común en todas las instancias. Como buena practica este valor no debería ser modificado. Es por ello que en vez de almacenar los posibles valores en un diccionario o lista, lo hacemos en una tupla ya que se trata de una estructura inmutable.


```python
class Te:

	duracion = 365
	formato = (300, 500)
	sabor = ('Té negro', 'Té verde', 'Agua de hierba')
```

### Requerimiento 2

En el archivo `te.py` y en la clase del requerimiento anterior, agregue un **método estático** que retorne el tiempo de preparación y la recomendación correspondiente, según el sabor ingresado por parámetro. Debe retornar el tiempo y recomendación correspondiente, según la descripción del problema.

Considere el parámetro sabor como un número entero, con la siguientes 3 posibles valores:

- 1: Corresponde a **Té negro**
- 2: Corresponde a **Té verde**
- 3: Corresponde a **Agua de hierbas**


```python
class Te(Te):
  """
  Estamos recibiendo la clase de forma recursiva, celda por celda.
  para mantener los atributos y métodos de otras celdas.
  """
  @staticmethod
  def preparacion(sabor):

    return {
            sabor == 1: "Preraración en 3 minutos, consumir al desayuno",
            sabor == 2: "Preraración en 5 minutos, consumir al medio día",
            sabor == 3: "Preraración en 6 minutos, consumir al atardecer"
		}.get(True, "Valor no válido")

if __name__ == "__main__":
	te = Te()
	print(Te.preparacion(1))
```

    Preraración en 3 minutos, consumir al desayuno
    

### Requerimiento 3

En el archivo `te.py` y en la clase del primer requerimiento, agregue un **método estático** que **retorne el precio** según el **formato** ingresado (número entero).

- Debe retornar el precio adecuado según la descripción del problema:


```python
class Te(Te):

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

if __name__ == "__main__":
	print("Precio:","$", Te.obtener_precio(1))
```

    Precio: $ 3000
    

### Requerimiento 4

En un archivo llamado `instancias.py`, importe la clase del primer requerimiento.

A partir de esta clase:

- Cree dos instancias.
- Almacene el tipo de dato de cada instancia creada en una variable (**Tip**: use la función `type()`).
- Muestre por pantalla, usando `print()`, el valor de cada tipo de dato almacenado.
- En caso de que ambos tipos almacenados sean iguales, muestre por pantalla, usando `print()`, el mensaje "Ambos objetos son del mismo tipo". En caso contrario, mostrar mensaje "Los objetos no son del mismo tipo".


```python
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
```

    <class '__main__.Te'>
    <class '__main__.Te'>
    Ambos objetos son del mismo tipo
    

### Requerimiento 5

En un archivo llamado `pedido.py`, escriba un programa que al ser ejecutado permita al usuario ingresar los datos para generar un pedido de té. Para ello, el programa debe hacer lo siguiente:

- Pedir al usuario que ingrese el valor para cada atributo requerido para especificar su pedido.
- Los valores entregados por el usuario deben almacenarse en variables.
- Utilizar las variables anteriores en los métodos de la clase del requerimiento 1 (importarla en este script).
- Mostrar en pantalla, mediante la función `print()`, el detalle de toda la información del té ordenado, a partir de los valores ingresados por el usuario, y los obtenidos a partir de los métodos de la clase del requerimiento 1. Por lo tanto, debe mostrar en pantalla los valores de:
	- Sabor del tipo de té (como texto)
	- Formato (como número)
	- Precio (como número)
	- Recomendación (como texto)


```python
if __name__ == "__main__":
  sabor = int(input(
  """Hola, ingrese una opción para el tipo de té
  (1) Té negro
  (2) Té verde
  (3) Aguas de hierba
  > """))

  formato = int(input(
  """Hola, ingrese una opción para el formato del té
  (1) 300gr
  (2) 500gr
  > """))


  print("Detalles del pedido:")
  print("Sabor:", Te.sabor[sabor - 1])
  print("Formato:", Te.formato[formato - 1], "gr")
  print("Precio:", "$", Te.obtener_precio(formato))
  print("Recomendación:", Te.preparacion(sabor))
```

    Hola, ingrese una opción para el tipo de té
      (1) Té negro
      (2) Té verde
      (3) Aguas de hierba
      > 1
    Hola, ingrese una opción para el formato del té
      (1) 300gr
      (2) 500gr
      > 1
    Detalles del pedido:
    Sabor: Té negro
    Formato: 300 gr
    Precio: $ 3000
    Recomendación: Preraración en 3 minutos, consumir al desayuno
    
