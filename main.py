
import random
import smtplib


# Create SMTP Server instance with gmail.com
server = smtplib.SMTP('smtp.gmail.com', 587)

# Secure the Server using TLS
server.starttls()

# Login to mail server using App Password
# Replace  'userid@gmail.com' with actual email ID
# And 'password' with actual credentials
server.login('userid@gmail.com', 'password')

# generating random OTP
otp = ''.join([str(random.randint(0,9)) for i in range(6)])
msg = 'Hello, Your OTP is ' + str(otp)

# sending Email
# replace 'userid@example.com' with sender Email ID
# And 'receiverid@gmail.com' with receiver Email ID
server.sendmail('userid@gmail.com', 'receiverid@gmail.com', msg)
server.quit()

# Input OTP to Varify
input_otp = input("Enter the 2FA OTP received via E-Mail: ")
if otp == input_otp:
    print("VERIFIED!!")
else:
    print("Invalid OTP")

