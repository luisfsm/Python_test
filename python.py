x = int(input("Digite um numero: "))
escolha="s"
while escolha=="s":
    print("par" if x % 2 ==0 else "impar")
    escolha = input("Deseja continuar ? s ou n ")
    x = int(input("Digite um numero: ")) if escolha=="s" else print("Fim Game")

