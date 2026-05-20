from app.models import User

def filter_users_by_company_name(
    users: list[User]
) -> list[User]:
    filtered_users = []

    for user in users:
        # Récupère le champs "compagny" de l'utilisateur
        company = user.get("company")

        # Si pas de champs, passe à l'utilisateur suivant
        if not company:
            continue

        # Récupère le champs "name" du champs "compagny"
        company_name = company.get("name", "")

        # Rajoute l'utilisateur au tableau filtered_users si "e" est dans le champs "name" de "compagny"
        if "e" in company_name.lower():
            filtered_users.append(user)

    return filtered_users