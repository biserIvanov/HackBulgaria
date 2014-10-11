import sys
from random import randint


def file_reader(name):
    file = open(name, "r")
    content = file.read()
    file.close()
    return content


def file_priner(files):
    for text_file_name in files:
        print(file_reader(text_file_name))


def file_creator(name, n):
    content = str(randint(1, 1000))*n
    file = open(name, 'w')
    file.write("  ".join(content))
    file.close()


def sum_numbers(filename):
    result = 0
    file = open(filename, "r")
    content = file.read().split()
    for element in content:
        result += int(element)
    print (result)


def file_concatenation(filenames):
    result = ""
    for text_file_name in filenames:
        result += file_reader(text_file_name)
        file = open('MEGATRON.txt', 'w')
        file.write(result)
    file.close()


def wc(command, filename):
    result = 0
    options = ('chars', 'words', 'lines')
    a = file_reader(filename)
    if command == options[0]:
        for char in a:
            if char != " ":
                result += 1
        return result
    elif command == options[1]:
        for char in a:
            if char == " ":
                result += 1
        return result + 1
    elif command == options[2]:
        with open(filename) as foo:
            lines = len(foo.readlines())
        return lines


def main():
    #file_priner(sys.argv[1:])
    #file_creator('biso.txt', 4)
    #sum_numbers('biso.txt')
    #file_concatenation(sys.argv[1:])
    print (wc('lines', 'biso.txt'))

if __name__ == '__main__':
    main()
