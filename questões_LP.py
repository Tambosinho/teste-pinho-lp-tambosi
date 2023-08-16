import numpy.random as npr
import numpy as np

<<<<<<< HEAD:questoes_LP.py

=======
>>>>>>> 7eedce28ac0ffc02b0e7e9aae39da52698cb0b20:questões_LP.py
def q1():
    array1 = np.array([1, 2, 3, 4, 5, 6, 1, 2 , 3])
    array2 = np.array([7, 8, 9, 10, 11, 12, 1, 2, 3])
    array3 = array1 + array2
    return array3


def q2():
    array3_2D = q1().reshape(3, 3)
    array3_float = array3_2D.astype(float)
    transposta = array3_float.transpose()
    return transposta


def q3():
    array4 = np.array([[2, 4, 1], [6, 8, 1], [4,5,1]])
    array4 = array4 * q2()
    return array4

def q4():
    array5 = npr.randint(0, 20, 10)
    array6 = npr.randint(0, 20, 10)
    
    elementos_em_comum = np.intersect1d(array5, array6)

    indices_array5 = np.where(np.isin(array5, elementos_em_comum))[0]
    indices_array6 = np.where(np.isin(array6, elementos_em_comum))[0]

    array5_n_array6 = np.setdiff1d(array5, array6)

    print("Elementos em comum:", elementos_em_comum)
    print("Índices dos elementos em comum no Array 5:", indices_array5)
    print("Índices dos elementos em comum no Array 6:", indices_array6)
    print("Elementos exlusivos do array 5:", array5_n_array6)

    return (array5,array6)

def q5(arrays):
    empilhamento5_6 = np.hstack(arrays)
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






