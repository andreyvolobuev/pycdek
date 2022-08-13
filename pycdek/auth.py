import entities
import endpoints
from pathlib import Path


class TokenManager:
    @staticmethod
    def _get_tmp_token_path(
        dir_name: str = "/tmp/pycdek", file_name: str = "_token.json"
    ) -> Path:
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        return Path(dir_name, file_name)

    @staticmethod
    def _read_token_from_file() -> None:
        tmp_file = TokenManager._get_tmp_token_path()
        if tmp_file.exists():
            with open(tmp_file) as file:
                token = entities.AccessToken.parse_raw(file.read())
                if token.is_valid():
                    return token

    @staticmethod
    def write_token_to_file(token: entities.AccessToken) -> None:
        tmp_file = TokenManager._get_tmp_token_path()
        tmp_file.touch()
        with open(tmp_file, "w") as file:
            file.write(token.json())

    @staticmethod
    def gen_new_token(credentials: entities.ClientCredentials) -> entities.AccessToken:
        """
        @param credentials: Объект логина и пароля интеграции СДЭК
        """
        endpoint = endpoints.Auth()
        return endpoint(params=credentials)

    @staticmethod
    def get_token(credentials: entities.ClientCredentials) -> entities.AccessToken:
        """
        Чтобы не делать запрос к СДЭКу каждый раз, когда нам нужен токен,
        мы будем сохранять его во временный файл и брать от туда до тех пор,
        пока не истечет срок его валидности.

        @param credentials: Объект логина и пароля интеграции СДЭК
        """
        token = TokenManager._read_token_from_file()
        if not token:
            token = TokenManager.gen_new_token(credentials)
            TokenManager.write_token_to_file(token)
        return token
