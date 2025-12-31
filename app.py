from docxtpl import DocxTemplate
import os

try:
    usr_input = input("Enter your range (EX- 0-100): ")
    usr_input = usr_input.strip()
    usr_input = usr_input.split("-")
    usr_input = [int(num) for num in usr_input]
except:
    print("Please use valid format")

doc = DocxTemplate(f"{os.getcwd()}\\src\\file.docx")
context = {
    "var": [num for num in range(usr_input[0], usr_input[1]) if num%2 != 0]
} 

doc.render(context)
doc.save("output.docx")