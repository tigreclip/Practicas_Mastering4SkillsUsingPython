"""
NORMALMENTE NECESITAS IMPRIMIR UN MESAJE QUE IMPLICA UN VALOR:
    ·"Please enter a number from 1 to 5 (5 es elnúmero de opciones del menú)
    ·"Miguel age is 33 and salary is 1000 (Tenemos 3 variables: miguel, edad y 1000)

 String formatting tiene que ver con tener alguna plantilla/estructura que lo haga fácil
 Hay 3 caminos para eso:

    - MODULUS OPERATOR (%) antiguo, pero sigue en código viejo 
     > print("%d %s cost $%.2f" % (6, "bananas", 1.74)) 
     > 6 bananas cost $1.7

    - REPLACEMENTS FIELDS: ok, pero evítalo por exceso de código 
     > '{x}/{y}/{z}'.format(x='foo', y='bar', z='baz')
     > 'foo/bar/baz'

    - F-STRING: LA FORMA MODERNA DE FORMATEAR STRINGS #######
    name = "Eric"
    age = 74
    f"Hello, {name}. You are {age}."
    'Hello, Eric. You are 74.'

 """