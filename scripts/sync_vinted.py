
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone

VINTED_PROFILE = "https://www.vinted.fr/member/171121583"

def tester_vinted():
    print("=== Test de synchronisation YrtalBox ===")
    print("Profil :", VINTED_PROFILE)

    request = urllib.request.Request(
        VINTED_PROFILE,
        headers={
            "User-Agent": "YrtalBox-Catalogue-Test/1.0",
            "Accept": "text/html"
        }
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            html = response.read().decode("utf-8", errors="replace")
            status = response.status

        resultat = {
            "date": datetime.now(timezone.utc).isoformat(),
            "status_http": status,
            "taille_page": len(html),
            "annonces_recuperees": 0,
            "synchronisation": False
        }

        print("Page accessible :", status)
        print("Taille de la page :", len(html), "caracteres")
        print("Aucune annonce extraite pour le moment.")
        print(json.dumps(resultat, indent=2))

    except urllib.error.HTTPError as erreur:
        print("Acces refuse ou indisponible :", erreur.code)
    except Exception as erreur:
        print("Erreur :", type(erreur).__name__, str(erreur))

if __name__ == "__main__":
    tester_vinted()
