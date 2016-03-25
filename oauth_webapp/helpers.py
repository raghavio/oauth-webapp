"""
Helper functions used throughout application
"""
import json


def is_new_user(email):
    """
    Checks if a user is new or not by checking email against other emails in database.
    :param email: Email of the user
    :return: True if email does not exist in database else False
    """
    with open("database", "r") as database:
        for user in database.readlines():
            user_data = json.loads(user)
            if user_data["email"] == email:
                return False
    return True


def create_new_user(user_data):
    """
    Creates a new user.
    Writes a JSON object containing provider, email, id and name of the user in a plain text file (database).
    :param user_data: Everything returned by the oauth provider.
    :return: None
    """
    with open("database", "a") as database:
        fields = user_data["fields"]

        provider = user_data["provider"]
        email = fields["email"]
        user_id = fields["id"]
        name = fields["name"]

        data_to_store = {"provider": provider, "email": email, "id": user_id, "name": name}

        database.write(json.dumps(data_to_store))
        database.write("\n")
