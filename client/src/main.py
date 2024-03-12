import socket
import argparse

def connect_to_server(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    return client_socket

def send_file(client_socket, file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read(1024)
        while file_data:
            client_socket.send(file_data)
            file_data = file.read(1024)
    print("Файл успешно отправлен")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Клиент для отправки файла по сети")
    parser.add_argument('-s', '--server', default='127.0.0.1', help='Адрес сервера')
    parser.add_argument('-p', '--port', default=12347, help='Порт сервера')
    args = parser.parse_args()

    client_socket = connect_to_server(args.server, args.port)
    file_path = input("Введите путь к файлу: ")
    send_file(client_socket, file_path)
    client_socket.close()
