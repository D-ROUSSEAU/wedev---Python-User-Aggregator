from app.models import User
from app.models import NormalizedUser

def normalize_users(
    users: list[User]
) -> list[NormalizedUser]:
    normalized_users: list[NormalizedUser] = []

    for user in users:
        address = user.get("address", {})

        normalized_user: NormalizedUser = {
            "id": user.get("id", 0),
            "full_name": user.get("name", "Unknown"),
            "email": user.get("email", "Unknown"),
            "city": address.get("city", "Unknown")
        }

        normalized_users.append(normalized_user)

    return normalized_users