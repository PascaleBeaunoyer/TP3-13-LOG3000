"""Tests unitaires du module operators."""
import pytest
from operators import add, divide, subtract, multiply


def test_add_positive_numbers():
    """Vérifie que l'addition de deux entiers positifs retourne la bonne somme."""
    assert add(2, 3) == 5

def test_divide():
    """Vérifie que la division de deux entiers retourne le bon quotient."""
    assert divide(6, 2) == 3

def test_divide_by_zero():
    """Vérifie que la division par zéro est gérée (erreur levée ou message)."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_subtract():
    """Vérifie que la soustraction de deux entiers retourne la bonne différence."""
    assert subtract(5, 3) == 2

def test_multiply():
    """Vérifie que la multiplication de deux entiers retourne le bon produit."""
    assert multiply(2, 3) == 6