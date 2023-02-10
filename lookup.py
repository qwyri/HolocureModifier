import base64
from re import sub
from configparser import ConfigParser


def stringToBase64(s):
    return base64.b64encode(s.encode('latin-1'))


def base64ToString(b):
    return base64.b64decode(b).decode('latin-1')


config = ConfigParser()

config.read(r'resources/all-max.ini')
config.read(r'resources/basic-source.ini')

print("Would you like to restart? Or continue a file modification")
print("[ 0 - make new save file | 1 - modify previous file ]")
choose = int(input(""))

if choose == 0:
    with open(r"save_copy.dat", "r") as f:
        ans = base64ToString(f.read())
        cans = ["", ans]
        val = [0, 1, 1]
        x = 0
        while x == 0:
            def c():
                min = int(input())
                match min:
                    case 1:
                        cans[val[0]] = sub('\"characters\".+] ]',
                                           (config.get('max-out-all', 'data')), cans[val[1]])
                    case 2:
                        cans[val[0]] = sub('\"holoCoins\": [^\s]+,',
                                           (config.get('coins', 'data')), cans[val[1]])
                    case 3:
                        x = input("")
                        y = int(input(""))
                        cans[val[0]] = sub(
                            f'\"{x}\": [^\s]+,', f'\"{x}\": {y}.0,', cans[val[1]])
                        print(f'Horray! "{x}" is now "{y}"')
                    case 4:
                        fa = open("save_n.dat", "wb")
                        fa.write(stringToBase64(cans[val[2]]))
                        fa.close()
                        exit()
            c()
            if val[0] == 0:
                val[0], val[1], val[2] = 1, 0, 0
            else:
                val[0], val[1], val[2] = 0, 1, 1
elif choose == 1:
    print("Write the name of the previous file you want to edit")
    fchoose = input("")
    # save_n.dat
    with open(f"{fchoose}", "r") as f:
        ans = base64ToString(f.read())
        cans = ["", ans]
        val = [0, 1, 1]
        x = 0
        while x == 0:
            def c():
                print(cans[val[2]])
                min = int(input())
                match min:
                    case 0:
                        print(cans[val[2]])
                    case 1:
                        cans[val[0]] = sub('\"characters\".+] ]',
                                           (config.get('max-out-all', 'data')), cans[val[1]])
                    case 2:
                        cans[val[0]] = sub('\"holoCoins\": [^\s]+,',
                                           (config.get('coins', 'data')), cans[val[1]])
                    case 3:
                        x = input("")
                        y = int(input(""))
                        cans[val[0]] = sub(
                            f'\"{x}\": [^\s]+,', f'\"{x}\": {y}.0,', cans[val[1]])
                        print(f'Horray! "{x}" is now "{y}"')
                    case 4:
                        fa = open("save_n.dat", "w+b")
                        fa.write(stringToBase64(cans[val[2]]))
                        fa.close()
                        exit()
            c()
            if val[0] == 0:
                val[0], val[1], val[2] = 1, 0, 0
            else:
                val[0], val[1], val[2] = 0, 1, 1
