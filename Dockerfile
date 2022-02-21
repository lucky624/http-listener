FROM python:3.9.5
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ADD server.py /server.py
CMD python server.py