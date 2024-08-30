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

### Ref
- https://curlconverter.com/python
