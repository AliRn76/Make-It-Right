# Created By AliRn.ir

import os

for file in os.listdir("."):
    if file.endswith('.srt'):
        base = os.path.splitext(file)[0]
        os.rename(file, base + ".txt")
        fileName = base + '.txt'

        try:
            with open(fileName, 'r', encoding="utf-8") as output:
                data = output.read()

            os.rename(fileName, base + ".srt")

            if data:
                continue

        except:
            with open(fileName, 'r', encoding="cp1256") as output2:
                data2 = output2.read()

            with open(fileName, 'w', encoding="utf-8") as input1:
                input1.write(data2)

            os.rename(fileName, base + ".srt")
