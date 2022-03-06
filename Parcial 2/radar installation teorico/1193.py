# Juan Diego Balanta
##
# 24 de Octubre de 2020
##
# Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
# a seguir los más altos estándares de integridad académica.
# Inspiración y Guia
# Notas de clase, codigo de cubrimiento de intervalos
from sys import stdin
from math import *


def interval(Y, D):
	d = D * D - Y * Y
	if(d < 0): return -1
	return sqrt(d)


def solve(A):
    N = len(A)
    A.sort(key=lambda x: x[1])
    print("key = lambda x : x[1]", A)
    ans, n = 0, 0
    while(n != N):
        best, n = n, n + 1
        while(n != N and A[n][0] < A[best][1]):
            n = n + 1
        ans = ans + 1
    return ans


def main():
    line = stdin.readline().strip()
    case = 1
    while(line != '0 0'):
        N, D = [int(i) for i in line.split()]
        A, flag, n = [], True, 0
        line = stdin.readline().strip()
        while(n != N):
            x, y = [int(i) for i in line.split()]
            d = interval(y, D)
            flag = flag and d != -1
            A.append((x - d, x + d))
            n = n + 1
            line = stdin.readline().strip()
        line = stdin.readline().strip()
        print("A es original", A)
        ans = -1 if not flag else solve(A)
        print("Case {}: {}".format(case, ans))
        case += 1



main()
