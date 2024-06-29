from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_compare_text_route_first():
    response = client.post("/compareText",json={"textBase":"hello","text":"hello"})
    assert response.status_code == 200
    assert response.json() == []


def test_compare_text_route_second():
    response = client.post("/compareText",json={"textBase":"hellofs","text":"hello"})
    assert response.status_code == 200
    assert response.json() == ['hello']

    
def test_compare_text_route_third():
    response = client.post("/compareText",json={"textBase":"hello","text":"goodbye"})
    assert response.status_code == 200
    assert response.json() == ['goodbye']
    
def test_compare_text_route_fourth():
    response = client.post("/compareText",json={"textBase":"hello","text":"hello"})
    assert response.status_code == 200
    
def test_compare_text_route_fifth():
    response = client.post("/compareText",json={"textBase":"Whats your name?","text":"What's your name?"})
    assert response.status_code == 200
    assert response.json() == ["What's"]

def test_get_data_by_level_route_first():
    response = client.post("/getDataByLevel",json={"level":1})
    assert response.status_code == 422

def test_get_data_by_level_route_second():
    response = client.post("/getDataByLevel",json={"level":'easy'})
    assert  response.status_code == 200

def test_get_data_by_level_route_third():
    response = client.post("/getDataByLevel",json={"level":'easy'})
    assert  response.json() != None

def test_get_data_by_level_route_fourth():
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

def test_get_data_by_level_route_fifth():
    response = client.post("/getDataByLevel",json={"level":'harddd'})
    assert response.json()['detail'] == "Level not found"

def test_get_data_by_level_route_sixth():
    response = client.post("/getDataByLevel",json={"level":'hard'})
    assert response.json() == [
        {"pl": "Mam na imię Jan i jestem z Polski", "eng": "My name is John and I am from Poland", "ger": "Mein Name ist Jan und ich komme aus Polen"},
        {"pl": "Miło cię poznać, jak się nazywasz?", "eng": "Nice to meet you, what is your name?", "ger": "Freut mich, dich kennenzulernen, wie heißt du?"},
        {"pl": "Skąd pochodzisz i co tu robisz?", "eng": "Where are you from and what are you doing here?", "ger": "Woher kommst du und was machst du hier?"},
        {"pl": "Czy mógłbyś mi powiedzieć, jak dotrzeć do najbliższej stacji?", "eng": "Could you tell me how to get to the nearest station?", "ger": "Könnten Sie mir sagen, wie ich zur nächsten Station komme?"},
        {"pl": "Czy mogę zarezerwować pokój na dwie noce?", "eng": "Can I book a room for two nights?", "ger": "Kann ich ein Zimmer für zwei Nächte buchen?"},
        {"pl": "Czy mogę zapłacić gotówką?", "eng": "Can I pay with cash?", "ger": "Kann ich bar bezahlen?"},
        {"pl": "Czy w tym hotelu jest dostęp do internetu?", "eng": "Is there internet access in this hotel?", "ger": "Gibt es in diesem Hotel Internetzugang?"},
        {"pl": "Jaki jest najbliższy przystanek autobusowy?", "eng": "Where is the nearest bus stop?", "ger": "Wo ist die nächste Bushaltestelle?"},
        {"pl": "Czy mogę wymienić pieniądze w recepcji?", "eng": "Can I exchange money at the reception?", "ger": "Kann ich an der Rezeption Geld wechseln?"},
        {"pl": "Czy mógłby Pan mi powiedzieć, gdzie jest najbliższa apteka?", "eng": "Could you tell me where the nearest pharmacy is?", "ger": "Könnten Sie mir sagen, wo die nächste Apotheke ist?"},
        {"pl": "Czy mogę zarezerwować stolik na dziś wieczór?", "eng": "Can I reserve a table for tonight?", "ger": "Kann ich einen Tisch für heute Abend reservieren?"},
        {"pl": "Czy mogę zostawić bagaż w hotelu?", "eng": "Can I leave my luggage at the hotel?", "ger": "Kann ich mein Gepäck im Hotel lassen?"}
    ]


