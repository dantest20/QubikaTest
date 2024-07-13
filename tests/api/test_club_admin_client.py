from builder.user_builder import UserBuilder


def test_create_user_ok(club_admin_client):
    # Given
    user_data = UserBuilder().build()
    # When
    new_user = club_admin_client.create_user(user_data)
    # Then
    assert new_user["id"]
    assert new_user["email"] == user_data["email"]
