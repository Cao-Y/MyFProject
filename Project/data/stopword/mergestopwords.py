lines = open('stopword.txt', 'r', encoding='utf-8')
newfile = open('stopwords.txt', 'w', encoding='utf-8')
new = []
for line in lines.readlines():
    if line not in new:
        new.append(line)
        newfile.writelines(line)

lines.close()
newfile.close()