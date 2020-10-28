'''
author 	: Arif Pambudi
email	: arifpambudi242@gmail.com

'''
from docx import Document
from os import system as cmd
import time
from googletrans import Translator
import sys
from autocorrect import Speller

spell = Speller()

trans = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])


filepath        = sys.argv[1] if len(sys.argv) >= 2 else input("Type Path of File : ")
targetlang 		= sys.argv[2] if len(sys.argv) >= 3 else "id"
document 		= Document(filepath)

paragraphs      = document.paragraphs
lenparagraphs   = len(paragraphs)

for ind, para in enumerate(paragraphs):
	percentase 	= round((ind + 1) / lenparagraphs * 100, 2)
	print(f"translatting.....{ind+1}/{lenparagraphs} - {percentase}% - {round((lenparagraphs - (ind + 1))/2)} s left")

	if para.text:
		inline = para.runs
		for i, v in enumerate(inline):
			# splelling correction
			corrected = spell(v.text)
			# translating
			translated = trans.translate(corrected, dest=targetlang).text
			# set paragraph text
			v.text = translated
	time.sleep(0.0001)
	cmd("clear") # change to cmd("cls") if your os is windows 

filename = filepath.split(".docx", 1)[0]
document.save(f"{filename}-{targetlang}-{round(time.time())}.docx")