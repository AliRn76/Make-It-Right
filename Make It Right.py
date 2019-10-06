# Created By AliRn.ir

import os

for file in os.listdir("."):
    print("File Name is: " + file)
    if file.endswith('.srt'):
        base = os.path.splitext(file)[0]
        os.rename(file, base + ".txt")
        fileName = base + '.txt'

        try:
            print("file: " + file + " , fileName: " + fileName)

            with open(fileName, 'r', encoding="utf-8") as output2:
                print(fileName + " ro open kard")

                data2 = output2.read()

            # with open(fileName, 'w', encoding="utf-8") as input2:
            #     input2.write(data)

            os.rename(fileName, base + ".srt")

            if data2:
                print("toonest read kone")
                continue


            print("baad az continue")
            # os.rename(fileName, base + ".srt")
            # continue
        except:
            with open(fileName, 'r', encoding="cp1256") as output:
              data = output.read()
              # print(data)

            with open(fileName, 'w', encoding="utf-8") as input:
              input.write(data)

            # os.rename(fileName, base + ".srt")


        # for i in "ÓÇíÊäíÝíÊÞÏíããí˜äÏ":
        #     for
        #         print("i: " + i + " j: " + j)
        #         if i == j:



                # else:
                #     print("too if naraft")
            os.rename(fileName, base + ".srt")