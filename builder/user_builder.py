import random
import secrets
import string


class UserBuilder:
    def __init__(self):
        self.email = self._generate_random_email()
        self.password = self._generate_random_password()
        self.roles = ["ROLE_ADMIN"]

    @staticmethod
    def _generate_random_email():
        domains = ["example.com", "test.com", "demo.com"]
        name = ''.join(random.choices(string.ascii_lowercase, k=8))
        domain = random.choice(domains)
        return f"{name}@{domain}"

    @staticmethod
    def _generate_random_password():
        # Password with at least 8 characters, including letters and digits
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for i in range(12))
        return password

    def build(self):
        return {
            "email": self.email,
            "password": self.password,
            "roles": self.roles
        }
