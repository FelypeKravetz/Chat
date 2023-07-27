import socket
import threading
import codecs
import sys

clients = []


def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Cliente {address[0]}:{address[1]} diz: {codecs.decode(data, 'utf-8')}")
            broadcast(data)
        except UnicodeDecodeError:
            print("Erro de decodificação. Ignorando a mensagem.")
        except:
            break

    print(f"Cliente {address[0]}:{address[1]} desconectou.")
    clients.remove(client_socket)
    client_socket.close()


def broadcast(message):
    for client in clients:
        client.send(message)


def send_message_to_clients():
    while True:
        message = input("Servidor:")
        broadcast(message.encode('utf-8'))


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(codecs.decode(data, 'utf-8'))
        except UnicodeDecodeError:
            print("Erro de decodificação. Ignorando a mensagem.")
        except:
            break


def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(codecs.encode(message, 'utf-8'))
            if message == "/sair":
                break
        except:
            break


def start_server():
    global clients

    HOST = '0.0.0.0'  # Bind to all available interfaces
    PORT = int(input("Digite a porta do servidor: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
    except OSError:
        print(f"A porta {PORT} está em uso ou você não tem permissão para usá-la. Tente outra porta.")
        return

    server.listen(5)
    clients = []

    print(f"Servidor pronto para receber conexões na porta {PORT}.")

    send_thread = threading.Thread(target=send_message_to_clients)
    send_thread.start()

    try:
        while True:
            client_socket, client_address = server.accept()
            print(f"\nNova conexão de {client_address[0]}:{client_address[1]}")
            print("Pressione [ENTER] para continuar.")

            try:
                client_socket.send("Conexão estabelecida com sucesso!".encode('utf-8'))
            except socket.error as e:
                print(f"Não foi possível enviar a mensagem de sucesso para {client_address[0]}:{client_address[1]}")
                print(f"Erro de conexão: {e}")

            clients.append(client_socket)
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except KeyboardInterrupt:
        print("\nServidor encerrado.")


def connect_to_server():
    global clients

    SERVER_IP = input("Digite o endereço IP do servidor: ")
    SERVER_PORT = int(input("Digite a porta do servidor: "))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((SERVER_IP, SERVER_PORT))
        message = client.recv(1024)
        print(codecs.decode(message, 'utf-8'))
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique o endereço IP e a porta.")
        return
    except:
        print("Erro ao receber a mensagem de sucesso do servidor.")
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

    # Espera até que o cliente termine a digitação de /sair
    print("Digite '/sair' para sair.")
    send_thread.join()

    # Fecha a conexão com o servidor
    client.close()

    # Encerra a aplicação
    sys.exit()


def show_credits():
    print("Créditos:")
    print("Este programa foi criado por Felype Kravetz.")
    print("Data: 26/07/2023.")


def main():
    while True:
        print("\nMenu:")
        print("1. Iniciar o servidor")
        print("2. Conectar ao servidor")
        print("3. Créditos")
        print("4. Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Opção inválida. Digite apenas um número válido.")
            continue

        if opcao == 1:
            start_server()
        elif opcao == 2:
            connect_to_server()
        elif opcao == 3:
            show_credits()
        elif opcao == 4:
            print("Encerrando o programa.")
            sys.exit()
        else:
            print("Opção inválida. Escolha uma opção válida.")


if __name__ == "__main__":
    main()
