class RegistrationValidator:
    def verify_empty_garage_message(self, actual_message, expected_message="You don’t have any cars in your garage"):
        assert actual_message == expected_message, "Empty garage message did not match"

    def print_registration_success(self, email):
        print(f' User {email} is registered!')
