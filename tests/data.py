import random


class Data:
    URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER_URL = f'{URL}register'
    FORGOT_PASSWORD_URL = f'{URL}forgot-password'
    LOGIN_URL = f'{URL}login'
    PERSONAL_CABINET_URL = f'{URL}account/profile'
    EMAIL = 'test123@tywt.com'
    PASSWORD = 'test123@tywt.com'
    INCORRECT_PASSWORD_ERROR = 'Некорректный пароль'

    def generate_name(self):
        return str(random.randint(100000, 1000000))

    def generate_email(self):
        return str(random.randint(1000, 1000000)) + '@ya12345.ru'

    def generate_correct_password(self):
        return random.randint(100000, 1000000)

    def generate_incorrect_password(self):
        return random.randint(1, 99999)
