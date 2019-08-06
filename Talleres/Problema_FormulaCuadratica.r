 #Pablo Veintemilla & Esteban Moreno: 
 #SIMULACION CUADRATICA  ax2 + bx + c = 0. 
  options(digits=8)

  a=3
  b=9^12
  c=-3

  #Método suma
  
  x1=-(b+sqrt(b^2-4*a*c))/(2*a)
  
  #Fórmula racionalizada 
  
  x2=-(2*c)/(b+sqrt(b^2-4*a*c))
  
  
  cat("Solución \n")
  cat("Raíz 1: ",x1, " Raíz 2: ",x2,"\n")
