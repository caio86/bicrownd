idade_velha = 0
idade_nova = 9999
qtd_pessoas = 40

for x in range(1, qtd_pessoas + 1):
    idade = int(input(f"Qual a idade da {x}ª pessoa? "))

    if idade > idade_velha:
        idade_velha = idade
    if idade < idade_nova:
        idade_nova = idade

print(f"A pessoa mais velha possui {idade_velha} anos")
print(f"A pessoa mais nova possui {idade_nova} anos")

