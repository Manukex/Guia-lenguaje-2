from math import log
 
C=float(raw_input('ingrese el capital inicial en euros: '))
Tasa = float(raw_input('ingrese la tasa de interes anual'))
if Tasa<=0:
    print 'no se puede realizar el calculo con la tasa menor o igual a 0'
else:
    if Tasa>0:
        anios=(log((C*(1+Tasa/100)))-log(C))/(log(1+Tasa)/100)
    Capital_final=(C*(1+Tasa/100)**anios)
if Capital_final !=0:
    print 'para obtener %4.3f por una inversion de %4.3f al %2.0f % anual' %(Capital_final, C, Tasa)
    print 'es necesario esperar %2.0f años' %(anios)
else:
    anios= 0