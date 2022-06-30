from camelcase import CamelCase

camelcase = CamelCase()
parrafo = "hola amigos veamos si esta librería funciona"

resultado = camelcase.hump(parrafo)
print(resultado)
