"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json
є валідними json. результат для невалідного файлу виведіть через логер
на рівні еррор у файл json__<your_second_name>.log
"""

# import json

# file_1 = 'localizations_en.json'
# try:
#     with open(file_1, 'r') as f:
#         data_1 = json.load(f)
#     print(type(data_1))
#     print(data_1)
# except json.JSONDecodeError as e:
#     print("JSON Decode Error:", e)
#
# file_2 = 'localizations_ru.json'
# try:
#     with open(file_2, 'r') as f:
#         data_2 = json.load(f)
#     print(type(data_2))
#     print(data_2)
# except json.JSONDecodeError as e:
#     print("JSON Decode Error:", e)
#
# file_3 = 'login.json'
# try:
#     with open(file_3, 'r') as f:
#         data_3 = json.load(f)
#     print(type(data_3))
#     print(data_3)
# except json.JSONDecodeError as e:
#     print("JSON Decode Error:", e)
#
#
# file_4 = 'swagger.json'
# try:
#     with open(file_4, 'r') as f:
#         data_4 = json.load(f)
#     print(type(data_4))
#     print(data_4)
# except json.JSONDecodeError as e:
#     print("JSON Decode Error:", e)


import json
import logging
import pytest


logging.basicConfig(
    filename='json__udovichenko.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s:%(message)s',
    force=True
)
logger = logging.getLogger("validate_json")


def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        return True
    except json.JSONDecodeError as e:
        logger.error(f"JSON Decode Error in file {file_path}: {e}")
        return False


@pytest.mark.parametrize('file', ['localizations_en.json', 'localizations_ru.json',
                                  'login.json', 'swagger.json'])
def test_validate_json(file):
    result = validate_json(file)
    print(f"{file}: {'Valid' if result else 'Invalid'}")
    assert result in [True, False], f"Validation failed for {file}"
