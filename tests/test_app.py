"""Tests des routes Flask de app.py (page d'accueil et calcul via POST)."""
import pytest
from app import app


@pytest.fixture
def client():
    """Rôle: Crée un client de test Flask (aucun serveur n'est lancé).
    Entrées: aucune
    Sortie: client Flask pour effectuer des requêtes de test"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_home_page(client):
    """Rôle: Vérifie que la route GET / retourne la page HTML avec un code 200.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: aucune"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data.lower()

def test_static_css_is_served(client):
    """Rôle: Vérifie que le fichier style.css est accessible.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: aucune"""
    response = client.get("/static/style.css")
    assert response.status_code == 200

def test_post_addition(client):
    """Rôle: Vérifie que la route POST / avec une addition valide affiche le bon résultat.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: aucune"""
    response = client.post("/", data={"num1": "2", "num2": "3", "operation": "add"})
    assert response.status_code == 200
    assert b"5" in response.data


def test_post_only_division_operator(client):
    """Rôle: Vérifie que appuyer sur '/' puis '=' (expression incomplète) ne fait pas planter le serveur.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: aucune"""
    response = client.post("/", data={"display": "/"})
    assert response.status_code == 200  # pas de 500
    assert b"Traceback" not in response.data

def test_post_invalid_input(client):
    """Rôle: Vérifie que les entrées non numériques sont gérées sans erreur serveur.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: aucune"""
    response = client.post("/", data={"num1": "abc", "num2": "3", "operation": "add"})
    assert response.status_code != 500