FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY chromedriver .
RUN mv chromedriver /usr/local/bin
RUN chmod +x /usr/local/bin/chromedriver
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
#Server will reload itself on file changes if in dev mode
ENV FLASK_ENV=development 
RUN apt-get update -y
RUN apt-get install nano -y
RUN apt-get install wget -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome-stable_current_amd64.deb -y
RUN apt-get install -y libglib2.0-0 \
    libx11-6 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]