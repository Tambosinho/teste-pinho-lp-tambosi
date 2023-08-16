import numpy.random as npr
import numpy as np

def q4():
    array5 = npr.randint(0, 20, 10)
    array6 = npr.randint(0, 20, 10)
    
    elementos_em_comum = np.intersect1d(array5, array6)

    indices_array5 = np.where(np.isin(array5, elementos_em_comum))[0]
    indices_array6 = np.where(np.isin(array6, elementos_em_comum))[0]

    array5_n_array6 = np.setdiff1d(array5, array6)

    print("Array 1:", array5)
    print("Array 2:", array6)
    print("Elementos em comum:", elementos_em_comum)
    print("Índices dos elementos em comum no Array 5:", indices_array5)
    print("Índices dos elementos em comum no Array 6:", indices_array6)
    print("Elementos exlusivos do array 5:", array5_n_array6)

    return (array5,array6)

def q5():
    empilhamento5_6 = np.hstack(q4())
    print(empilhamento5_6)
    print("Média Empilhamento:", np.mean(empilhamento5_6))
    print("Desvio Padrão Empilhamento:", np.std(empilhamento5_6))
    print("Variância Empilhamento:", np.var(empilhamento5_6))

    for i in range(len(empilhamento5_6)):
        if(empilhamento5_6[i] % 2 ==0):
            empilhamento5_6[i] = 1
        else:
            empilhamento5_6[i] = -1
    
    print("Resultado transformação:", empilhamento5_6)






