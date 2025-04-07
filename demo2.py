from dotenv import load_dotenv
import os
from pathlib import Path

def clear_ENV():
    # Remove all environment variables loaded by dotenv
    for key in list(os.environ.keys()):
        if key in ['ENV', 'API_KEY', 'DB_USERNAME', 'DB_PASSWORD', 'DEBUG']:
            del os.environ[key]

def load_environment(env_profile):
    # Clear previously loaded environment variables
    clear_ENV()

    if env_profile in ['dev', 'prod']:
        env_file = Path(f"{env_profile}.env")
        if env_file.exists():
            load_dotenv(dotenv_path=env_file)
            print(f" Loading {env_profile} environment...")
        else:
            print(f" Environment file {env_file} not found. Using default environment.")
    else:
        env_file = Path(".env")
        if env_file.exists():
            load_dotenv(dotenv_path=env_file)
            print(" Loading default environment...")
        else:
            print("Default .env file not found.")

    # Display the loaded environment variables
    display_environment_variables()

def display_environment_variables():
    env = os.getenv('ENV')
    if env:
        print(f"Environment Variable Value: {env}")
    else:
        print("ENV not set")

    api_key = os.getenv('API_KEY')
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    debug = os.getenv('DEBUG')

    if api_key: print(f"API_KEY: {api_key}")
    if db_username: print(f"DB_USERNAME: {db_username}")
    if db_password: print(f"DB_PASSWORD: {db_password}")
    if debug: print(f"DEBUG: {debug}")
    print("\n")

# Test loading environments
load_environment('dev')
load_environment('prod')
load_environment('test')