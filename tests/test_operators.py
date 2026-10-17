"""Tests unitaires du module operators."""
import pytest
from operators import add, divide, subtract, multiply


def test_add_positive_numbers():
    """Rôle: Vérifie que l'addition de deux entiers positifs retourne la bonne somme.
    Entrées: aucune
    Sortie: aucune"""
    assert add(2, 3) == 5

def test_divide():
    """Rôle: Vérifie que la division de deux entiers retourne le bon quotient.
    Entrées: aucune
    Sortie: aucune"""
    assert divide(6, 2) == 3

def test_divide_float():
    """Rôle: Vérifie que la division de deux nombres retourne le bon quotient (à virgule).
    Entrées: aucune
    Sortie: aucune"""
    assert divide(1, 2) == 0.5

def test_divide_by_zero():
    """Rôle: Vérifie que la division par zéro est gérée (erreur levée ou message).
    Entrées: aucune
    Sortie: aucune"""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_subtract():
    """Rôle: Vérifie que la soustraction de deux entiers retourne la bonne différence.
    Entrées: aucune
    Sortie: aucune"""
    assert subtract(5, 3) == 2

def test_multiply():
    """Rôle: Vérifie que la multiplication de deux entiers retourne le bon produit.
    Entrées: aucune
    Sortie: aucune"""
    assert multiply(2, 3) == 6