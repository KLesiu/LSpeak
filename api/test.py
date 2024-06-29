from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_compare_text_root_first():
    response = client.post("/compareText",json={"textBase":"hello","text":"hello"})
    assert response.status_code == 200
    assert response.json() == []


def test_compare_text_root_second():
    response = client.post("/compareText",json={"textBase":"hellofs","text":"hello"})
    assert response.status_code == 200
    assert response.json() == ['hello']

    
def test_compare_text_root_third():
    response = client.post("/compareText",json={"textBase":"hello","text":"goodbye"})
    assert response.status_code == 200
    assert response.json() == ['goodbye']
    
def test_compare_text_root_fourth():
    response = client.post("/compareText",json={"textBase":"hello","text":"f"})
    assert response.status_code == 200
    assert response.json() == ['f']
    
def test_compare_text_root_fifth():
    response = client.post("/compareText",json={"textBase":"Whats your name?","text":"What's your name?"})
    assert response.status_code == 200
    assert response.json() == ["What's"]

def test_transcribe_text_root():
    response = client.post("/transcribeText",json={"file":"hello"})

