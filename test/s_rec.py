import cv2
import numpy as np
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))

def receive():
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        nparr = np.fromstring(data, np.uint8)
        img = cv2.imencode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow("Client", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

receive()
cv2.destroyAllWindows()