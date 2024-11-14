prod_options = [
    [1, 'Coca-Cola', 3.75, 2], 
    [2, 'Pepsi', 3.67, 5], 
    [3, 'Monster', 9.96, 1], 
    [4, 'Café', 1.25, 100], 
    [5, 'Redbull', 13.99, 2]
]

def val_prodchoice():
    while True:
        try:
            prod_choice = int(input(f'''
A máquina de bebida possui os seguintes produtos:
ID Produto Valor Estoque
1 Coca-cola, R$ 3,75, {prod_options[0][3]}
2 Pepsi, R$ 3,67, {prod_options[1][3]}
3 Monster, R$ 9,96, {prod_options[2][3]}
4 Café, R$ 1,25, {prod_options[3][3]}
5 Redbull, R$ 13,99, {prod_options[4][3]}
Escolha um produto: ''')) - 1
            if 0 <= prod_choice < len(prod_options):
                if prod_options[prod_choice][3] > 0:
                    return prod_choice
                else:
                    print("Produto fora de estoque.")
            else:
                print("ID de produto inválido.")
        except ValueError:
            print("Por favor, insira um número válido.")

def val_payment(prod_price):
    while True:
        try:
            payment = float(input("Insira uma quantidade de dinheiro: "))
            if payment >= prod_price:
                return payment
            else:
                print("O valor do pagamento deve ser igual ou superior ao valor do produto.")
        except ValueError:
            print("Por favor, insira um valor válido.")

def calc_change(valor):
    coins = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    troco = {}

    for coin in coins:
        if valor >= coin:
            quantidade_moedas = int(valor // coin)
            valor = round(valor - quantidade_moedas * coin, 2)
            troco[coin] = quantidade_moedas

    return {moeda: quantidade for moeda, quantidade in troco.items() if quantidade > 0}

def dedeuce_prod(prod_choice):
    prod_options[prod_choice][3] -= 1

def main():
    continuar = "1"
    while continuar == "1":
        prod_choice = val_prodchoice()
        prod_price = prod_options[prod_choice][2]
        
        payment = val_payment(prod_price)
        exchange = payment - prod_price
        
        if exchange > 0:
            troco = calc_change(exchange)
            print(f"\nTroco: {exchange}:")
            for moeda, quantidade in troco.items():
                print(f"{moeda} x {quantidade}")
        
        dedeuce_prod(prod_choice)
        print(f"\nVocê comprou {prod_options[prod_choice][1]}. Estoque restante: {prod_options[prod_choice][3]}")
        
        continuar = input('''\nDeseja comprar mais algum produto?
1 - Sim
2 - Não
Escolha: ''')
        if continuar != "1":
            print("Programa encerrado. Obrigado por utilizar. Produzido por @JoaoPicoli")

main()
