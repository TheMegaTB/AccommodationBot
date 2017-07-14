import sys

from reportlab.pdfgen import canvas
from pdfrw import PdfReader, PageMerge
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl


def add_text(filepath, text):
    inch = 72

    fname = sys.argv[1:]
    page = PdfReader(filepath, decompress=False).pages[0]
    p = pagexobj(PageMerge().add(page).render())

    c = canvas.Canvas('outstuff.pdf')
    c.setPageSize([8.27 * inch, 11.69 * inch])  # Set page size (for portrait)
    c.doForm(makerl(c, p))
    c.drawString(100, 100, 'Hello, world!')
    c.showPage()
    c.save()
