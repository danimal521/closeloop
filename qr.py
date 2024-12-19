
import pyqrcode
from io import BytesIO
from pyzbar import pyzbar

def generate_qr_code(data):
    qr = pyqrcode.create(data)
    buffer = BytesIO()
    qr.png(buffer, scale=6)
    buffer.seek(0)
    return buffer

def decode_qr_code(frame):
    decoded_objects = pyzbar.decode(frame)
    qr_codes = [obj.data.decode('utf-8') for obj in decoded_objects]
    return qr_codes