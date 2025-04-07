default_config = {
    "DEBUG": False,
    "DATABASE_URL": "sqlite://:memory:",
    "CACHE_TIMEOUT": 300,
    "LOG_LEVEL": "INFO",
}

dev_config = {
    "DEBUG": True,
    "DATABASE_URL": "postgresql://localhost/dev_db",
    "LOG_LEVEL": "DEBUG",
}

prod_config = {
    "DATABASE_URL": "postgresql://localhost/prod_db",
    "CACHE_TIMEOUT": 600,
}

static_config = default_config | dev_config
print("Static Configuration:", static_config)