def test_get_data_by_level_route_seventh():
    response = client.post("/getDataByLevel",json={"level":'extreme'})
    assert response.json()== [
        {"pl": "Przepraszam, czy mogę zapłacić kartą za moje zamówienie w tej restauracji?", "eng": "Excuse me, can I pay by card for my order in this restaurant?", "ger": "Entschuldigung, kann ich in diesem Restaurant mit Karte bezahlen?"},
        {"pl": "Chciałbym zarezerwować stolik dla czterech osób na jutro wieczór, proszę", "eng": "I would like to reserve a table for four people for tomorrow evening, please", "ger": "Ich möchte einen Tisch für vier Personen für morgen Abend reservieren, bitte"},
        {"pl": "Poproszę menu w języku angielskim, ponieważ nie mówię dobrze po polsku", "eng": "Can I have the menu in English, because I don't speak Polish well", "ger": "Kann ich die Speisekarte auf Englisch haben, weil ich nicht gut Polnisch spreche"},
        {"pl": "Czy mógłby Pan mi powiedzieć, jak najlepiej dostać się do muzeum komunikacji miejskiej?", "eng": "Could you tell me the best way to get to the public transport museum?", "ger": "Könnten Sie mir sagen, wie ich am besten zum Nahverkehrsmuseum komme?"},
        {"pl": "Czy mogę prosić o dodatkowe ręczniki do mojego pokoju?", "eng": "Can I have some extra towels for my room?", "ger": "Kann ich zusätzliche Handtücher für mein Zimmer haben?"},
        {"pl": "Czy mogę zapłacić z góry za cały pobyt?", "eng": "Can I pay in advance for the entire stay?", "ger": "Kann ich im Voraus für den gesamten Aufenthalt bezahlen?"},
        {"pl": "Czy mogę prosić o późniejsze wymeldowanie?", "eng": "Can I request a late check-out?", "ger": "Kann ich einen späten Check-out beantragen?"},
        {"pl": "Czy możecie zorganizować transport na lotnisko?", "eng": "Can you arrange transportation to the airport?", "ger": "Können Sie einen Transport zum Flughafen organisieren?"},
        {"pl": "Czy w pobliżu jest jakieś miejsce, gdzie mogę wynająć rower?", "eng": "Is there a place nearby where I can rent a bicycle?", "ger": "Gibt es in der Nähe einen Ort, an dem ich ein Fahrrad mieten kann?"},
        {"pl": "Czy mógłby Pan zadzwonić po taksówkę?", "eng": "Could you call a taxi for me?", "ger": "Könnten Sie mir ein Taxi rufen?"},
        {"pl": "Czy mogę prosić o dodatkowy klucz do pokoju?", "eng": "Can I have an extra key to my room?", "ger": "Kann ich einen zusätzlichen Schlüssel zu meinem Zimmer haben?"},
        {"pl": "Czy możecie polecić jakieś dobre restauracje w pobliżu?", "eng": "Can you recommend any good restaurants nearby?", "ger": "Können Sie gute Restaurants in der Nähe empfehlen?"}
    ]

def test_get_all_data_first():
    response = client.get("/getAllData")
    assert response.status_code == 200

