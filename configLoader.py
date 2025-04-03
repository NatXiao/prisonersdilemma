import json

def load_config(config_file="config.json"):
    """Charge la configuration depuis un fichier JSON."""
    with open(config_file, "r", encoding="utf-8") as file:
        return json.load(file)

# Exemple d'utilisation
config = load_config()