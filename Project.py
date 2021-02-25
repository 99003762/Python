import re


class Find:
    def __init__(self, itr):
        self.itr = itr

    def my_function(self):
        for i in range(self.itr):
            count = 0
            line = 0
            word = str(input("Enter word {} : ".format(i+1)))
            with open("{}.txt".format(word), 'w') as file_answer:
                with open('Input_file.txt', 'rt') as file_info:
                    for file_line in file_info:
                        line += 1
                        file_line = re.sub(r"\W", " ", file_line)
                        k = file_line.split()
                        for j in range(len(k)):
                            if word.lower() == k[j].lower():
                                n= line
                                if j > 0 and j < (len(k)-1):
                                    count += 1
                                    str1 = ('\n'+k[j-1]+" "+k[j]+" "+k[j+1])
                                    file_answer.write((str1+" --------(IS FOUND AT): "+str(n)))
                                else:
                                    file_answer.write('\n'+k[j]+" --------(IS FOUND AT): "+ str(n))
                                    count += 1
            print("total line count", count)
            f = open("{}.txt".format(word), 'a')
            f.write('\n'+"Total number of occurrence:"+str(count))


p1 = Find(int(input("Enter the number of words: ")))
p1.my_function()
