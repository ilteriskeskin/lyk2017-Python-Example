import sys


def print2(*value, sep=" ",end="\n"):
    sonuncu = value[-1]
    for v in value:
        sys.stdout.write(v)
        if v != sonuncu:
            sys.stdout.write(sep)
    sys.stdout.write(end)

def input2(prompt=""):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    sonuc = sys.stdin.readline()
    return sonuc

isim = input2("İsminiz: ")
print2("İsim: " + isim)




