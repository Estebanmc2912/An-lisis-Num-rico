#Problema Función Secante
#Esteban Moreno & Pablo Veintemilla

FuncionSecante= function (f,x0,x1,t,max)
{
  y0=f(x0)
  y1=f(x1)
  
  
  Ei = c() #vector
  Ej = c() #vector
  issues = c() #vector
  ite = c() #vector

  cat(formatC(c("1","x_1","x_2","Error estimado"), width = -15, format = "f", flag = " "),"\n")
  while(abs(x1-x0)>t&&i<=max)
  {

    i=1
    i=i+1
    pendiente = (y1-y0)/(x1-x0)
    if(pendiente==0) return(cero=NA,f.cero = NA, iter=k,issuest=NA)
    x2=x1-y1/pendiente
    y2=f(x2)
    x0 = x1;y0=y1
    x1=x2;y1=y2
    ite = c(ite, i)
    Error = abs(x1-x0)
    issues = c(issues, Error)
    cat(formatC( c(i,x1,x2,Error), digits = 8, width = -15, format = "f", flag = " "), "\n")

  }

  if(i>max)
  {
    cat("Numero maximo de iteraciones alcanzado")
    cat(i, "X1: ", x1, "X2: ", x2, "Error: ", abs(x1-x0))
  }
  cat("Numero de iteraciones: ",i, "X1: ", x1, "X2: ", x2, "Error: ", abs(x1-x0))
  plot(ite,issues, type = "l", xlab = "No. ite",ylab="Error")
 
  for(b in 1:i){

    if(b!=i){

      Ei[b]=issues[b]

      Ej[b]=issues[b+1]  

    }
  }

  plot(Ei,Ej, type = "l", xlab = "Error i",ylab="Error i+1")
  
}

f=function(x) x^2-612
plot(f,0,10)
FuncionSecante(f,20,24,1e-8,1000)
