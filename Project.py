import re
count = 0
software = []
line = 0
pattern = re.compile("software", re.I)

with open('Input_file.txt', 'rt') as file_info:
    for file_line in file_info:
        line += 1
        if pattern.search(file_line) != None:
            software.append((line, file_line.rstrip('\n')))
    for answer in software:
        count += 1
        with open('software.txt', 'a') as file_answer:
            file_answer.writelines(str(count)+' :')
            file_answer.writelines(answer[1]+'\n')
print(count)


license = []
count = 0
pattern = re.compile("license", re.I)

with open('Input_file.txt', 'rt') as file_info:
    for file_line in file_info:
        line += 1
        if pattern.search(file_line) != None:
            license.append((line, file_line.rstrip('\n')))
    for answer in license:
        count += 1
        with open('license.txt', 'a') as file_answer:
            file_answer.writelines(str(count)+' :')
            file_answer.writelines(answer[1]+'\n')

print(count)