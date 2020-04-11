FROM python:3.8
ADD requirements.txt /requirements.txt
ADD server.py /server.py

RUN pip install -r requirements.txt
CMD python server.py