import random
my_action = input("pedra, papel ou tesoura?")
opponent_action = random.choice(["pedra", "papel", "tesoura"])
if my_action == opponent_action:
   print(f"É um empate. Vocês dois selecionaram {my_action}")
elif my_action == "pedra":
   if opponent_action =="tesoura":
       print("pedra quebra tesoura.. Eu ganhei!!")
   else:
       print("Oponente vence!! papel cobre pedra")
elif my_action == "papel":
    if opponent_action == "pedra":
       print("Eu ganhei!!! papel cobre pedra")
   else:
       print("Oponente vence!! tesoura corta papel")
elif my_action == "tesoura":
   if opponent_action == "papel":
       print("Eu ganhei!!! tesoura corta papel")
   else:
       print("Oponente ganhou.. pedra quebra tesoura"
