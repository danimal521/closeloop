import uuid
import streamlit as st
import io
import streamlit as st
import numpy as np
from PIL import Image
from qr import decode_qr_code
from azure.cosmos import CosmosClient, PartitionKey, exceptions

COSMOS_URI = ''
COSMOS_KEY = ''
client = CosmosClient(COSMOS_URI, COSMOS_KEY)
database_name = 'closeloop'
try:
    database = client.create_database_if_not_exists(id=database_name)
    print(f'Database {database_name} created successfully.')
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)
    print(f'Database {database_name} already exists.')

container_name = 'leads'
try:
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path='/partitionKey'),
        offer_throughput=400
    )
    print(f'Container {container_name} created successfully.')
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(container_name)
    print(f'Container {container_name} already exists.')

st.title("Scan a Badge")
st.write("Scan a customer badge and enter any request information.")

picture = st.camera_input("")

if picture is not None:
    image = Image.open(io.BytesIO(picture.getvalue()))
    grayscale_image = image.convert("L")
    image_array = np.array(grayscale_image)    
    qr_codes = decode_qr_code(image_array)
    if(len(qr_codes)) > 0:
        stremail = qr_codes[0]
        st.success(stremail)
        strRequest = st.text_input("Enter request")
    
        if st.button("Save"):
            if strRequest:
                 item = {
                            'id': str(uuid.uuid4()),
                            'partitionKey': stremail,
                            'request': strRequest
                        }
                 container.create_item(body=item)
                 st.toast('Saved!', icon='🎉')       
        

       