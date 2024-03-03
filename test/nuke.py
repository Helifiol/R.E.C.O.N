import os, stat, subprocess, platform

filename = "nuke.sh"

def destroy():
    os.chmod(filename, os.stat(filename).st_mode | stat.S_IEXEC)

    if "Darwin" in platform.system() or "Linux" in platform.system():
        os.system(f'./{filename}')
    else:
        print("Sorry no windows")