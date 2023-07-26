#Задача - написать программу заменяющую слово из строки на номер слова в приложенном файле

def read2list(file):
    file = open(file, 'r', encoding='utf-8')
    file_lines = file.readlines()
    file_lines = [line.rstrip('\n') for line in file_lines]
    file.close()
    return file_lines
file_lines = read2list('russian.txt')
numbers = list(range(1, len(file_lines)))
file_dict = dict(zip(numbers, file_lines))

str_in = str(input())
result = [x for x in file_lines if x in str_in.split()]
print(result)

# for i in result:
#     if i == file_dict.values():
#         result.append(i, file_dict.keys())
#     print(result)
