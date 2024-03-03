# R.E.C.O.N

## Software designed using python to add a basic keylogger, voice recorder and web cam recorder to a target system

The program connects using the python socket module to establish a connection between the target and the server, once the
client program is executed, the program waits until a connection from the main.py program is established. Once the connection is
established the server program can request the client to either start / stop its keylogging, voice recording and video recording programs, moreover
the program can also request the client program to send it the saved files for the three programs.

### Dependencies

    pip install tqdm

### Usage

Run the **main.py** file in the server computer and the **client.py** in the client computer

### using keylogger program

In the *enter command* prompt in the main file

    start keylogger - start keylogger program
    stop keylogger - stop keylogger program
    get keylog - download keylog results

### using voice record program

In the *enter command* prompt in the main file

    start vorec - start voice recorder
    stop vorec - stop voice recorder
    get vorce - download voice recording

### using video record program

in the *enter command* prompt in the main file

    start vidrec - start video recorder
    stop vidrec - stop video recorder
    get vidrec - download video recording

### exit program

    exit - exit program
    terminate - terminate connection between client and server
