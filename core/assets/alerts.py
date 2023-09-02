from core.assets.colors import red,green,blue,yellow


# print error and exit
def ERROR(E):
    print(red(f"[-] {E}"))
    exit(1)

# print warning
def WARN(W):
    print(yellow(f"[!] {W}"))


# print message
def MSG(M):
    print(green(f"[+] {M}"))


# print info
def INFO(I):
    print(blue(f"[*] {I}"))
