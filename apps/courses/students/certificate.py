import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime



class Certificate:
    def generate_certificate(input_pdf, output_pdf, name, x=320, y=268):
        pdf_doc = fitz.open(input_pdf)

        page = pdf_doc[0]

        font_size = 30
        color = ( 0, 0, 0)


        # insert student name
        page.insert_text((x,y), name, fontsize=font_size, color=color)
        pdf_doc.save(output_pdf)
        pdf_doc.close()