def test_get_all_data_second():
    response = client.get("/getAllData")
    assert response.json() == {
    "easy": [
        {"pl": "Dzień dobry", "eng": "Good morning", "ger": "Guten Morgen"},
        {"pl": "Jak się masz?", "eng": "How are you?", "ger": "Wie geht's?"},
        {"pl": "Do widzenia", "eng": "Goodbye", "ger": "Auf Wiedersehen"},
        {"pl": "Dziękuję", "eng": "Thank you", "ger": "Danke"},
        {"pl": "Tak", "eng": "Yes", "ger": "Ja"},
        {"pl": "Przepraszam", "eng": "Excuse me", "ger": "Entschuldigung"},
        {"pl": "Proszę", "eng": "Please", "ger": "Bitte"},
        {"pl": "Nie rozumiem", "eng": "I don't understand", "ger": "Ich verstehe nicht"},
        {"pl": "Mogę pomóc?", "eng": "Can I help?", "ger": "Kann ich helfen?"},
        {"pl": "Cześć", "eng": "Hello", "ger": "Hallo"},
        {"pl": "Dobry wieczór", "eng": "Good evening", "ger": "Guten Abend"},
        {"pl": "Nie", "eng": "No", "ger": "Nein"}
    ]
    ,
    "medium": [
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
    ,
    "hard": [
        {"pl": "Mam na imię Jan i jestem z Polski", "eng": "My name is John and I am from Poland", "ger": "Mein Name ist Jan und ich komme aus Polen"},
        {"pl": "Miło cię poznać, jak się nazywasz?", "eng": "Nice to meet you, what is your name?", "ger": "Freut mich, dich kennenzulernen, wie heißt du?"},
        {"pl": "Skąd pochodzisz i co tu robisz?", "eng": "Where are you from and what are you doing here?", "ger": "Woher kommst du und was machst du hier?"},
        {"pl": "Czy mógłbyś mi powiedzieć, jak dotrzeć do najbliższej stacji?", "eng": "Could you tell me how to get to the nearest station?", "ger": "Könnten Sie mir sagen, wie ich zur nächsten Station komme?"},
        {"pl": "Czy mogę zarezerwować pokój na dwie noce?", "eng": "Can I book a room for two nights?", "ger": "Kann ich ein Zimmer für zwei Nächte buchen?"},
        {"pl": "Czy mogę zapłacić gotówką?", "eng": "Can I pay with cash?", "ger": "Kann ich bar bezahlen?"},
        {"pl": "Czy w tym hotelu jest dostęp do internetu?", "eng": "Is there internet access in this hotel?", "ger": "Gibt es in diesem Hotel Internetzugang?"},
        {"pl": "Jaki jest najbliższy przystanek autobusowy?", "eng": "Where is the nearest bus stop?", "ger": "Wo ist die nächste Bushaltestelle?"},
        {"pl": "Czy mogę wymienić pieniądze w recepcji?", "eng": "Can I exchange money at the reception?", "ger": "Kann ich an der Rezeption Geld wechseln?"},
        {"pl": "Czy mógłby Pan mi powiedzieć, gdzie jest najbliższa apteka?", "eng": "Could you tell me where the nearest pharmacy is?", "ger": "Könnten Sie mir sagen, wo die nächste Apotheke ist?"},
        {"pl": "Czy mogę zarezerwować stolik na dziś wieczór?", "eng": "Can I reserve a table for tonight?", "ger": "Kann ich einen Tisch für heute Abend reservieren?"},
        {"pl": "Czy mogę zostawić bagaż w hotelu?", "eng": "Can I leave my luggage at the hotel?", "ger": "Kann ich mein Gepäck im Hotel lassen?"}
    ]
    ,
    "extreme": [
        {"pl": "Przepraszam, czy mogę zapłacić kartą za moje zamówienie w tej restauracji?", "eng": "Excuse me, can I pay by card for my order in this restaurant?", "ger": "Entschuldigung, kann ich in diesem Restaurant mit Karte bezahlen?"},
        {"pl": "Chciałbym zarezerwować stolik dla czterech osób na jutro wieczór, proszę", "eng": "I would like to reserve a table for four people for tomorrow evening, please", "ger": "Ich möchte einen Tisch für vier Personen für morgen Abend reservieren, bitte"},
        {"pl": "Poproszę menu w języku angielskim, ponieważ nie mówię dobrze po polsku", "eng": "Can I have the menu in English, because I don't speak Polish well", "ger": "Kann ich die Speisekarte auf Englisch haben, weil ich nicht gut Polnisch spreche"},
        {"pl": "Czy mógłby Pan mi powiedzieć, jak najlepiej dostać się do muzeum komunikacji miejskiej?", "eng": "Could you tell me the best way to get to the public transport museum?", "ger": "Könnten Sie mir sagen, wie ich am besten zum Nahverkehrsmuseum komme?"},
        {"pl": "Czy mogę prosić o dodatkowe ręczniki do mojego pokoju?", "eng": "Can I have some extra towels for my room?", "ger": "Kann ich zusätzliche Handtücher für mein Zimmer haben?"},
        {"pl": "Czy mogę zapłacić z góry za cały pobyt?", "eng": "Can I pay in advance for the entire stay?", "ger": "Kann ich im Voraus für den gesamten Aufenthalt bezahlen?"},
        {"pl": "Czy mogę prosić o późniejsze wymeldowanie?", "eng": "Can I request a late check-out?", "ger": "Kann ich einen späten Check-out beantragen?"},
        {"pl": "Czy możecie zorganizować transport na lotnisko?", "eng": "Can you arrange transportation to the airport?", "ger": "Können Sie einen Transport zum Flughafen organisieren?"},
        {"pl": "Czy w pobliżu jest jakieś miejsce, gdzie mogę wynająć rower?", "eng": "Is there a place nearby where I can rent a bicycle?", "ger": "Gibt es in der Nähe einen Ort, an dem ich ein Fahrrad mieten kann?"},
        {"pl": "Czy mógłby Pan zadzwonić po taksówkę?", "eng": "Could you call a taxi for me?", "ger": "Könnten Sie mir ein Taxi rufen?"},
        {"pl": "Czy mogę prosić o dodatkowy klucz do pokoju?", "eng": "Can I have an extra key to my room?", "ger": "Kann ich einen zusätzlichen Schlüssel zu meinem Zimmer haben?"},
        {"pl": "Czy możecie polecić jakieś dobre restauracje w pobliżu?", "eng": "Can you recommend any good restaurants nearby?", "ger": "Können Sie gute Restaurants in der Nähe empfehlen?"}
    ]
    
}

