import base64


def stringToBase64(s):
    return base64.b64encode(s.encode('latin-1'))


def base64ToString(b):
    return base64.b64decode(b).decode('latin-1')


old = '''"shion", 0.0'''
new = '''"shion", 100000.0'''

with open(r"save_n.dat", "r") as f:
    ans = base64ToString(f.read()).replace(old, new)

    f = open("demofile2.txt", "w", encoding="latin-1")
    f.write(ans)
    f.close()

    fa = open("save.dat", "wb")
    fa.write(stringToBase64(ans))
    fa.close()
