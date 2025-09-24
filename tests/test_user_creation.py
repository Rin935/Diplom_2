import allure
from helpers.api_requests import get_user_data, register_user, login_user
from data.data import USER_WITH_MISSING_FIELDS, USER


@allure.feature("Создание пользователя")
class TestUserCreation:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, setup_unique_user):
        user_data = setup_unique_user

        auth_response = login_user(user_data)
        assert auth_response.status_code == 200, \
            f"Ошибка авторизации: {auth_response.status_code}. Ответ: {auth_response.text}"

        auth_token = auth_response.json().get("accessToken")
        token = auth_token.split(' ')[1] if ' ' in auth_token else auth_token
        assert token, "Toкен отсутствует или имеет неверный формат"

        response = get_user_data(token)

        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}. Ответ: {response.text}"

        assert response.json().get("user", {}).get("email") == user_data["email"], \
            f"Ожидался emaiL: {user_data['email']}, получен: {response.json().get('user', {}).get('email')}"

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        response: register_user(USER)

        assert response.status_code == 403, \
            f"Ожидался код 403, получен {response.status_code}. Ответ: {response.text}"
        expected_response = {
            "success": False,
            "message":"User already exists"}

        assert response.json() == expected_response, \
            f"Ожидался ответ {expected_response}, получен:{response.json()}"

    REQUIRED_FIELDS = ["email", "password", "name"]

    @pytest.mark.parametrize("field", REQUIRED_FIELDS)
    @allure.title("Создание пользователя с отсутствующим обязательным полем: {field} (missing)")
    def test_create_user_missing_field(field):
        user = USER.copy()
        user.pop(field, None)

        response = register_user(user)

        assert response.status_code == 403, \
            f"Ожидался код 403, получен {response.status_code}. Ответ:{response.text}"
        expected_response = {
            "success": False,
            "message": "Email, password and name are required fields"
        }
        assert response.json() == expected_response, \
            f"Ожидался ответ {expected_response}, получен:{response.json()}"

    @pytest.mark.parametrize("field", REQUIRED_FIELDS)
    @allure.title("Создание пользователя с пустым обязательным полем: {field} (empty_string)")
    def test_create_user_empty_field(field):
        user = USER.copy()
        user[field] = ""

        response = register_user(user)

        assert response.status_code == 403, \
            f"Ожидался код 403, получен {response.status_code}. Ответ:{response.text}"
        expected_response = {
            "success": False,
            "message": "Email, password and name are required fields"
        }
        assert response.json() == expected_response, \
            f"Ожидался ответ {expected_response}, получен:{response.json()}"