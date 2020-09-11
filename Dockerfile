FROM python:3.6.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app:app
CMD ["flask", "run", "--host", "0.0.0.0"]