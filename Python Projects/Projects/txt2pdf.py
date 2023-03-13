# txt2pdf - simple text to pdf
# 0xskar

# import the os library - this library has commands that let us communicate with the operating system
import os
# import the PythonPDF2 library - this lets us interact with PDF files
import PyPDF2


# open the text file we want to convert to PDF - "r" mean read only
text_file = open('input.txt', 'r')

# create PDF the textfile will become
pdf_writer = PyPDF2.PdfFileWriter()

# read the text file line by line and add them to the PDF file
for line in text_file:
    pdf_writer.addPage(line)

# save the PDF file to the disk - wb meaning write binary - we can also add to a PDF with ab (append)
output_file = open('output.pdf', 'wb') 


