import cv2 
import socket

cap = cv2.VideoCapture(0)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(10)

client_socket, client_address = server_socket.accept()
connection = client_socket.makefile('wb')

def send():
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        data = cv2.imencode('.jpg', frame)[1].tobytes()
        try:
            connection.write(data)
        except:
            break

send()
cap.release()
cv2.destroyAllWindows()