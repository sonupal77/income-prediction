FROM python:3.9.5
COPY . /usr/app/
EXPOSE 8080
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python app.py