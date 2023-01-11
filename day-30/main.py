#FileNotFound

try:
    file = open('a_file_that_does_not_exist.txt')
except FileNotFoundError:
    open('a_file_that_does_not_exist.txt', 'w')