import re

re_n = re.compile(r"^(\d){3,5}$")
print(re_n.match("12345456"))