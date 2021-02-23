import re
count = 0
word = str(input())
OUTPUT = []
line = 0
pattern = re.compile(word, re.I)

with open('Input_file.txt', 'rt') as file_info:
    for file_line in file_info:
        line += 1
        if pattern.search(file_line) is not None:
            OUTPUT.append((line, file_line.rstrip('\n')))
    for answer in OUTPUT:
        count += 1
        with open('OUTPUT.txt', 'a') as file_answer:
            file_answer.writelines(str(count)+' :')
            file_answer.writelines(answer[1]+'\n')
print(count)
