# Función para calcular 
def bisection(f, a, b, tolerance):

    """ Evaluación de la función en el intervalo """
    if f(a) * f(b) > 0:
        return None
    else:
        """ Cálculo de punto medio """
        Xm = (a + b) / 2
        
        """ Ciclo de cálculo de punto medio"""
        while abs(f(Xm)) > tolerance and abs(b - a) > tolerance: 
            counter += 1
            if f(Xm) == 0:
                print(f"La raíz es exacta: {Xm}")   
                break
        
            if f(a) * f(Xm) < 0:
                b = Xm
                Xm = (a + b) / 2
            else:
                a = Xm
                Xm = (a + b) / 2
        return Xm

""" Función que será evaluada """
def f(x):
    return x**2 - 4 

""" Definimos el intervalo y su tolerancia """
a = 1
b = 3
tolerance = 0.1
counter = 0
 
""" Uso del método """ 
root = bisection(f, a, b, tolerance)

""" Distintas respuestas"""
if  root == None:
    print(f"El teorema no se cumple, por lo tanto la raíz no se encuentra en este intervalo.")
else:
    print(f"La raíz es {root}" + f" con {counter} iteraciones.")