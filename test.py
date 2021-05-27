

import os


def openFile():
    with open('test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()


if __name__ == "__main__":

    openFile()

