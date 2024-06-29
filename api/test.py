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
    response = client.post("/compareText",json={"textBase":"hello","text":"hello"})
    assert response.status_code == 200
    
def test_compare_text_root_fifth():
    response = client.post("/compareText",json={"textBase":"Whats your name?","text":"What's your name?"})
    assert response.status_code == 200
    assert response.json() == ["What's"]

def test_get_data_by_level_root_first():
    response = client.post("/getDataByLevel",json={"level":1})
    assert response.status_code == 422

def test_get_data_by_level_root_second():
    response = client.post("/getDataByLevel",json={"level":'easy'})
    assert  response.status_code == 200

def test_get_data_by_level_root_third():
    response = client.post("/getDataByLevel",json={"level":'easy'})
    assert  response.json() != None

def test_get_data_by_level_root_fourth():
    response = client.post("/getDataByLevel",json={"level":'medium'})
    assert response.json() == [
        {"pl": "Czy mówisz po angielsku?", "eng": "Do you speak English?", "ger": "Sprechen Sie Englisch?"},
        {"pl": "Gdzie jest najbliższy hotel?", "eng": "Where is the nearest hotel?", "ger": "Wo ist das nächste Hotel?"},
        {"pl": "Ile to kosztuje?", "eng": "How much does it cost?", "ger": "Wie viel kostet das?"},
        {"pl": "Proszę o pomoc", "eng": "Please help me", "ger": "Bitte helfen Sie mir"},
        {"pl": "Która jest godzina?", "eng": "What time is it?", "ger": "Wie spät ist es?"},
        {"pl": "Czy mogę prosić o rachunek?", "eng": "Can I have the bill, please?", "ger": "Kann ich bitte die Rechnung haben?"},
        {"pl": "Jak dojadę do centrum?", "eng": "How do I get to the city center?", "ger": "Wie komme ich ins Stadtzentrum?"},
        {"pl": "Czy mogę zamówić taksówkę?", "eng": "Can I order a taxi?", "ger": "Kann ich ein Taxi bestellen?"},
        {"pl": "Czy są tu jakieś restauracje?", "eng": "Are there any restaurants around here?", "ger": "Gibt es hier Restaurants?"},
        {"pl": "Czy to jest daleko?", "eng": "Is it far?", "ger": "Ist es weit?"},
        {"pl": "Gdzie jest toaleta?", "eng": "Where is the toilet?", "ger": "Wo ist die Toilette?"},
        {"pl": "Czy to jest blisko?", "eng": "Is it near?", "ger": "Ist es nah?"}
    ]

def test_get_data_by_level_root_fifth():
    response = client.post("/getDataByLevel",json={"level":'harddd'})
    assert response.json()['detail'] == "Level not found"