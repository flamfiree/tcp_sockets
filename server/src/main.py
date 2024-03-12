import argparse
import signal
from server import TCPServer

def shutdown(server):
    print("Shutting down server...")
    server.stop()

def main():
    parser = argparse.ArgumentParser(description="Simple TCP Server")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host IP to bind")
    parser.add_argument("--port", type=int, default=12347, help="Port to listen on")
    parser.add_argument("--max_clients", type=int, default=5, help="Maximum number of clients")
    parser.add_argument("--max_file_size", type=int, default=1024 * 1024, help="Maximum file size in bytes")
    args = parser.parse_args()

    server = TCPServer(args.host, args.port, args.max_clients, args.max_file_size)
    signal.signal(signal.SIGTERM, lambda signum, frame: shutdown(server))

    print("Server started on {}:{}".format(args.host, args.port))
    try:
        server.start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt received, stopping server...")
        server.stop()

if __name__ == "__main__":
    main()
