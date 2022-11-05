import random
from claseGrafoSecuencial import GrafoSecuencial
from claseGrafoEnlazado import GrafoEnlazado

if __name__ == '__main__':
    #obj = GrafoEnlazado(5)
    #obj.crearArista(1, 2)
    obj = GrafoSecuencial(5)
    obj.crearArista(1, 2)
    obj.crearArista(1, 4)
    obj.crearArista(2, 3)
    obj.crearArista(2, 5)
    obj.crearArista(4, 5)
    #print(obj.mostrarMatriz())
    '''for i in range(20):
        x = random.randint(1,obj.getCantidadVertices())
        y = random.randint(1,obj.getCantidadVertices())
        obj.crearArista(x,y)'''
    if obj.Conexo():
        print('Grafo conexo')
    else:
        print('Grafo no conexo')
    