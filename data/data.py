URL = "https://stellarburgers.nomoreparties.site/"

ENDPOINTS = {
    "register_user": f"{URL}/api/auth/register",
    "login": f"{URL}/api/auth/login",
    "logout": f"{URL}/api/auth/logout",
    "token": f"{URL}/api/auth/token",
    "user": f"{URL}/api/auth/user",
    "orders": f"{URL}/api/orders"
}

USER = {
    "email": "ivanivanov@gmail.com",
    "password": "Fdjklwekls321",
    "name": "IvanIvanov"
}

USER_WITH_MISSING_FIELDS = {
    "email": "user01@gmail.com",
    "password": "",
    "name": "User01"
}

INVALID_USER = {
    "email": "user02@gmail.com",
    "password": "invalid_password"
}

INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d"
    "61c0c5a71d1f82001bdaaa6f"
    "61c0c5a71d1f82001bdaaa70"
    "61c0c5a71d1f82001bdaaa71"
]