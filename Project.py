import re


class person:
    def __init__(self, cycle):
        self.cycle = cycle

    def myfunc(self):
        for i in range(0, self.cycle):
            count = 0
            line = 0
            str1 = 0
            word = str(input("Enter word {} :".format(i+1)))
            with open("{}.txt".format(word), 'w') as file_answer:
                with open('Input_file.txt', 'rt') as file_info:
                    for file_line in file_info:
                        line += 1
                        file_line = re.sub(r"\W", " ", file_line)
                        L = (file_line).split()
                        l = list(L)
                        for j in range(len(l)):
                            if word.lower() == l[j].lower():
                                if j > 0 and j < (len(l)-1):
                                    count += 1
                                    str1 = (l[j-1]+" "+l[j]+" "+l[j+1]+'\n')
                                    file_answer.writelines(str(count)+' :')
                                    file_answer.write(str1)
                                    print(str1)
                                else:
                                    file_answer.writelines(str(count+1)+' :')
                                    file_answer.write(l[j]+'\n')
                                    count += 1
            print("total line count", count)
            f = open("{}.txt".format(word), 'a')
            f.write("Total number of occurence:"+str(count))
p1 = person(int(input("Enter the number of words")))
p1.myfunc()
