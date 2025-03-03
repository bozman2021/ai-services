import secrets
import string
import uuid  # Ensure UUID is imported

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def hook(context):
    print("\nDEBUG: copier_pre_gen.py is running!\n")  # Debug message to check if the hook runs

    # Generate values
    generated_password = generate_password()
    generated_uuid = str(uuid.uuid4())

    # Inject values into the Copier context
    context.update({
        "postgress_password": generated_password,
        "random_uuid": generated_uuid
    })

    # Debugging Output
    print(f"\nDEBUG: Injected values into Copier context ->")
    print(f"  postgress_password: {generated_password}")
    print(f"  random_uuid: {generated_uuid}\n")

# Ensure script runs when executed manually
if __name__ == "__main__":
    print("\nDEBUG: Running copier_pre_gen.py manually...")
    hook({"postgress_password": "", "random_uuid": ""})  # Test with dummy context
