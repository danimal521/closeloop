import streamlit as st

if 'page' not in st.session_state:
    st.session_state.page = 'Scan Badge'

st.title("Main Page")
st.write("Welcome to the main page!")

st.page_link("pages/scanpage.py", label="Scan Badge", icon="1️⃣")

# # Navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.selectbox("Go to", ["Main Page", "Scan Badge", "Badges"])

# if page == "Scan Badge":
#     st.experimental_rerun("pages/scanpage.py")
# elif page == "Badges":
#     st.experimental_rerun("pages/badgepage.py")


# import io
# import streamlit as st
# import numpy as np
# from PIL import Image
# from qr import generate_qr_code, decode_qr_code


# def main():
#     st.title("Close Loop")

#     if st.button('Scan'):
#         print("scan")
#         picture = st.camera_input("Scan Badge")
#         if picture is not None:
#             print("read")

#     # varRead = None
#     # if st.button('Scan'):
#     #     print("scan")
#     #     picture = st.camera_input("Scan Badge")
#     #     print("start read")
#     #     if picture is not None:
#     #         print("picture")
#     #         image = Image.open(io.BytesIO(picture.getvalue()))
#     #         grayscale_image = image.convert("L")
#     #         image_array = np.array(grayscale_image)    
#     #         varRead = decode_qr_code(image_array)
            
#     # if varRead is not None:
#     #     st.success(varRead)
        
#     # st.success("test")

# # st.title("Webcam Picture Capture4")

# # # Enable the camera input
# # picture = st.camera_input("Take a picture")

# # if picture is not None:
# #     # img = Image.open(generate_qr_code("danimal"))
# #     # st.image(img, caption="Generated QR Code", use_column_width=False)
# #     # img.save("qrnew.png")
    
    
    
# #     image = Image.open(io.BytesIO(picture.getvalue()))
# #     #image = Image.open('qrnew.png')
# #     # #image = Image.open('captured_image.png')
    

# #     grayscale_image = image.convert("L")
# #     st.image(grayscale_image)

# #     # #grayscale_image.save("captured_image.png")
    
    
# #     image_array = np.array(grayscale_image)    
# #     qr_codes = decode_qr_code(image_array)
    
    
# #     st.success(qr_codes)
    
    




# # import streamlit as st
# # from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
# # import cv2

# # class VideoTransformer(VideoTransformerBase):
# #     def __init__(self):
# #         self.snapshot = None

# #     def transform(self, frame):
# #         img = frame.to_ndarray(format="bgr24")
# #         if self.snapshot:
# #             self.snapshot = img
# #         return img


# #     st.title("Take a Picture with Streamlit-WebRTC")
# #     ctx = webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

# #     if st.button("Take Snapshot"):
# #         if ctx.video_transformer:
# #             frame = ctx.video_transformer.frame
# #             if frame is not None:
# #                 st.image(frame, channels="BGR")
# #                 if st.button("Save Picture"):
# #                     cv2.imwrite("captured_image.jpg", frame)
# #                     st.success("Picture saved successfully!")

# if __name__ == "__main__":
#     main()

# # import streamlit as st
# # import pyqrcode
# # from io import BytesIO
# # from PIL import Image
# # import cv2
# # from pyzbar import pyzbar

# # def generate_qr_code(data):
# #     """
# #     Generates a QR code image from the provided data.

# #     Parameters:
# #     data (str): The data to encode in the QR code.

# #     Returns:
# #     BytesIO: The QR code image in a BytesIO buffer.
# #     """
# #     qr = pyqrcode.create(data)
# #     buffer = BytesIO()
# #     qr.png(buffer, scale=6)
# #     buffer.seek(0)
# #     return buffer

# # def decode_qr_code(frame):
# #     """
# #     Decodes QR codes in the given image frame.

# #     Parameters:
# #     frame (numpy.ndarray): The image frame to scan for QR codes.

# #     Returns:
# #     list: A list of decoded QR code data.
# #     """
# #     decoded_objects = pyzbar.decode(frame)
# #     qr_codes = [obj.data.decode('utf-8') for obj in decoded_objects]
# #     return qr_codes

# # def create_qr_code():
# #     st.title("QR Code Generator")
# #     data = st.text_input("Enter the data to encode in the QR code")  # input by user

# #     if data:
# #         qr_image = generate_qr_code(data)    # function generate_qr_code with data as argument
# #         img = Image.open(qr_image)

# #         st.image(img, caption="Generated QR Code", use_column_width=False)

# #         st.download_button(
# #             label="Download QR Code",
# #             data=qr_image,
# #             file_name="qrcode.png",
# #             mime="image/png"
# #         )

# # def scan_qr_code():
# #     st.title("QR Code Scanner")
# #     st.write("Click the button below to start the camera and scan a QR code.")

# #     # Initialize session state for control buttons and decoded message
# #     if "scanning" not in st.session_state:
# #         st.session_state.scanning = False

# #     if "decoded_message" not in st.session_state:
# #         st.session_state.decoded_message = None

# #     def start_scanning():
# #         st.session_state.scanning = True

# #     def stop_scanning():
# #         st.session_state.scanning = False

# #     if not st.session_state.scanning:
# #         if st.button('Start Scanning', key='start'):
# #             start_scanning()

# #     if st.session_state.scanning:
# #         cap = cv2.VideoCapture(0, cv2.CAP_V4L)

# #         # if not cap.isOpened():
# #         #     st.error("Could not open video device")

# #         stframe = st.empty()

# #         while st.session_state.scanning:
# #             ret, frame = cap.read()
# #             if not ret:
# #                 st.write("Failed to capture image.")
# #                 break

# #             qr_codes = decode_qr_code(frame)

# #             # Display the frame
# #             stframe.image(frame, channels="BGR")

# #             # Display the decoded QR codes if it's a new message
# #             if qr_codes:
# #                 if st.session_state.decoded_message != qr_codes[0]:
# #                     st.session_state.decoded_message = qr_codes[0]
# #                     st.success(f"Decoded QR Code: {qr_codes[0]}")
# #                     break

# #         if st.button('Stop Scanning', key='stop', on_click=stop_scanning):
# #             cap.release()
# #             cv2.destroyAllWindows()

# # st.title("QR Code Toolkit")

# # option = st.radio(
# #     "Choose an option:",
# #     ("Create QR", "Scan QR")
# # )

# # if option == "Create QR":
# #     create_qr_code()
# # elif option == "Scan QR":
# #     scan_qr_code()