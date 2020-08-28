import sys, time
from random import randint

def countingSort(A,B):
    k =  max(A)
    C = [0]*(k+1)
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for j in reversed(range(len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

if __name__ == '__main__':
    A = []
    
    n = input("Digite o tamanho do vetor: ")
    if not(n.isdigit()):
        sys.exit("Erro: Entrada inválida.")
    for i in range(int(n)):
        x = input("Digite o valor na posição {} do vetor: ".format(i))
        if not(x.isdigit()):
            sys.exit("Erro: Entrada inválida.")
        A.append(int(x))

    print(countingSort(A,[0]*len(A)))