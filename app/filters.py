from app.models import User

def filter_users_by_company_name(
    users: list[User]
) -> list[User]:
    filtered_users = []

    for user in users:
        company = user.get("company")

        if not company:
            continue

        company_name = company.get("name", "")

        if "e" in company_name.lower():
            filtered_users.append(user)

    return filtered_users