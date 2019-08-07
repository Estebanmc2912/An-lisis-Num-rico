#Problema Posición Falsa
#Esteban Moreno & Pablo Veintemilla



FuncionNewton = function (f,fp,x0,tol,maxiter){

  k=0

  Ei = c() #vector
  Ej = c() #vector
  issues = c() #vector
  ite = c() #vector

  cat(formatC(c("x0","x1","dx","Error estimado"), width = -15, format = "f", flag = " "),"\n")
  repeat{
    correcion = f(x0)/fp(x0)
    x1 = x0 - correcion
    dx = abs(x1-x0)
    x0 = x1
    issues[k+1]=abs(correcion)
    iteraciones[k+1]=k+1
    k = k+1
    cat(formatC( c(x0,x1,dx,correcion), digits = 7, width = -15, format = "f", flag = " "), "\n")
    if(dx<=tol || k >maxiter)
      break
    
  }
  for(b in 1:(k+1)){
    if(b!=k+1){
      Ei[b]=issues[b]
      Ej[b]=issues[b+1]
    }
  }
  if(k > maxiter){
    cat("Numero máximo de Iteraciones alcanzado.")
    cat("Iteraciones=", k, " X: ",x1," f(x):",f(x1)," Error Estimado: ", correcion)
  }
  else{
    cat("Iteraciones=", k, " X: ",x1," f(x):",f(x1)," Error Estimado: ", correcion)
    
  }
  plot(iteraciones,issues,type = "l", xlab = "N iteraciones", ylab= "Error")
  plot(Ei,Ej, type = "l", xlab= "Error i", ylab = "Error i+1")
  
}

f= function(x) exp(x)-pi*x
fp= function(x) exp(x)-pi
FuncionNewton(f,fp,1.6,1e-8,1000)
