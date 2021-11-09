import numpy as np

array_ID = np.array([1,2,3])
### array_2D = np.array([1,2,3], [2,3,4])
### Numero de dimensiones
### ndim =
# biomasa en unidades de absorbancia
ecoli_matraz = np.array([0.1, 0.15, 0.19, 0.5,
                         0.9, 1.4, 1.8, 2.1, 2.3])
print(ecoli_matraz.ndim)
print(ecoli_matraz.shape)
print(len(ecoli_matraz))

ecoli_m_b = np.array([0.1 , 0.15, 0.19, 0.5 , 0.9 , 1.4 , 1.8 , 2.1 , 2.3 ])
ecoli_matraz_gl = ecoli_m_b*(0.39)

ejercicio1 = np.array([[5,3],[11,7],[4,9],[2,6]])
costos = np.array([3.5,5,7,4.3])
costos2 = np.array([[3.5,3.5],[5,5],[7,7],[4.3,4.3]])
beneficios = costos2/ejercicio1
print(ejercicio1)
print(costos)
print(beneficios)
beneficios2 = costos / ejercicio1.T
print(beneficios2)

### Tipos de dato
### dtype (dice que tipo de dato se uso)
### lo_que_quieres_saber.dtype
### Con "numero"j podemos usar numeros complejos