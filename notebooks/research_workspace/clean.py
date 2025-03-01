import re
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
with open('tree.txt', 'r') as file:
    content = file.read()
clean_content = ansi_escape.sub('', content)
with open('tree.txt', 'w') as file:
    file.write(clean_content)