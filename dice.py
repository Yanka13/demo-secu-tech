

import random
from flask import Flask, jsonify

# Création de l'application Flask
app = Flask(__name__)

# Route pour le jeu de dés
@app.route("/roll_dice", methods=["GET"])
def roll_dice():
    # Génération d'un nombre aléatoire entre 1 et 6
    dice_roll = random.randint(1, 6) # nosec
    # Retour du résultat sous forme de JSON
    return jsonify({"result": dice_roll})

# Exécution de l'application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False) # nosec
