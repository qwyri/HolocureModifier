import base64
def stringToBase64(s):
    sample = s.encode("utf-8")
    base64_bytes = base64.b64encode(sample)
    return base64_bytes.decode("latin-1")

import codecs
BLOCKSIZE = 1048576 # or some other, desired size in bytes
with codecs.open("demofile2.txt", "r", "latin-1") as sourceFile:
    with codecs.open("save.dat", "w", "utf-8") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            print(stringToBase64(contents))
            targetFile.write(stringToBase64(contents))