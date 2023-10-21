n = int(input("Digite um número para ser verificado: "))

def primo(num):
    for i in range(2,num):
        if(num%i == 0):
            return False
    return True
if(primo(n)):
    print(n, "é primo")
else: print(n, "não é primo")