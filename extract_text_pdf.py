from pypdf import PdfReader

reader = PdfReader('Aloure_Flowers_Knowledge_Base.pdf')

full_text = ""

for page in reader.pages:
    full_text = full_text + page.extract_text() + "\n"

splited_lines = full_text.splitlines()
print(splited_lines)


