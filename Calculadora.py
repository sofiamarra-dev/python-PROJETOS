while True:
   try:
    num1 = input(float("informe um numero:"))
    num2 = input(float("informe outro numero:"))
   except ValueError:
       print("Um dos valores ou amboas estao incorretos")
       
   operacao = input("informe o modulo de operacao +-/*:")
  
   if operacao not in "+-/*":
        print("informe um modulo de operacao correto +-/*")
        continue
    
   if operacao == "+":
           resultado = num1+num2   
   elif operacao == "-":
           resultaodo = num1-num2
   elif operacao == "/":
           resultado = num1/num2
   elif operacao == "*":
            resultado = num1*num2
   else:
        print("informe um valor correto ")
        
   print("Calculando....")
   print(f"Resultado:{num1}{operacao}{num2}= {resultado}")
   
   sair = input("Quer sair?[s]im".lower().startswith("s"))
   
   if  sair:
       break
   