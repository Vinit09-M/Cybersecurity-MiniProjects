import re

def check_password_strength(password: str) -> str:
    """
    Returns password strength as 'Weak', 'Medium', or 'Strong'.
    Rules checked:
      - Length >= 8
      - At least one digit
      - At least one uppercase
      - At least one lowercase
      - At least one symbol from common set
    """
    length_ok = len(password) >= 8
    digit_ok = re.search(r'\d', password) is not None
    upper_ok = re.search(r'[A-Z]', password) is not None
    lower_ok = re.search(r'[a-z]', password) is not None
    symbol_ok = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_ok, digit_ok, upper_ok, lower_ok, symbol_ok])

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

if __name__ == "__main__":
    try:
        pwd = input("Enter a password to check: ")
        print("Password Strength:", check_password_strength(pwd))
    except KeyboardInterrupt:
        print("\nCancelled.")
