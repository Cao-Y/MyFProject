import pkuseg
list =['01','02','03','04','05','06','07','08','09','10','11','12']
if __name__ == '__main__':
    for num in list:
        inPath = num+'.txt'
        outPath = num+'_pku.txt'
        print(inPath)
        print(outPath)
        pkuseg.test(inPath, outPath, model_name='news', nthread=10)