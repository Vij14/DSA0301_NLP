import re
text = "Hello, my email is example@email.com, and my phone number is 123-456-7890."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

email_matches = re.findall(email_pattern, text)
phone_matches = re.findall(phone_pattern, text)

if email_matches:
    print("Email addresses found:")
    for email in email_matches:
        print(email)

if phone_matches:
    print("Phone numbers found:")
    for phone in phone_matches:
        print(phone)
