## Write a program to manipulate pdf files using pyPDF.
# Program should be able to merge multiple pdf files into a single pdf.

#------Code------#
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
    
for pdf in files:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()