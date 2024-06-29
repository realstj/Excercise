import re

# catching groups
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")
rearrange_name("Lovelace, Ada")
rearrange_name("Ritchie, Dennis")

print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

