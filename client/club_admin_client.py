from client.base_client import BaseClient
from config.settings import settings


class ClubAdminClient(BaseClient):
    """
        Client for Club Administration API interactions.
    """

    def create_user(self, user_data):
        """
        Creates a new user.

        Args:
            user_data (dict): A dictionary containing user information.

        Returns:
            dict: The response from the API containing the created user's details.
        """
        url = f"{settings.API_BASE_URL}/api/auth/register"
        return self.post(url, user_data)
