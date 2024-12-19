import streamlit as st
from qr import generate_qr_code
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

st.title("badge page")
st.write("badge page!")



# Label dimensions and positions
label_width = 3.375 * 72  # 3-3/8 inches in points
label_height = 2.125 * 72  # 2-1/8 inches in points
labels_per_row = 2
labels_per_column = 4
page_width, page_height = letter

def create_labels(filename, labels, rotation_angle=90):
    c = canvas.Canvas(filename, pagesize=letter)
    for i, label in enumerate(labels):

        img = Image.open(generate_qr_code("danimal"))

        x = (i % labels_per_row) * label_width
        y = page_height - ((i // labels_per_row + 1) * label_height)
        c.saveState()
        c.translate(x + label_width / 2, y + label_height / 2)
        c.rotate(rotation_angle)
        c.drawString(-label_height / 2 + 10, -label_width / 2 + 20, label)
        c.drawImage(img.seek(0), -label_height / 2 + 10, -label_width / 2 + 40, width=50, height=50)
        c.restoreState()
        if (i + 1) % (labels_per_row * labels_per_column) == 0:
            c.showPage()
    c.save()

# Example labels
labels = [f"Label {i+1}" for i in range(8)]
create_labels("avery_61612_labels.pdf", labels, rotation_angle=90)

print("PDF with Avery 61612 labels created successfully.")