from dotenv import load_dotenv


load_dotenv()

pytest_plugins = [
    'e2e_testing.fixtures.page',
    'e2e_testing.fixtures.user_auth'
]

