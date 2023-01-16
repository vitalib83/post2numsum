FROM python:3.8

COPY . /app
WORKDIR /app
RUN pip install flask


EXPOSE 5000:5000
CMD ["python", "main.py"]
