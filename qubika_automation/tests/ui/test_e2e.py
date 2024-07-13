from builder.string_builder import StringBuilder
from builder.user_builder import UserBuilder
from pages.login.login_page import LoginPage
from pages.category.category_page import CategoryPage
from config.logger import logger


def test_club_administration_categories_e2e(club_admin_client, page):
    """
    E2E test for Club Administration categories.

    Steps:
    1. Create a new user.
    2. Log in as the new user.
    3. Create a parent category.
    4. Create a subcategory under the parent category.
    """
    logger.info("Starting club administration category creation e2e")

    # Generate user data and create a new user
    user_data = UserBuilder().build()
    new_user = club_admin_client.create_user(user_data)
    logger.info(f"User created: {new_user['email']}")

    # Initialize the login page and navigate to it
    login_page = LoginPage(page)
    login_page.navigate()
    assert login_page.is_page_displayed()

    # Log in with the newly created user
    login_page.login(new_user["email"], user_data["password"])
    assert login_page.is_user_logged_in()
    logger.info("User has successfully logged in")

    # Initialize the category page and navigate to it
    category_page = CategoryPage(page)
    category_page.go_to_category_page()

    # Create a new parent category
    parent_category_name = StringBuilder().generate_random_string()
    category_page.create_category(parent_category_name)
    assert category_page.is_category_present(parent_category_name)
    logger.info(f"Category created: {parent_category_name}")

    # Create a new subcategory under the parent category
    sub_category_name = StringBuilder().generate_random_string()
    category_page.create_sub_category(sub_category_name, parent_category_name)
    assert category_page.is_subcategory_present(sub_category_name, parent_category_name)
    logger.info(f"Subcategory created: {sub_category_name}")
