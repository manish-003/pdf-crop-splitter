from pypdf import PdfWriter, PdfReader  

pdf = PdfReader('test.pdf')

writer = PdfWriter()
for page in pdf.pages:
    right = page.mediabox.right
    page.mediabox.upper_right = (
        page.mediabox.right / 2,
        page.mediabox.top,
    )
    writer.add_page(page)
    page.mediabox.upper_left = (
        right /2,
        page.mediabox.top
    )
    page.mediabox.upper_right = (
        right, page.mediabox.top
    )
    writer.add_page(page)

with open("output.pdf",'wb') as fp:
    writer.write(fp)