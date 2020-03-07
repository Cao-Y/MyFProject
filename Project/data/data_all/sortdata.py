dict ={"时尚":'01','科技':'02', '社会':'03', '娱乐':'04','家居':'05','财经':'06',
       '教育':'07', '房产':'08','时政':'09','游戏':'10','体育':'11','股票':'12'}
# print(dict['时尚'])

inputfile = open("../../item.txt", 'r', encoding='utf-8')

def sortfile():
       for str in inputfile.readlines():
              string = str[0]+str[1]
              # print(string)
              print(dict[string])
              # print(str[3:])
              out = outfile(dict[string]+'.txt')
              out.write(str[3:])

def outfile(path):
       out = open(path,'a',encoding='utf-8')
       return out

sortfile()
print("end")
inputfile.close()
