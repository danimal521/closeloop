FROM python:3.11.7-slim

EXPOSE 8000

RUN mkdir /app 
  
ADD . /app   

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y  
RUN apt-get install zbar-tools -y
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]   