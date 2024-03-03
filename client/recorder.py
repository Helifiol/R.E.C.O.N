import pyaudio, wave, time

chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
sec = 3
filename = "output.wav"
flag = False

def start_rec():
    p = pyaudio.PyAudio()

    print("recording...")

    stream = p.open(format=sample_format, channels=channels, 
                    rate=fs, frames_per_buffer=chunk, input=True)

    frames = []

    # for i in range(0, int(fs / chunk * sec)):
    #     data = stream.read(chunk)
    #     frames.append(data)
    
    while True:
        data = stream.read(chunk)
        frames.append(data)
        if flag:
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Finished Recording")

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def stop_rec():
    global flag
    flag = True