import random
import string

#1. First, create a secure random generator instance
secure_generator = random.SystemRandom()

# 2. Define the character set for the OTP (digits 0 - 9)
otp_characters = string.digits

# 3. Generate the OTP by choosing 6 characters from the set
otp = ''.join(secure_generator.choice(otp_characters) for _ in range(6))

print(f"Your secure one-time password is: {otp}")