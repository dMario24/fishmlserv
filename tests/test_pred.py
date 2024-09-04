from fishmlserv.rest.get import pred

def test_pred():
  r = pred(10,10)
  assert r == "빙어"

