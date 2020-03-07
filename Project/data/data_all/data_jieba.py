# encoding=utf-8
import jieba


list =['01','02','03','04','05','06','07','08','09','10','11','12']

def jiebaSeparate(str):
    #print("Start separate")
    out = jieba.cut(str)
    return out

def infile(path):
    inf = open(path,'r',encoding='utf-8')
    return inf

def outfile(path):
    out = open(path, 'w', encoding='utf-8')
    return out

def sort():
    stopwords = [line.strip() for line in open('../stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords

for num in list:
    inPath = num+'.txt'
    outPath = num+'_jieba.txt'

    infi = infile(inPath)
    out = outfile(outPath)
    try:
        sen = infi.readline()
        stopwords = sort()
        while sen:
            afterSep = jiebaSeparate(sen)
            outstr = ''
            # 去停用词
            for word in afterSep:
                if word not in stopwords:
                    if word != '\t':
                        outstr += word
                        outstr += " "
            out.write(outstr)
            #print("写入中")
            sen = infi.readline()
    finally:
        infi.close()
        out.close()
    print(num + "is ok")




