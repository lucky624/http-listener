FROM python:3.10.0b4
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ADD server.py /server.py
CMD python server.py