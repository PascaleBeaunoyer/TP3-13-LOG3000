import re
from html.parser import HTMLParser

import pytest
from app import app


class ButtonParser(HTMLParser):
    """Rôle: Tests du gabarit index.html : libellés des boutons et affichage initial en
    extrayant les <button> (attributs + libellé) d'une page HTML.
    Entrées: page HTML (str)
    Sortie: liste de boutons (dict avec 'attrs' et 'label')"""

    def __init__(self):
        """Rôle: initialise le parser HTML pour extraire les boutons.
        Entrées: aucune
        Sortie: aucune"""
        super().__init__()
        self.buttons = []
        self._current = None

    def handle_starttag(self, tag, attrs):
        """Rôle: détecte le début d'un bouton et initialise un dictionnaire pour stocker ses attributs et son libellé.
        Entrées: tag (str) est le nom de la balise, attrs (list) est la liste des attributs de la balise
        Sortie: aucune"""
        if tag == "button":
            self._current = {"attrs": dict(attrs), "label": ""}

    def handle_data(self, data):
        """Rôle: ajoute le texte à l'intérieur d'un bouton au libellé du bouton en cours.
        Entrées: data (str) est le texte à l'intérieur de la balise
        Sortie: aucune"""
        if self._current is not None:
            self._current["label"] += data

    def handle_endtag(self, tag):
        """Rôle: détecte la fin d'un bouton et ajoute le bouton à la liste des boutons.
        Entrées: tag (str) est le nom de la balise
        Sortie: aucune"""
        if tag == "button" and self._current is not None:
            self._current["label"] = self._current["label"].strip()
            self.buttons.append(self._current)
            self._current = None


@pytest.fixture
def client():
    """Rôle: Client de test Flask.
    Entrées: aucune
    Sortie: client Flask pour effectuer des requêtes de test"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def get_buttons(client):
    """Rôle: Retourne la liste des boutons de la page d'accueil.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: list - la liste des boutons"""
    parser = ButtonParser()
    parser.feed(client.get("/").data.decode())
    return parser.buttons


@pytest.mark.parametrize("key", list("0123456789+-*/"))
def test_button_exists_with_correct_label(client, key):
    """Chaque touche doit avoir un bouton dont le libellé est exactement la touche."""
    found = False
    for b in get_buttons(client):
        onclick = b["attrs"].get("onclick", "")
        if f"appendToDisplay('{key}')" in onclick:
            found = True
            assert b["label"] == key, f"Le bouton '{key}' affiche '{b['label']}'"
    assert found, f"Aucun bouton n'ajoute '{key}' à l'affichage"


def test_no_button_has_empty_label(client):
    """Rôle: Vérifie que aucun bouton n'a un libellé vide.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: aucune"""
    for b in get_buttons(client):
        assert b["label"] != "", f"Bouton sans libellé : {b['attrs']}"


def test_equals_button_submits_form(client):
    """Rôle: Vérifie que le bouton '=' est de type submit.
    Entrées: client (FlaskClient) - le client de test Flask
    Sortie: aucune"""
    submits = [b for b in get_buttons(client) if b["attrs"].get("type") == "submit"]
    assert any(b["label"] == "=" for b in submits)


def test_initial_display_is_empty(client):
    """Rôle: Vérifie que l'affichage est vide à l'ouverture.
    Entrées: client (FlaskClient) est le client de test Flask
    Sortie: aucune"""
    html = client.get("/").data.decode()
    match = re.search(r'<input[^>]*name="display"[^>]*value="([^"]*)"', html)
    assert match is not None
    assert match.group(1) == ""