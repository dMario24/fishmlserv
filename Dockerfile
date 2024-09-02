FROM python:3.11

WORKDIR /code

#COPY . /code/
COPY  src/fishmlserv/main.py /code/

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install git+https://<MY_PIP_GITHUB_URL>

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
