import random
import secrets
import string


class StringBuilder:

    @staticmethod
    def generate_random_string(length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))