'''
author 	: Arif Pambudi
email	: arifpambudi242@gmail.com

'''
from docx import Document
from os import system as cmd
from time import sleep
from googletrans import Translator
import sys

trans = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])


filepath        = sys.argv[1] if len(sys.argv) >= 2 else input("Masukan Path File : ")
targetlang 		= sys.argv[2] if len(sys.argv) >= 3 else "id"
document 		= Document(filepath)

paragraphs      = document.paragraphs
lenparagraphs   = len(paragraphs)

for ind, para in enumerate(paragraphs):
	percentase 	= round((ind + 1) / lenparagraphs * 100, 2)
	print(f"translatting.....{ind+1}/{lenparagraphs} - {percentase}%")

	if para.text:
		inline = para.runs
		for i, v in enumerate(inline):
			# translate
			translated = trans.translate(inline[i].text, dest=targetlang).text
			inline[i].text = translated
	sleep(0.1)
	cmd("clear")

filename = filepath.split(".docx", 1)[0]
document.save(f"{filename}-{targetlang}.docx")