import secrets
import string
import uuid  # Ensure UUID is imported

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def hook(context):
    # Generate random values
    context['postgress_password'] = generate_password()
    context['random_uuid'] = str(uuid.uuid4())

    # Print debug information
    print("DEBUG: Injected values into Copier context:")
    print(f"  postgress_password: {context['postgress_password']}")
    print(f"  random_uuid: {context['random_uuid']}")
