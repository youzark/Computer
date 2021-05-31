file = open("./count","r")
record = file.readlines()
sum = 0
for re in record:
    sum += int(re.split()[1])

print(sum)
