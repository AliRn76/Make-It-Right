# Created By AliRn.ir

import os

for file in os.listdir("."):
    if file.endswith('.srt'):
        try:
            base = os.path.splitext(file)[0]
            os.rename(file, base + ".txt")
            newFileName = base + '.txt'


            with open(newFileName, 'r', encoding="utf-8") as output:
                data = output.read()
                print(data)

            # with open(newFileName, 'r', encoding="utf-8") as output:

            with open(newFileName, 'r', encoding="cp1256") as output:
                data = output.read()
                print(data)

            with open(newFileName, 'w', encoding="utf-8") as input:
                input.write(data)
            os.rename(newFileName, base + ".srt")

        except:
            print("error")


