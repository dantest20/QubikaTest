from pages.base_page import BasePage


class CategoryPage(BasePage):
    """
    Page object model for the Category Page.
    """

    # Locators
    ADD_CATEGORY_BTN = 'text=Adicionar'
    ADD_CATEGORY_INPUT = '#input-username'
    SUBMIT_BTN = 'text=Aceptar'
    TABLE_ROWS = 'tbody tr'
    TABLE_DATA = 'td'
    NEXT_PAGE_BTN = 'a.page-link >> text=Next'
    ADD_SUBCATEGORY_BTN = 'label:has-text("Es subcategoria?")'
    PARENT_CATEGORY_INPUT = 'input[aria-autocomplete="list"]'
    PAGE_LINK_BTN = ".page-item"
    ADD_SUBCATEGORY_SUCCESS_MESSAGE = 'text=Tipo de categoría adicionada satisfactoriamente'

    # Actions

    def create_category(self, name):
        """
        Create a new category.

        Args:
            name (str): Name of the category to create.
        """
        self.get_create_category_btn().click()
        self.page.fill(self.ADD_CATEGORY_INPUT, name)
        self.page.click(self.SUBMIT_BTN)

    def create_sub_category(self, sub_category_name, parent_category_name):
        """
        Create a new subcategory under a parent category.

        Args:
            sub_category_name (str): Name of the subcategory to create.
            parent_category_name (str): Name of the parent category.
        """
        self.get_create_category_btn().click()
        self.get_create_sub_category_check().click()
        self.page.fill(self.ADD_CATEGORY_INPUT, sub_category_name)
        self.get_parent_category_intput().fill(parent_category_name)
        self.select_autocomplete_option(parent_category_name)
        self.page.click(self.SUBMIT_BTN)

        # Wait for the success message to appear and disappear
        self.page.wait_for_selector(self.ADD_SUBCATEGORY_SUCCESS_MESSAGE)
        self.page.wait_for_selector(self.ADD_SUBCATEGORY_SUCCESS_MESSAGE, state='hidden')

    def select_autocomplete_option(self, option_text):
        """
        Select an option from the autocomplete dropdown.

        Args:
            option_text (str): The text of the option to select.
        """
        option_locator = self.page.locator('span', has_text=option_text)
        option_locator.wait_for()
        option_locator.click()

    # Getters

    def get_parent_category_intput(self):
        """
        Get the parent category input field locator.

        Returns:
            Locator: The locator for the parent category input field.
        """
        parent_category_input = self.page.locator(self.PARENT_CATEGORY_INPUT)
        parent_category_input.wait_for()
        return parent_category_input

    def get_create_sub_category_check(self):
        """
        Get the create subcategory checkbox locator.

        Returns:
            Locator: The locator for the create subcategory checkbox.
        """
        btn = self.page.locator(self.ADD_SUBCATEGORY_BTN)
        btn.wait_for()
        return btn

    def get_create_category_btn(self):
        """
        Get the create category button locator.

        Returns:
            Locator: The locator for the create category button.
        """
        add_category_btn = self.page.locator(self.ADD_CATEGORY_BTN)
        add_category_btn.wait_for()
        return add_category_btn

    def is_category_present(self, category_name):
        """
        Check if a category is present in the table.

        Args:
            category_name (str): The name of the category to check.

        Returns:
            bool: True if the category is present, False otherwise.
        """
        page_number = 1
        while True:
            # Wait until the current page is loaded
            self.wait_until_table_page_is_loaded(page_number)

            rows_locator = self.page.locator(self.TABLE_ROWS)
            row_count = rows_locator.count()

            for i in range(row_count):
                cell_locator = rows_locator.nth(i).locator(self.TABLE_DATA).nth(0)
                cell_locator.wait_for()
                if cell_locator.inner_text() == category_name:
                    return True

            next_button_locator = self.page.locator(self.NEXT_PAGE_BTN)
            if next_button_locator.is_enabled():
                next_button_locator.click()
                page_number += 1
            else:
                break

        return False

    def wait_until_table_page_is_loaded(self, page_number):
        """
        Wait until the table page with the specified number is loaded.

        Args:
            page_number (int): The page number to wait for.
        """
        self.page.wait_for_selector(f'li.page-item.active a.page-link:has-text("{page_number}")')

    def is_subcategory_present(self, subcategory_name, parent_category_name):
        """
        Check if a subcategory is present under a specific parent category.

        Args:
            subcategory_name (str): The name of the subcategory to check.
            parent_category_name (str): The name of the parent category.

        Returns:
            bool: True if the subcategory is present under the parent category, False otherwise.
        """
        rows_locator = self.page.locator(self.TABLE_ROWS)
        row_count = rows_locator.count()

        for i in range(row_count):
            subcategory_cell_locator = rows_locator.nth(i).locator(self.TABLE_DATA).nth(0)
            parent_category_cell_locator = rows_locator.nth(i).locator(self.TABLE_DATA).nth(1)

            subcategory_cell_locator.wait_for()
            parent_category_cell_locator.wait_for()

            if (subcategory_cell_locator.inner_text() == subcategory_name
                    and parent_category_cell_locator.inner_text() == parent_category_name):
                return True

        return False
