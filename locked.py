from PyPDF2 import PdfFileReader , PdfFileWriter 
import getpass #prompts the user for a password without echoing

pw = PdfFileWriter()
pr = PdfFileReader("your_file.pdf")

for page_num in range(pr.numPages):
  pw.addPage(pr.getPage(page_num))

password = getpass.getpass(prompt='Please enter password for prompts your file : ')
pw.encrypt(password)

with open("file locked",'wb') as iteration: 
	pw.write(iteration)
	iteration.close()
