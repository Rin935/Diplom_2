from data.data import INVALID_USER, USER
import allure


@allure.feature('Логин пользователя')
class TestUserLogin:

    @allure.title('Вход под существующим пользователем')
    def test_login_successful(self, login_user):
        with allure.step('Отправить запрос на вход с существующими данными'):
            response = login_user(USER)

        with allure.step('Проверить успешный ответ'):
            assert response.status_code == 200, \
                f"Ожидался код 200, получен {response.status_code}. Ответ: {response.text}"
            response_json = response.json()
            assert response_json.get("success")is True, \
                f"Ожидался 'success': True, получен {response_json.get('success')}"
            assert "accessToken" in response_json, \
                f"В ответе отсутствует accessToken. Ответ: {response_json}"
            assert "refreshToken" in response_json, \
                f"В ответе отсутствует refreshToken. Ответ: {response_json}"
            assert "user" in response_json, \
                f"В ответе отсутствуют данные пользователя. Ответ: {response_json}"

    @allure.title('Вход с неверным логином и паролем')
    def test_login_invalid_fields(self, login_user):
        with allure.step('Отправить запрос на вход с неверными данными'):
            response = login_user(INVALID_USER)

        with allure.step('Проверить ошибку авторизации'):
            assert response.status_code == 401, \
                f"Ожидался код 401, получен {response.status_code}. Ответ: {response.text}"
            response_json = response.json()
            assert response_json.get("success") is False, \
                f"Ожидался 'success': False, получен {response_json.get('success')}"
            assert response_json.get("message") == "email or password are incorrect", \
                f"Ожидалось сообщение 'email or password are incorrect', получено: {response_json.get("message")}"