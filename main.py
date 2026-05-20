import json
import logging

from app.api import fetch_users
from app.filters import filter_users_by_company_name
from app.transformers import normalize_users

def main() -> None:
    try:
        users = fetch_users()

        if not users:
            logging.warning("No users found")
            return

        filtered_users = filter_users_by_company_name(users)

        normalized_users = normalize_users(filtered_users)

        print(
            json.dumps(
                normalized_users,
                indent=4,
                ensure_ascii=False
            )
        )

    except Exception as error:
        logging.error(f"Unexpected application error: {error}")

if __name__ == "__main__":
    main()