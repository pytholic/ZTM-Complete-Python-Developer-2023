"""
email
password: 
    1. Can be 8 characters long
    2. Can contain letters, numbers and $@%#
    3. Ends with a number
"""

import re

email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
pass_pattern = re.compile(r"[a-zA-Z0-9@#$%]{8,}\d$")

email = "b@b.com"
email2 = "asas"
password = "ahgshag121#$5"
password2 = "ahgs12"

a = email_pattern.search(email)
b = pass_pattern.fullmatch(password)
c = email_pattern.search(email2)
d = pass_pattern.fullmatch(password2)
print(a)
print(b)
print(c)
print(d)
