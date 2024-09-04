from fishmlserv.curl import get

def test_get():
    r = get(10, 10)
    assert r == "빙어"
