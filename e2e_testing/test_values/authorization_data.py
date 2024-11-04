tests_with_incorrect_data = [
    # тест с заблокированным пользователем
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),

    # тест с неккоректными логином и паролем
    ("wrong_login", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),

    # тест с неккоректным логином и корректным паролем
    ("wrong_login", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),

    # тест с корректным логином и некорректным паролем
    ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service")
]

tests_with_empty_data = [
    # тест с пустыми полями для логина и пароля
    ("", "", "Epic sadface: Username is required"),

    # тест с пустым полем для логина и корректным для пароля
    ("", "secret_sauce", "Epic sadface: Username is required"),

    # тест с логином и пустым полем для пароля
    ("standard_user", "", "Epic sadface: Password is required")
]