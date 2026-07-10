# ============================================
# Password Strength Checker
# ============================================

print("      PASSWORD STRENGTH ANALYZER")


password = input("Enter password to analyze: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

score = 0

for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    elif not char.isalnum():
        has_symbol = True

common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "admin123",
    "welcome",
    "abc123",
    "letmein"
]

# Length
if length >= 8:
    score += 2

# Uppercase
if has_upper:
    score += 2

# Lowercase
if has_lower:
    score += 2

# Digit
if has_digit:
    score += 2

# Symbol
if has_symbol:
    score += 2

if password.lower() in common_passwords:
    score = 0

if score > 10:
    score = 10

if score <= 3:
    strength = "WEAK"

elif score <= 7:
    strength = "MEDIUM"

else:
    strength = "STRONG"

print("\nSuggestions")

if length < 8:
    print("- Use at least 8 characters.")

if not has_upper:
    print("- Add at least one uppercase letter.")

if not has_lower:
    print("- Add lowercase letters.")

if not has_digit:
    print("- Add at least one number.")

if not has_symbol:
    print("- Add at least one special character (!,@,#,$,%,&,*)")

if password.lower() in common_passwords:
    print("- Avoid using common passwords.")

if (
    length >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_symbol
    and password.lower() not in common_passwords
):
    print("- Excellent! Your password follows good security practices.")

print("\n" + "=" * 45)
print("FINAL RESULT")
print("=" * 45)

print(f"Password Strength : {strength}")
print(f"Security Score    : {score}/10")

print("=" * 45)
print("Analysis Complete.")