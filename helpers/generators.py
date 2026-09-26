import uuid

from data.users import DEFAULT_PASSWORD


def generate_unique_email():
    return f"user_{uuid.uuid4().hex[:8]}@test.com"


def generate_unique_user():
    return {
        "email": generate_unique_email(),
        "password": DEFAULT_PASSWORD,
    }