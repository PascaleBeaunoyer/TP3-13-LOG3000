"""Tests des routes Flask de app.py (page d'accueil et calcul via POST)."""
import pytest
from app import app


@pytest.fixture
def client():
    """Crée un client de test Flask (aucun serveur n'est lancé)."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_home_page(client):
    """GET / doit retourner la page HTML avec un code 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data.lower()

def test_static_css_is_served(client):
    """Le fichier style.css doit être accessible."""
    response = client.get("/static/style.css")
    assert response.status_code == 200

def test_post_addition(client):
    """POST / avec une addition valide doit afficher le bon résultat."""
    response = client.post("/", data={"num1": "2", "num2": "3", "operation": "add"})
    assert response.status_code == 200
    assert b"5" in response.data


def test_post_only_division_operator(client):
    """Appuyer sur '/' puis '=' (expression incomplète) ne doit pas faire planter le serveur."""
    response = client.post("/", data={"display": "/"})
    assert response.status_code == 200  # pas de 500
    assert b"Traceback" not in response.data

def test_post_invalid_input(client):
    """Une entrée non numérique doit être gérée sans erreur serveur."""
    response = client.post("/", data={"num1": "abc", "num2": "3", "operation": "add"})
    assert response.status_code != 500