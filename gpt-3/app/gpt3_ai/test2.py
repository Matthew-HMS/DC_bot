import json

file = open("history.txt", "r")
contents = file.read()
lines = contents.split("\n")
history = []

for line in lines:
    mes = json.loads(line)
    history.append(mes)

print(lines)
print(history)