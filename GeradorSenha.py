import random
import string

#Inicialização das variáveis e conjuntos dos caracteres
conditionalWhile = ""
letras = string.ascii_letters
digitos = string.digits
caracteres_especiais = ["!","@","#","$","%","&","*","_","-",]
opcoes = [letras, digitos, caracteres_especiais]

while True:
  try:
    senha = ""
    valor_entrada = input("Quantos caracteres voce quer em sua senha?")

    #Validação de valor numérico
    if not valor_entrada.isdigit():
      print("Por favor digite um valor válido ")
      continue

    senha_caracteres = int(valor_entrada)
    #Limitador de caracteres minimos possiveis
    if senha_caracteres < 4:
      print("A senha deve conter pelo menos 4 caracteres")
      continue 

    #Logica simples de quantificação da senha e concatenação das strings aleatorias
    for c in range(0, senha_caracteres):
      escolha = random.choice(opcoes)
      escolha = random.choice(escolha)
      senha += escolha
      
    print(f"Sua senha é: {senha}")

    conditionalWhile = str(input("Digite S/s para gerar uma nova senha: "))
    if conditionalWhile.lower() != "s":
      break
  #Except de interrupção do teclado no caso do usuario interromper antes do encerramento comum
  except KeyboardInterrupt:
    print("Processo interrompido por usuário")
    break

print("Fim do processo")