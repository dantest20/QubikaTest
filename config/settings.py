import os


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://club-administration.qa.qubika.com")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.club-administration.qa.qubika.com")
    HEADLESS = os.getenv("HEADLESS", "false").lower() in ["true", "1", "t"]
    EMAIL = os.getenv("EMAIL", "test.qubika@qubika.com")
    PASSWORD = os.getenv("PASSWORD", "12345678")


settings = Settings()
