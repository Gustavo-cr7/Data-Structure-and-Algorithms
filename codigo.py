ROXO = "\033[95m"
AZUL = "\033[94m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

historico = []

def inserir_dados():
    temperatura = float(input("Temperatura da nave: "))
    energia = float(input("Nível de energia (%): "))
    comunicacao = int(input("Comunicação (1 = ativa / 0 = falha): "))

    leitura = {
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao
    }

    historico.append(leitura)
    print(f"{VERDE}Dados cadastrados com sucesso.{RESET}")

def visualizar_status():
    if len(historico) == 0:
        print(f"{VERMELHO}Nenhum dado cadastrado.{RESET}")
    else:
        ultimo = historico[-1]

        print(f"\n{ROXO}STATUS ATUAL DA MISSÃO{RESET}")
        print("Temperatura:", ultimo["temperatura"], "°C")
        print("Energia:", ultimo["energia"], "%")

        if ultimo["comunicacao"] == 1:
            print("Comunicação: ativa")
        else:
            print("Comunicação: falha")

def executar_analise():
    if len(historico) == 0:
        print(f"{VERMELHO}Nenhum dado para analisar.{RESET}")
    else:
        ultimo = historico[-1]

        print(f"\n{ROXO}ANÁLISE OPERACIONAL{RESET}")

        if ultimo["temperatura"] > 80:
            print(f"{VERMELHO}Alerta de superaquecimento{RESET}")

        elif ultimo["energia"] < 20:
            print(f"{VERMELHO}Economia de energia{RESET}")

        elif ultimo["comunicacao"] == 0:
            print(f"{VERMELHO}Falha de comunicação{RESET}")

        else:
            print(f"{VERDE}Missão em estado normal{RESET}")

def mostrar_historico():
    if len(historico) == 0:
        print(f"{VERMELHO}Histórico vazio.{RESET}")

    else:
        print(f"\n{ROXO}HISTÓRICO DAS LEITURAS{RESET}")

        for i, dado in enumerate(historico):
            print(f"\nLeitura {i + 1}")
            print("Temperatura:", dado["temperatura"], "°C")
            print("Energia:", dado["energia"], "%")

            if dado["comunicacao"] == 1:
                print("Comunicação: ativa")
            else:
                print("Comunicação: falha")

def menu():
    while True:

        print(f"\n{ROXO}")
        print("╔══════════════════════════════════════╗")
        print("║      MONITORAMENTO ESPACIAL IA      ║")
        print("╚══════════════════════════════════════╝")
        print(RESET)

        print(f"{AZUL}1{RESET} - Inserir dados")
        print(f"{AZUL}2{RESET} - Visualizar status")
        print(f"{AZUL}3{RESET} - Executar análise")
        print(f"{AZUL}4{RESET} - Histórico das leituras")
        print(f"{AZUL}5{RESET} - Encerrar sistema")

        opcao = input(f"\n{ROXO}Escolha uma opção:{RESET} ")

        if opcao == "1":
            inserir_dados()

        elif opcao == "2":
            visualizar_status()

        elif opcao == "3":
            executar_analise()

        elif opcao == "4":
            mostrar_historico()

        elif opcao == "5":
            print(f"\n{VERDE}Sistema encerrado.{RESET}")
            break

        else:
            print(f"\n{VERMELHO}Opção inválida.{RESET}")

menu()