from src.app import app

def test_home():
    client = app.test_client()
    assert client.get('/').status_code == 200

def test_health():
    client = app.test_client()
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json['status'] == 'ok'

def test_products():
    client = app.test_client()
    res = client.get('/api/products')
    assert len(res.json) == 2