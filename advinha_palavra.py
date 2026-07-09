palavra_secreta = "perfume"
letras_acertadas = ""
numero_tentativa = 0
while True:
    letra_digitada = input("digite uma letra:")
    numero_tentativa += 1
    if len(letra_digitada) > 1:
        print("digite apenas uma letra")
        continue
   
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    for letra_secreta in palavra_secreta:
       if letra_secreta in letras_acertadas:
        print(letra_secreta)
       else:
        print("*")
        
    palavra_formada = ""  
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print("Palavra formada:",palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print("VOCE GANHOU!! PARABÉNS!")
        print(f"a palavra era {palavra_formada}")
        print(f"numero total de tentativas foi {numero_tentativa}")
        break
                    