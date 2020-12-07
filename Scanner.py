import os
import sys

reader = open("saida.txt", "w")


def scan(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                scan(entry.path)
            else:
                reader.write(entry.path[len(initialscan):] + " " + str(os.stat(entry.path).st_size) + "Bytes" + "\n")


if __name__ == "__main__" and len(sys.argv) > 1:
    initialscan = sys.argv[1]
    scan(initialscan)
else:
    print("Missing path argument")
    
reader.close()