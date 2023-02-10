import base64
import re
from configparser import ConfigParser

def stringToBase64(s):
    return base64.b64encode(s.encode('latin-1'))


def base64ToString(b):
    return base64.b64decode(b).decode('latin-1')

config = ConfigParser()

config.read(r'resources/all-max.ini')


old = '''"fandom": 0.0'''
new = '''"fandom": 1.0'''

with open(r"save_copy.dat", "r") as f:
    ans = base64ToString(f.read()).replace(old, new)
    # print(re.sub('\"characters\".+] ]',(config.get('max-out-all', 'data')),ans))

    # f = open("demofile2.txt", "w", encoding="latin-1")
    # f.write(re.sub('\"characters\".+] ]',"TESTEST",ans))
    # f.close()

    fa = open("save_n.dat", "wb")
    fa.write(stringToBase64(re.sub('\"characters\".+] ]',(config.get('max-out-all', 'data')),ans)))
    fa.close()
