import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',5090)) # here put server.py file ip and port.

print('[*] To Exit type "-c" or "--exit"')

while True:

    data = input("Enter message to send -->>")

    client_socket.send(data.encode())

    server_data = client_socket.recv(1024) 

    if(server_data.decode() == '-c' or server_data.decode() == '--exit'): 
        print('[-] Connection closed by remote host .....') 
        break
    if(data == '-c' or data == '--exit'): 
        client_socket.send(data.encode())
        break

    print('[+] Server send -------->>',server_data.decode())



client_socket.close()