import numpy.random as random
from numpy import ceil
Fx = input('Insira a maior funcao (f(x)) ')
Gx = input('Insira a menor funcao (g(x)) ')
a = int(input('Insira o menor ponto x (a) '))
b = int(input('Insira o maior ponto x (b) '))
t = int(input('Insira o total de pontos a serem gerados '))

def Funcao(Fx,x):
    return eval(Fx)

maxy = max([Funcao(Fx,i) for i in range(a,b+1)])
miny = min([Funcao(Gx,i) for i in range(a,b+1)])

n =-0
for i in range(t):
    p = [random.uniform(a,b), random.uniform(miny,maxy)]
    if p[1] <= Funcao(Fx,p[0]) and p[1] >= Funcao(Gx,p[0]):
        n += 1
print ((n/t)*((b-a)*(maxy-miny)))

