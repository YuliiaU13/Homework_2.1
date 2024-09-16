
def test_user_registration(registration_page, signed_in_page, driver, name, last_name, email, password):

    registration_page.open_registration_form()
    registration_page.sign_in(name, last_name, email, password)
    signed_in_page.verify_page_loaded()
    signed_in_page.verify_empty_garage_message(email)
