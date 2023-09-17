"""
Descrição:

Escreva um programa que leia o nome de uma pessoa e exiba a mensagem “Olá, FULANO” (onde FULANO é o nome da pessoa lida da entrada padrão).

- Formato de entrada

O nome de uma pessoa.

- Formato de saída

Um cumprimento à pessoa no seguinte formato:

Olá, Fulano!

Onde "Fulano" é o nome informado na entrada.

Exemplos de:

Entrada : Henrique

Saída:Olah, Henrique! 
"""

nome = str(input())

print("Olah, {}!".format(nome))