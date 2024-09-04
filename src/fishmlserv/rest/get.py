import requests

def pred(l, w, url="http://localhost:8765/fish"):
  # GET 요청을 보낼 URL 설정
  
  params = {
      "length": 10,
      "weight": 10
  }

  # GET 요청 보내기
  response = requests.get(url, params=params)

  # 응답에서 JSON 데이터 추출
  data = response.json()

  # 'prediction' 값 추출
  r = data.get("prediction")

  print(f"Prediction: {r}")

  return r
