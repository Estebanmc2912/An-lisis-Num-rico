#Problema Posición Falsa
#Esteban Moreno & Pablo Veintemilla


PosicionFalsa= function(f, x0, x1, max, t)
{
  f0 = f(x0)
  f1 = f(x1)

  Ei = c() #vector
  Ej = c() #vector
  issues = c() #vector
  ite = c() #vector

  i = 1
  last = x1
  cat(formatC(c("i","x_i","f(x)","Error est."), width = -15, format = "f", flag = " "),"\n")
  while(i <= max)
  {

    x2 =(x0*f1-x1*f0)/(f1-f0)
    f2 = f(x2)
    if(abs(f2)<= t)
    {
      break
    }
    ite = c(ite, i)
    Error = abs(x1 - x0)
    issues = c(issues, Error)
    if(sign(f2) == sign(f0))
    {
      x0 = x2
      last = x2
      f0 = f2
    }
    else
    {
      x1 = x2
      last = x2
      f1 = f2
    }
    cat(formatC( c(i,x2,f(x2),Error), digits = 8, width = -15, format = "f", flag = " "), "\n")
    i = i+1

  }
  cat("Cero de funcion: ", x2, " con error <=", abs(x2 - last), "Iteraciones: ", i)
  plot(ite,issues, type = "l", xlab = "No. Iteraciones",ylab="Error")
  #Errores Ei vs Ei+1
  for(b in 1:i){
    if(b!=i){
      Ei[b]=issues[b]
      Ej[b]=issues[b+1]  
    }
  }
  plot(Ei,Ej, type = "l", xlab = "Error i",ylab="Error i+1")
}
f = function(x) exp(x)-pi*x;
PosicionFalsa(f,0,1,1000,1e-6)
