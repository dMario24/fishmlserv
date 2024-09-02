FROM python:3.11

WORKDIR /code

COPY src/fishmlserv/main.py /code/

RUN pip install git+https://github.com/dMario24/fishmlserv.git@0.7/MANIFEST

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
