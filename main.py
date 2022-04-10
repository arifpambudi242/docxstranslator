'''
author 	: Arif Pambudi
email	: arifpambudi242@gmail.com

'''
'''
author 	: Arif Pambudi
email	: arifpambudi242@gmail.com

'''
from docx import Document
from os import system as cmd
import time
from googletrans import Translator
from autocorrect import Speller
import sys


trans = Translator()
spell = Speller(lang="en")

filepath = sys.argv[1] if len(sys.argv) >= 2 else input("Type Path of File : ")
targetlang = sys.argv[2] if len(sys.argv) >= 3 else "id"

document = Document(filepath)

paragraphs = document.paragraphs
lenparagraphs = len(paragraphs)

for ind, para in enumerate(paragraphs):
    try:
        percentage = round((ind + 1) / lenparagraphs * 100, 2)
        print(f"translatting..... {percentage}% - {round((lenparagraphs - (ind + 1))/4)} s left")

        if para.text:
            inline = para.runs
            for i, v in enumerate(inline):
                corrected = spell.autocorrect_sentence(v.text)
                # translating
                translated = trans.translate(corrected, dest=targetlang).text
                # set paragraph text
                if translated:
                    v.text = translated
        time.sleep(0.1)
        cmd("cls")  # change to cmd("cls") if your os is windows
    except:
        continue

filename = filepath.split(".docx", 1)[0]
document.save(f"{filename}-{targetlang}-{round(time.time())}.docx")
print(f"{filename}-{targetlang}-{round(time.time())}.docx has been generated")