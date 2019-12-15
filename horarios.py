
from constraint import *
import time

problem = Problem()

inicioTiempo = time.time()

problem.addVariables(['N1','N2','L1','L2','I1','I2','E1'],[1,2,3,4,5,6,7,8,9,10,11])
problem.addVariables(['M1','M2'],[1,4,7,10])
problem.addVariables(['S1','S2'],[3,6,9,11])
problem.addVariables(['Lucia1','Lucia2','Andrea1','Andrea2','Juan1','Juan2'],['N','S','L','W','I','E'])


problem.addConstraint(AllDifferentConstraint(),['N1','N2','L1','L2','I1','I2','E1','M1','M2','S1','S2'])
problem.addConstraint(AllDifferentConstraint(),['Lucia1','Lucia2','Andrea1','Andrea2','Juan1','Juan2'])


# A continuacion se anyaden las restricciones del problema mediante la funcion addConstraint proporcionada por la libreria

def consecutiveNaturales(a,b):
	if a>=1 and a<=2 and b>=1 and b<=2:
		return True
	if a>=2 and a<=3 and b>=2 and b<=3:
		return True
	if a>=4 and a<=5 and b>=4 and b<=5:
		return True
	if a>=5 and a<=6 and b>=5 and b<=6:
		return True
	if a>=7 and a<=8 and b>=7 and b<=8:
		return True
	if a>=8 and a<=9 and b>=8 and b<=9:
		return True
	if a>=10 and a<=11 and b>=10 and b<=11:
		return True

problem.addConstraint(consecutiveNaturales,('N1','N2'))



def distintoDia(a,b):
	if a>=1 and a<=3 and b>3:
		return True
	if a>=4 and a<=6 and(b<=3 or b>=7):
		return True
	if a>=7 and a<=9 and(b<=6 or b>=10):
		return True
	if a>=10 and b<=9:
		return True

problem.addConstraint(distintoDia,('M1','N1'))
problem.addConstraint(distintoDia,('M1','N2'))
problem.addConstraint(distintoDia,('M1','I1'))
problem.addConstraint(distintoDia,('M1','I2'))

problem.addConstraint(distintoDia,('M2','N1'))
problem.addConstraint(distintoDia,('M2','N2'))
problem.addConstraint(distintoDia,('M2','I1'))
problem.addConstraint(distintoDia,('M2','I2'))


#Asi evitamos soluciones repetidas que solo cambian en el orden de M1 y M2
def ordenarAsignaturas(a, b):
	if a < b:
		return True

problem.addConstraint(ordenarAsignaturas, ('M1', 'M2'))
problem.addConstraint(ordenarAsignaturas, ('N1', 'N2'))
problem.addConstraint(ordenarAsignaturas, ('L1', 'L2'))
problem.addConstraint(ordenarAsignaturas, ('S1', 'S2'))
problem.addConstraint(ordenarAsignaturas, ('I1', 'I2'))

#LOS PROFES

def luciaS_andreaE(l1,l2,a1,a2):
	if (l1 == 'S' or l2 == 'S') and (a1 != 'E' and a2 != 'E'):
		return False
	else:
		return True

problem.addConstraint(luciaS_andreaE,('Lucia1','Lucia2','Andrea1','Andrea2'))


# a = juan1, b = juan2, c = N1  y d = N2
def madrugarNaturales(a,b,c,d):
	if (a=='N' or b=='N') and ((c==1 or c==10) or (d==1 or d==10)):
		return False
	else:
		return True

problem.addConstraint(madrugarNaturales,('Juan1','Juan2','N1','N2'))

# a = juan1, b = juan2, c = S1  y d = S2
def madrugarSociales(a,b,c,d):
	if (a=='S' or b=='S') and ((c==1 or c==10) or (d==1 or d==10)):
		return False
	else:
		return True

problem.addConstraint(madrugarSociales,('Juan1','Juan2','S1','S2'))



# Una vez modelado el problema, podemos recuperar una de las soluciones:

print(problem.getSolution())

# o todas las soluciones:

print(problem.getSolutions())

tiempoFinal = time.time()
tiempoTranscurrido = tiempoFinal - inicioTiempo
print "\n\nTomo %d segundos." % (tiempoTranscurrido)
