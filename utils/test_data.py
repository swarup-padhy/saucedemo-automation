# utils/test_data.py


class Users:
    STANDARD    = {"username": "standard_user",  "password": "secret_sauce"}
    LOCKED      = {"username": "locked_out_user", "password": "secret_sauce"}
    PROBLEM     = {"username": "problem_user",    "password": "secret_sauce"}
    PERFORMANCE = {"username": "performance_glitch_user", "password": "secret_sauce"}


class CheckoutInfo:
    VALID = {"first_name": "John", "last_name": "Doe", "postal_code": "12345"}
    MISSING_FIRST  = {"first_name": "",     "last_name": "Doe", "postal_code": "12345"}
    MISSING_LAST   = {"first_name": "John", "last_name": "",    "postal_code": "12345"}
    MISSING_ZIP    = {"first_name": "John", "last_name": "Doe", "postal_code": ""}
