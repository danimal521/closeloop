import streamlit as st
from qr import generate_qr_code
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PIL import Image
import io
import pandas as pd

class Person:
    def __init__(self, firstname, lastname, email, company, role):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.company = company
        self.role = role

    def __repr__(self):
        return f"Person(firstname={self.firstname}, lastname={self.lastname}, email={self.email}, company={self.company}, role={self.role})"

def load_people_from_csv():
    people = []    
    df = pd.read_csv("event.csv")
    for index, row in df.iterrows():
        person = Person(row['firstname'], row['lastname'], row['email'], row['company'], row['role'])
        people.append(person)

    return people

def create_pdf():
    people = load_people_from_csv()
   
    label_width = 3.375 * 72  # 3-3/8 inches in points
    label_height = 2.125 * 72  # 2-1/8 inches in points
    labels_per_row = 2
    labels_per_column = 4
    page_width, page_height = letter
    label_offsetx = .67 * 72
    label_offsety = .68 * 72
    
    label_nextcoloffsetx = 0.37 * 72
    label_nextrowoffsetx = 0.38 * 72

    # buffer = io.BytesIO()
    # c = canvas.Canvas(buffer, pagesize=letter)
    c = canvas.Canvas("out.pdf", pagesize=letter)
    i = 0
    x = 0
    y = 0
    print("-------")
    for person in people:
        image = ImageReader(generate_qr_code(person.email))
        
        
     
            
            
        
        # c.saveState()
        #c.translate(x + label_width / 2, y + label_height / 2)
        #c.rotate(90)
        #c.showPage()
        #c.rect(x, y, label_width, label_height)
        c.rect(label_offsetx + (x * label_width) + (x * label_nextcoloffsetx), page_height - label_height - label_offsety - (y * label_height) - (y * label_nextrowoffsetx), label_width, label_height)
        c.drawString(label_offsetx + (x * label_width) + (x * label_nextcoloffsetx), page_height - label_height - label_offsety - (y * label_height) - (y * label_nextrowoffsetx), person.firstname + " " + str(x) + " " + str(y))


        #c.rect(label_offsetx + (x * label_width), page_height - label_height - label_offsety - (y * label_height), label_width, label_height)
        
        #c.drawString(label_offsetx, page_height - label_height - label_offsety, person.firstname + " " + person.lastname)
        
        
        #c.rect(label_offsetx + label_nextcoloffsetx, page_height - label_height - label_offsety, label_width, label_height)
        
        
        


        #c.drawString(0, 0, str(x) + " " + str(y) + " " + str(page_height) + " " + str(page_width))

        # c.drawString(-label_height / 2, -label_width / 2, person.firstname + " " + person.lastname)
        # c.drawImage(image, -label_height / 2, -label_width / 2 + 100, width=50, height=50)
        
        
        
        #c.restoreState()
        #if (i + 1) % (labels_per_row * labels_per_column) == 0:
        
            #i=0

        print(str(x) + "," + str(y))           
        if i % 2 == 0:
            x = 1
        else:
            x = 0
            y = y + 1
        i = i + 1

        if y > 3:
            c.showPage()
            i = 0
            x = 0
            y = 0
    c.save()

    # pdf_data = buffer.getvalue()

    # buffer.close()
    # return pdf_data

# Streamlit app
st.title("Download Badge PDF")
pdf_data = create_pdf()

# st.download_button(
#     label="Download PDF",
#     data=pdf_data,
#     file_name="output.pdf",
#     mime="application/pdf"
# )

# buffer = io.BytesIO()
# c = canvas.Canvas(buffer)
# c.drawImage("qr2.png", x=10, y=10, width=50, height=50)
# c.save()
# pdf_data = buffer.getvalue()


# buffer.close()


# # Label dimensions and positions
# label_width = 3.375 * 72  # 3-3/8 inches in points
# label_height = 2.125 * 72  # 2-1/8 inches in points
# labels_per_row = 2
# labels_per_column = 4
# page_width, page_height = letter

# def create_labels(filename, labels, rotation_angle=90):
#     c = canvas.Canvas(filename, pagesize=letter)
#     for i, label in enumerate(labels):

#         img = Image.open(generate_qr_code("danimal"))
#         img.seek(0).save("qr3.png")
#         #img.save("qr2.png")

#         x = (i % labels_per_row) * label_width
#         y = page_height - ((i // labels_per_row + 1) * label_height)
#         c.saveState()
#         c.translate(x + label_width / 2, y + label_height / 2)
#         #c.rotate(rotation_angle)
#         #c.drawString(-label_height / 2 + 10, -label_width / 2 + 20, label)
#         #c.drawImage(img.seek(0), -label_height / 2, -label_width / 2, width=50, height=50)
#         c.drawImage(img.seek(0), 10, 10, 150,150)
#         c.restoreState()
#         if (i + 1) % (labels_per_row * labels_per_column) == 0:
#             c.showPage()

#     c.save()

# # Example labels
# labels = [f"Label {i+1}" for i in range(8)]
# create_labels("avery_61612_labels.pdf", labels, rotation_angle=90)

# print("PDF with Avery 61612 labels created successfully.")