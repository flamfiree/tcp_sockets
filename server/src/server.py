from datetime import datetime
import os
import socket
from threading import Thread

class TCPServer:
    def __init__(self, host, port, max_clients, max_file_size):
        self.host = host
        self.port = port
        self.max_clients = max_clients
        self.max_file_size = max_file_size
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.max_clients)
        print(f"Server started on {self.host}:{self.port}")
        self.running = True

    def handle_client(self, client_socket, address):
        print(f"Accepted connection from {address}")
        file_content = client_socket.recv(1024)

        if len(file_content) > self.max_file_size:
            client_socket.send("File size exceeds maximum allowed size!".encode())
            client_socket.close()
        else:
            os.makedirs("uploads", exist_ok=True)
            
            # Write the received file data to a file in the 'uploads' directory
            file_path = os.path.join("uploads", datetime.today().strftime('%Y-%m-%d') + ".txt")
            with open(file_path, "wb") as file:
                file.write(file_content)
            client_socket.send("File saved successfully".encode())
            client_socket.close()

    def start(self):
        threads = []
        while self.running:
            client_socket, address = self.server_socket.accept()
            client_handler = Thread(target=self.handle_client, args=(client_socket, address), daemon=True)
            client_handler.start()
            threads.append(client_handler)

        # Ожидание завершения всех дочерних потоков
        for thread in threads:
            thread.join()

