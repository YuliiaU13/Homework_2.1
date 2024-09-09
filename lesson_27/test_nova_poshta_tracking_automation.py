import pytest
from lesson_27.nova_poshta_tracking import NovaPoshtaTracking


@pytest.mark.parametrize(
    "tracking_number, expected_status", [
        ("20450982447375", "Отримана"),
        ("20450982449765", "Відправлення отримано. Грошовий переказ видано одержувачу."),
        ("hhhhhhhhhhh", "Ми не знайшли посилку за таким номером. Можливо, вона ще не передана для відправлення, "
                        "або номер некоректний. Перевірте, чи відповідає вказаний номер можливому формату: "
                        "59500000031324 або AENM0002497278NPI.")
    ]
)
@pytest.mark.nova_poshta
def test_nova_poshta_tracking_automation(tracking_number, expected_status, driver):
    tracker = NovaPoshtaTracking(driver)

    tracker.open_tracking_page()
    tracker.enter_tracking_number(tracking_number)
    actual_status = tracker.get_status()

    assert actual_status == expected_status, f"Expected status: {expected_status}, but got: {actual_status}"
    print(f'Test passed! Actual_status: "{actual_status}".')
