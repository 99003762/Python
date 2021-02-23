import re
cycle = int(input("Enter the number of words to search :"))
for i in range(0, cycle):
    count = 0
    line = 0
    OUTPUT = []
    word = str(input("Enter word {} :".format(i+1)))
    pattern = re.compile(word, re.I)
    with open('Input_file.txt', 'rt') as file_info:
        for file_line in file_info:
            line += 1
            if pattern.search(file_line) is not None:
                OUTPUT.append((line, file_line.rstrip('\n')))
        for answer in OUTPUT:
            count += 1
            with open("{}.txt".format(word), 'a') as file_answer:
                file_answer.writelines(str(count)+' :')
                file_answer.writelines(answer[1]+'\n')
    print(count)
