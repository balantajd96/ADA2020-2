inf = float('-inf')


def lis(A):
    N, lis, ans = len(A), 0, False
    if N != 0:
        tab = [1 for _ in range(N)]
        for n in range(1, N):
            for i in range(n):
                if tab[i] >= tab[n] and A[i] <= A[n]:
                    tab[n] = tab[i]+1
            ans = max(ans, tab[n])
            # lis = max(ans, tab[n])
            # if lis==k:
            #         ans= True
            #         return ans
    return ans


def lis2(A):
    N, ans = len(A), 0
    tab = [1 for _ in range(N)]
    for n in range(0, N):
        for i in range(n):
            if tab[i] >= tab[n] and A[i] <= A[n]:
                tab[n] = tab[i]+1
        ans = max(ans, tab[n])

    return ans


b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

A = [6, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
#A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def lisReintento(i, j):
    global A
    ans = False
    if j > len(A)-1:
        return 0
    elif A[i] > A[j]:
        return lisReintento(i, j+1)
    else:
        salto = lisReintento(i, j+1)
        tomo = lisReintento(j, j+1)+1
        tem = max(salto, tomo)
        return tem

def LISR(Arreglo, k):
    Arreglo.insert(0, inf)
    tamanioLis = lisReintento(0, 1)
    if tamanioLis >= k:
        return True
    else:
        return False
print("REINTENTO: ", LISR(A, 2), "----------")
#print("lisReintento", lisReintento(0,1))
# print(len(b))
# print("La solución de lis es:", lis(b))
# print("La solución de lis2 es:", lis2(b))


# si me quedan elementos y ya acabe de recorrer la secuencia:
# retornar false

# si recorro la secuencia y llego a k
# retorno True
# de lo contrario: elijo entre dos lados y retorno
# lo lleno or no lo llevo


def solve(A, n, i, j, k):
    # pre and memo are lists
    # 0 <= n <= len(A)
    if n == len(A):
        if j > len(A) or n == k:
            # retorna 0
            return True
        else:
            if A[i] > A[j]:
                return solve(A, n, i, j+1, k)
            elif A[i] == A[j]:
                solve(A, n+1, i, j+1, k)
    else:
        if i == 0 or A[i] <= A[j]:
            max = (solve(A, n+1, i, j+1, k), solve(A, n, j, j+1, k))




def solve2(A, n, pre, k):
    ans = None
    if n == len(A):
        ans = [list(pre)]
    else:
        ans0 = None
        ans = solve2(A, n+1, pre, k)
        if len(pre) == 0 or pre[-1] <= A[n]:
            pre.append(A[n])
            ans0 = solve2(A, n+1, pre, k)
            pre.pop()
            if len(ans0[-1]) == len(ans[-1]):
                ans.extend(ans0)
            elif len(ans0[-1]) > len(ans[-1]):
                ans = ans0
    return ans

def solve123(A, n, pre, memo):
  # pre and memo are lists
  # 0 <= n <= len(A)
  if n==len(A):
    if len(memo)==0:
      memo.append(list(pre))
    else:
      if len(memo[-1])<len(pre):
        memo.clear() ; memo.append(list(pre))
      elif len(memo[-1])==len(pre):
        memo.append(list(pre))
  else:
    if len(pre)==0 or pre[-1]<=A[n]:
      pre.append(A[n]) ; solve(A, n+1, pre, memo) ; pre.pop()
    solve(A, n+1, pre, memo)


A = [6, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
#print(solve123(A, 0, [], 3))
