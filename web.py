from googlesearch import search
import wikipedia as wk
#import pdfkit
from fpdf import FPDF

'''
#PDF options
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}
'''



print("-------------------------------------------------------WEBSPIDER V0.1-----------------------------------------------------------")

#Input acquisition and preprocessing
query=input()
out=[]
content=""

pdf=FPDF("P",'mm','A4')
pdf.add_page()
pdf.set_font("Helvetica", 16)


#Wiki report
wk_result = wk.search(query)


print(wk_result)


for i in range(min(2,len(wk_result))):
	page=wk.page(wk_result[i])
	out.append(page.content)

#final output

for i in out:
	content+=i+"\n"

#pdfkit.from_string(content,query+" Results.pdf", options=options)
pdf.cell(40,10, content)
pdf.output(query+" Results.pdf", 'F')
