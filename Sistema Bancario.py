import os
from time import sleep

# Sistema Bancario #

os.system('cls' if os.name == 'nt' else 'clear')

BILLS = (200, 100, 50, 20, 10, 5, 2)

# registrado
registered = False
# nome
name = ""
# saldo
balance = 0
# depositos
deposits = 0
# total de depositos
deposits_total = 0
# saques
withdraws = 0
# total de saques
withdraws_total = 0
# saldo inicial
opening_balance = 0
# ganho no juros
earned = 0
# saldo minimo
min_bal = 0
# saldo maximo
max_bal = 0

# tela dos extrato
def display_stats():
  print(f"Nome: {name}")
  print(f"Saldo inicial: R${opening_balance:.2f}")
  print(f"Saldo total: R${balance}")
  print(f"Número de depositos: {deposits}")
  print(f"Total de depositos: R${deposits_total:.2f}")
  print(f"Número de saques: {withdraws}")
  print(f"Total de saques: R${withdraws_total:.2f}")
  print(f"Ganhos com juros: R${earned:.2f}")
  print(f"Saldo minimo: R${min_bal:.2f}")
  print(f"Saldo maximo: R${max_bal:.2f}")
  input("Aperte ENTER para continuar...")

# tela do emprestimo
def loan():
  amount = take_num_input("Digite qual valor do emprestimo: ")
  percentage = take_num_input("Digite a porcentagem: ") / 100
  installments = take_num_input("Escreva o número de parcelas: ")

  need_to_pay = amount + amount * percentage
  installment = round(need_to_pay / installments, 2)

  print("Valor a pagar: ", need_to_pay)
  print("Valor da parcela: ", installment)

# tela dos juros   
def savings():
  global balance, earned
  amount = take_num_input("Digite a porcentagem: ") / 100
  recieved = balance * amount
  balance = balance + recieved
  earned += recieved
  print("Novo saldo:", format_balance(balance))

# tela do saque
def withdraw():
  global balance, withdraws, withdraws_total
  #200 100 50 20 10 5 2
  bills = ""
  while True:
    amount = take_num_input("Digite o quanto deseja sacar: ")
    amount_copy = amount
    while amount > balance:
      print("Isso não pode ser sacado, tente novamente!")
      amount = take_num_input("Digite o quanto deseja sacar: ")
    for number in BILLS:
      if amount > 0:
        if amount >= number:
          rest = divmod(amount, number) # division(/) modulo(%) => (div_result, mod_result) [representa os calculos feitos]
          amount = rest[1]
          bills += f"Você receberá {rest[0]:.0f} cédulas de {number}\n"
      else:
        break
    if amount > 0:
      print("Isso não pode ser sacado, tente novamente!")
    elif amount == 0:
      print(bills)
      balance = balance - amount_copy
      withdraws_total += amount_copy
      withdraws += 1
      print("Novo saldo:", format_balance(balance))
      input('Precione ENTER para continuar')
      break
    else:
      print("ERRO!")
    
# tela do deposito
def deposit():
  global balance, deposits, deposits_total
  amount = take_num_input("Digite o quanto deseja depositar: ")
  balance += amount
  deposits_total += amount
  deposits += 1
  print("Novo saldo:", format_balance(balance))
  
def format_balance(number):
  return f"{number:.2f}"
  
def take_num_input(text=''):
  amount = input(text)
  amount = amount.replace(",", ".")

  while True:
    if amount.replace(".", "").isdigit():
      number = float(amount)
      if number > 0:
        return number
      else:
        print("Número errado!")
    else:
      print("Número errado!")

    amount = input(text)

# checar o valor maximo e minimo
def check_min_max():
  global min_bal, max_bal
  if balance > max_bal:
    max_bal = balance
  elif balance < min_bal:
    min_bal = balance

# tela 2 de registrado
def window2():
  print("1. Realizar Depósito\n2. Realizar Saque\n3. Aplicar juros\n4. Simular empréstimo\n5. Extrato\n6. Sair")
  response = input("Selecione uma opção: ")
  os.system('cls' if os.name == 'nt' else 'clear')
  print(f"Opção escolhida: {response}\n")
  if response == "1":
    deposit()
  elif response == "2":
    withdraw()
  elif response == "3":
    savings()
  elif response == "4":
    loan()
  elif response == "5":
    display_stats()
  elif response == "6":
    exit()
  else:
    print("Opção não existente!")
  check_min_max()
  sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')

# tela 1 pra quem nao é registrado
def window1():
  global registered, name, balance, opening_balance, min_bal, max_bal

  print("1. Abrir conta\n2. Sair")
  response = input("Selecione uma opção: ")
  os.system('cls' if os.name == 'nt' else 'clear')
  print(f"Opção escolhida: {response}\n")
  if response == "1":
    name = input("Digite seu nome e sobrenome: ")
    min_bal = max_bal = balance = take_num_input("Digite seu saldo inicial: ")
    opening_balance = balance
    registered = True
  elif response == "2":
    exit()
  else:
    print("Opção não existente!")
    input('Precione ENTER para continuar')
  os.system('cls' if os.name == 'nt' else 'clear')

# main
def main():
  while True:
    if not registered:
      window1()
    else:
      window2()

if __name__ == "__main__":
  main()