import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',5090)) #Replace IP with your IP. Change the port if you want to use another port

server_socket.listen(10)

print('[*] To Exit type "-c" or "--exit"')
print( "[+] Listening for connections on localhost:5090....")

while True:

    connection , ipAddr = server_socket.accept()

    print("[+] Got a connection from ",format(ipAddr))

    while True:
    
        get_ClientData = connection.recv(1024)

        if(get_ClientData.decode() == '-c' or get_ClientData.decode() == '--exit'): 
            print('[-] Connection closed by Client.......')
            break

        print("[+] Client send -------->>",get_ClientData.decode())

        server_input = input('Enter message to send -->>')

        if( server_input == '-c' or server_input == '--exit' ) :
            connection.send(server_input.encode())
            break
        else:
            connection.send(server_input.encode())

    connection.close()
    
    print('[-] Connection closed..........')
    break

    

