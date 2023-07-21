import random
import string


def generate_password(length: int = 20, special_character: bool = False):
    # Define character universe
    character_sets = string.ascii_letters + string.digits
    if special_character:
        character_sets += string.punctuation

    random_password = ''.join([''.join(random.choices(character_sets, k=length))])

    return random_password


if __name__ == "__main__":
    password_length = 30
    generated_password = generate_password(password_length, special_character=True)
    print("Generated Password:", generated_password)
