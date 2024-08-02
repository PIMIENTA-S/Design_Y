import rpy2.robjects as r
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import IntVector
import os

os.environ['R_HOME'] = 'C:\\Program Files\\R\\R-4.3.3' 
# Importar el paquete stats de R
stats = importr('stats')

# Definir los parámetros para dbinom
x = 5       # número de éxitos
size = 10   # número de pruebas
prob = 0.5  # probabilidad de éxito en cada prueba

# Llamar a la función dbinom de R
result = stats.dbinom(x, size=size, prob=prob)
print(result)