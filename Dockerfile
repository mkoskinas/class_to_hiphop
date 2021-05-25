FROM python:3.9.4
COPY . .
RUN pip install -r requirements.txt
RUN export FLASK_APP=app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]