import socket
IP = "0.0.0.0"
PORT = 7772

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen()
    print("Listening..")
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(4096)
            print('Received', repr(data))
            print('Sending data')
            conn.send(data)
