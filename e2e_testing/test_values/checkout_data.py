tests_with_correct_checkout = [
    ("Ivan", "Ivanov", "123456", "Checkout: Complete!", "No problems")
]

tests_with_incorrect_checkout = [
    ("", "Ivanov", "123456", "Error: First Name is required", "The error was not found"),
    ("Ivan", "", "123456", "Error: Last Name is required", "The error was not found"),
    ("Ivan", "Ivanov", "", "Error: Postal Code is required", "The error was not found")
]