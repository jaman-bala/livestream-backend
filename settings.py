from envparse import Env

env = Env()


REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://superuser:ZAQ12345tgb@0.0.0.0:5432/unaa_db",
)
# # APP_PORT = env.int("APP_PORT")
#
#
# TEST_DATABASE_URL = env.str(
#     "TEST_DATABASE_URL",
#     default="postgresql+asyncpg://polls_test:password-test@0.0.0.0:5433/polls_test",
# )
# REAL_DATABASE_URL = env.str(
#     "REAL_DATABASE_URL", default="sqlite+aiosqlite:///./my_database.db"
# )

# TEST_DATABASE_URL = env.str(
#     "REAL_DATABASE_URL", default="sqlite+aiosqlite:///./test_database.db"
# )

SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
ALGORITHM: str = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
# SENTRY_URL: str = env.str("SENTRY_URL")
