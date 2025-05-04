import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[\W_]', password))  # \W matches non-alphanumeric

    # Scoring
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if number_criteria:
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if special_criteria:
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., !, @, #, $).")

    # Result
    if strength == 5:
        result = "Very Strong Password"
    elif strength >= 4:
        result = "Strong Password"
    elif strength >= 3:
        result = "Moderate Password"
    elif strength >= 2:
        result = "Weak Password"
    else:
        result = "Very Weak Password"

    return result, feedback

# Example usage
password = input("Enter your password to check: ")
result, feedback = assess_password_strength(password)

print(f"\nPassword Strength: {result}")
if feedback:
    print("Suggestions:")
    for tip in feedback:
        print(f"- {tip}")