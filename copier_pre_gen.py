import secrets
import string
import uuid  # Import uuid for random UUID generation

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def hook(context):
    # Generate values and inject them into Copier's context
    context['postgress_password'] = generate_password()
    #context['random_uuid'] = str(uuid.uuid4())  # Store as string for Jinja
