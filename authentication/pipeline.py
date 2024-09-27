

def log_social_token(backend, response, *args, **kwargs):
    # Логируем данные токена или информацию о пользователе
    token = response.get('access_token')
    if token:
        print(f"VK Access Token: {token}")
