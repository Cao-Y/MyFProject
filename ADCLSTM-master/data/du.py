import pickle

file = open('char_embd.pickle','rb')
data = pickle.load(file)
numbers = open('model_input_word_data.txt','r')
i = numbers.readline()
# for i in numbers:
#     print(i)
print(i)
# print(data[0])
# print(data[1])
# print(data[2])
# print(len(data))
# for i in data :
#     print(i)
#     print(len(i))
file.close()
numbers.close()