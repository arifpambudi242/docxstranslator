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

class Pdf_Translator:
    def __init__(self):
        pass

    def translate(self, file_name, sourcelang='en', targetlang='id'):
        file_extension = file_name.split(".")[-1]
        if (file_extension == "pdf"):
            conv = Converter(file_name)
            conv.convert(file_name.split(".")[0] + ".docx")
            conv.close()
            file_name = file_name.split(".")[0] + ".docx"

        document = Document(file_name)

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

        file_name = file_name.split(".docx", 1)[0]
        try:
            docx_name = f"{file_name}-{targetlang}-{time.strftime('%d.%m.%Y-%H.%M.%S')}.docx"
            document.save(docx_name)
            pdf_file = f"{file_name}-{targetlang}-{time.strftime('%d.%m.%Y-%H.%M.%S')}.pdf"
            convert_docx_to_pdf(docx_name, pdf_file)
            return pdf_file
        except Exception as e:
            raise e


if __name__ == '__main__':
    trans = Pdf_Translator()

    pdf_result = trans.translate('Python Developer - Indonesia (1).pdf', targetlang='id')

    print(pdf_result)