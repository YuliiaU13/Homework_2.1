from lesson_28.qauto2_pages.signed_in_page import SignedInPage
from lesson_28.qauto2_pages.validators import RegistrationValidator


def test_user_registration(registration_page, signed_in_page, name, last_name, email, password):
    validator = RegistrationValidator()

    registration_page.open_registration_form()
    registration_page.sign_in(name, last_name, email, password)

    signed_in_page.verify_page_loaded()

    empty_garage_message = signed_in_page.get_empty_garage_message()
    validator.verify_empty_garage_message(empty_garage_message)
    validator.print_registration_success(email)
