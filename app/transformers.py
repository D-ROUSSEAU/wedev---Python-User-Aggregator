from app.models import User
from app.models import NormalizedUser

def normalize_users(
    users: list[User]
) -> list[NormalizedUser]:
    normalized_users: list[NormalizedUser] = []

    for user in users:
        # Récupère le champs "address" de l'utilisateur
        address = user.get("address", {})

        # Créer un NormalizedUser
        normalized_user: NormalizedUser = {
            "id": user.get("id", 0),
            "full_name": user.get("name", "Unknown"),
            "email": user.get("email", "Unknown"),
            "city": address.get("city", "Unknown")
        }

        # Rajoute le NormalizedUser au tableau normalized_users
        normalized_users.append(normalized_user)

    return normalized_users