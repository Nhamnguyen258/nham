from functools import lru_cache


class Settings:
    app_name: str = "FastAPI"
    database_url: str = "mysql+aiomysql://dbuser:dbpassword@mysql:3306/mydatabase"

    access_token_secret: str = "nhamnguyen"
    access_token_expire_minutes: int = "60"

    refresh_token_secret: str = "nhamnguyen12"
    refresh_token_expire_minutes: int = 60


@lru_cache()
def get_settings():
    return Settings()
