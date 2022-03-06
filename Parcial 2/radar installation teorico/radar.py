# Juan Diego Balanta
# id: 0220859
# 24 de Septiembre de 2020
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

def mic_wf(L, H, a):
    """
    Codigo de las notas de clase
    Cubrimiento de intervalos
    """
    a.sort()
    ans, low, n, ok, N = list(), L, 0, True, len(a)
    cnt = len(a)
    while ok and low < H and n != N:
        ok = a[n][0] <= low
        best, n = n, n+1
        while ok and n != N and a[n][0] <= low:
            if a[n][1] > a[best][1]:
                best = n
            n += 1
        ans.append(best)
        cnt -= 1
        low = a[best][1]
    ok = ok and low >= H
    if ok == False:
        ans = list()
    if ans == []:
        cnt = -1
    return cnt


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
    #A.sort(key=lambda x: x[1])
    print(A)
    ans = -1 if not flag else mic_wf(A[0][0], A[N-1][0], A)
    print("Case {}: {}".format(case, ans))
    case += 1

main()
