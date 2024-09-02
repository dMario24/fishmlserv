# fishmlserv

### Deploy
![image](https://github.com/user-attachments/assets/e3af6d93-78de-416d-bf0d-c1079d42a4ef)

### Run
- dev
- http://localhost:8000/docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```
- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```

### Docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
```

### Fly.io
```
$ fly launch --no-deploy
$ flyctl launch --name mariofish
$ flyctl scale memory 256
$ flyctl deploy
```

### Ref
- https://curlconverter.com/python
