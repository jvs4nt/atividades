import os
import sys

def clear():
    os.system("clear")

e = 1

nome = str(input("Digite seu nome: "))

clear()

print(f"Olá {nome}! Seja bem-vindo(a) ao sistema de instruções da SALESFORCE.")
print("")

while (e != 2):
    print("Escolha uma das opções para seguir: ")
    print("1 - Informações sobre nossos produtos")
    print("2 - Entre em contato conosco")
    print("3 - Visite nossas redes sociais")
    print("4 - Participar do programa de fidelidade")
    print("")

    op = int(input("Digite a opção desejada: "))

    match op:
        case 1:
            clear()
            print(f"Boa escolha {nome}! Sobre qual produto você deseja obter informações?")
            print("")
            print("1 - Vendas")
            print("2 - Atendimento ao Cliente")
            print("3 - Marketing")
            print("4 - Commerce")
            print("5 - Data Cloud")
            print("6 - Voltar para o início")
            print("")

            produto = int(input("Digite a opção desejada: "))

            match produto:
                case 1:
                    clear()
                    print(f"informações sobre as vendas")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 2:
                    clear()
                    print(f"realizar atendimento ao cliente")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 3:
                    clear()
                    print(f"informações o marketing")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 4:
                    clear()
                    print(f"informações sobre commerce")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 5:
                    clear()
                    print(f"informações sobre data cloud")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 6:
                    clear()

        case 2:
            clear()
            print(f"Ok {nome}. Por qual canal deseja entrar em contato?")
            print("")

            input("Pressione ENTER para continuar...")

            clear()
            print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()
        case 3:
            clear()
            print(f"Boa escolha {nome}! Segue abaixo nossas redes sociais:")
            print("Intagram: @salesforcebrasil")
            print("LinkedIn: SalesforceBrasil")
            print("")

            input("Pressione ENTER para continuar...")

            clear()
            print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()
        case 4:
            clear()
            print(f"Que bom que deseja participar do nosso programa de fidelidade {nome}! Mas antes vamos saber um pouco melhor sobre o programa...")
            print("")
            print("O programa de fidelidade da Salesforce, denominado \"Salesforce Loyalty Plus\",")
            print("oferece aos clientes uma experiência excepcional e recompensadora. Com base na premiada")
            print("plataforma Salesforce, ele permite que as empresas personalizem ofertas, melhorem o")
            print("atendimento ao cliente e incentivem a fidelização. Os participantes ganham pontos por")
            print("engajamento e compras, que podem ser resgatados por descontos, serviços premium e acesso a")
            print("recursos exclusivos. O \"Salesforce Loyalty Plus\" impulsiona a satisfação do cliente e o")
            print("crescimento dos negócios, estabelecendo uma conexão duradoura entre empresas e clientes.")
            print("Uma maneira eficaz de recompensar e manter a lealdade em um mundo digital.")
            print("")

            input("Pressione ENTER para continuar...")

            clear()
            print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()
