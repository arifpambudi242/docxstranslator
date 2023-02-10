'''
author 	: Arif Pambudi
email	: arifpambudi242@gmail.com

'''
from docx import Document
from os import system as cmd
from pdf2docx import Converter
from docx2pdf import convert as convert_docx_to_pdf
import time
from python_translator import Translator
from autocorrect import Speller
import sys

trans = Translator()
spell = Speller(lang="en")

filepath = sys.argv[1] if len(sys.argv) >= 2 else input("Type Path of File : ")
targetlang = sys.argv[2] if len(sys.argv) >= 3 else 'id'
sourcelang = sys.argv[3] if len(sys.argv) >= 4 else 'en'
# get file extension
file_extension = filepath.split(".")[-1]
if (file_extension == "pdf"):
    conv = Converter(filepath)
    conv.convert(filepath.split(".")[0] + ".docx")
    conv.close()
    filepath = filepath.split(".")[0] + ".docx"

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
                translated = trans.translate(corrected, targetlang, sourcelang).new_text
                # set paragraph text
                if translated:
                    v.text = translated
        time.sleep(0.1)
        cmd("cls")  # change to cmd("cls") if your os is windows
    except:
        continue

filename = filepath.split(".docx", 1)[0]
try:
    docx_name = f"{filename}-{targetlang}-{time.strftime('%d.%m.%Y-%H.%M.%S')}.docx"
    document.save(docx_name)
    convert_docx_to_pdf(docx_name, f"{filename}-{targetlang}-{time.strftime('%d.%m.%Y-%H.%M.%S')}.pdf")
    print(f"{filename}-{targetlang}-{round(time.time())}.docx has been generated")
except Exception as e:
    raise e