# PyCrawler
A python based web crawler? I'm not sure. It's just getting started.

Tried python PDF library:
PDFKit - Not sure why but html2pdf doesnt work. Doesnt install. Path isnt detected. A mess in general.
PyFPDF - Can generate PDF file. After a lot of rumbling with UTF-8 encoding being nullified by latin-1. Finally found a few work arounds. like, working on UTF-8 encoded data instead of strings. But ultimately, styling options (escpecially ln attribute for cells) is a mess of something logic cant explain. Will probably use reportlab.
Yeah, reportlab is the stuff. But currently, it's too much information. Let's stick to the standard text file output for the time being.
