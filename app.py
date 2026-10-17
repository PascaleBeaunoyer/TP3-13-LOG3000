from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide
"""
Rôle: application Flask pour effectuer des calculs simples via une interface web.
Entrées: aucune (les entrées sont fournies via le formulaire web).
Sortie: page HTML affichant le résultat du calcul ou un message d'erreur.
"""
app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Rôle: évalue une expression mathématique simple (deux opérandes et un opérateur).
       Entrées: expr (str) - expression mathématique sous forme de chaîne
       Sortie: résultat du calcul (float ou int) ou lève une exception si l'expression est invalide."""
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Rôle: page d'accueil de l'application Flask. Affiche un formulaire pour entrer une expression mathématique.
       Entrées: aucune (les entrées sont fournies via le formulaire web).
       Sortie: page HTML affichant le résultat du calcul ou un message d'erreur."""
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)