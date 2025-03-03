import secrets
import string
import uuid

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def hook(context):
    context['postgress_password'] = generate_password()
