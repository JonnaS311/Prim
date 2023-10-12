from ciudades_nodo import Ciudad

a= Ciudad("A", 0, 10)
b= Ciudad("B", 1, 10)
c= Ciudad("C", 2, 10)
d= Ciudad("D", 3, 10)
e= Ciudad("E", 4, 10)
f= Ciudad("F", 5, 10)
g= Ciudad("G", 6, 10)

lista_ciudades = [
                a,b,c,d,e,f,g
                ]

adyacentes = [
    #0 #1 #2 #3 #4 #5 #6
    [0, 7, 0, 5, 0, 0, 0], #0
    [7, 0, 8, 9, 7, 0, 0], #1
    [0, 8, 0, 0, 5, 0, 0], #2
    [5, 9, 0, 0, 15, 6, 0], #3
    [0, 7, 5, 15, 0, 8, 9], #4
    [0, 0, 0, 6, 8, 0, 11], #5
    [0, 0, 0, 0, 9, 11, 0], #6
]