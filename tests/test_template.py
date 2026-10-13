"""Tests du gabarit index.html : libellés des boutons et affichage initial."""
import re
from html.parser import HTMLParser

import pytest
from app import app


class ButtonParser(HTMLParser):
    """Extrait les <button> (attributs + libellé) d'une page HTML."""

    def __init__(self):
        super().__init__()
        self.buttons = []
        self._current = None

    def handle_starttag(self, tag, attrs):
        if tag == "button":
            self._current = {"attrs": dict(attrs), "label": ""}

    def handle_data(self, data):
        if self._current is not None:
            self._current["label"] += data

    def handle_endtag(self, tag):
        if tag == "button" and self._current is not None:
            self._current["label"] = self._current["label"].strip()
            self.buttons.append(self._current)
            self._current = None


@pytest.fixture
def client():
    """Client de test Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def get_buttons(client):
    """Retourne la liste des boutons de la page d'accueil."""
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
    """Aucun bouton ne doit être vide (sinon invisible pour l'utilisateur)."""
    for b in get_buttons(client):
        assert b["label"] != "", f"Bouton sans libellé : {b['attrs']}"


def test_equals_button_submits_form(client):
    """Le bouton '=' doit être de type submit."""
    submits = [b for b in get_buttons(client) if b["attrs"].get("type") == "submit"]
    assert any(b["label"] == "=" for b in submits)


def test_initial_display_is_empty(client):
    """À l'ouverture, l'affichage doit être vide (pas 'None')."""
    html = client.get("/").data.decode()
    match = re.search(r'<input[^>]*name="display"[^>]*value="([^"]*)"', html)
    assert match is not None
    assert match.group(1) == ""