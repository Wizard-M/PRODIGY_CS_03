import re

# Function to assess password strength
def assess_password_strength(password):
    # Initial score
    score = 0
    feedback = []

    # Criteria for scoring
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine strength level based on score
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback to the user
    return strength, feedback

# Main function to get user input and assess password
def main():
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)

    print(f"Password strength: {strength}")
    if feedback:
        print("Feedback:")
        for message in feedback:
            print(f"- {message}")

# Run the main function
if __name__ == "__main__":
    main()
