ano_atual= 2022

print ("################################")
print ("Seja bem vindo!!")
print ("################################")
ano_de_nascimento= input ("Que ano você nasceu? ")
ano_de_nascimento= int(ano_de_nascimento)

idade= ano_atual - ano_de_nascimento
#Se a idade for maior que 40 anos, diga "Nossa, como você está velho!"
if idade <18:
    print ("Menor de idade!") 

    if idade >18:
            print("Aproveita a juventude!!")

if idade > 40:
    print ("Nossa, como você é velho!")

    if idade >60:
        print("Mas nem tão velho assim!")

print ("Sua idade é: {} anos!".format(idade)) 


