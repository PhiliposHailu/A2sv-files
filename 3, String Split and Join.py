# split and join functions in python
def split_and_join(line):
    # write your code here
    a = "this is a string"
    a = a.split(" ")
    a = "-".join(a)
    return a
if __name__ == '__main__':
    line = str()
    result = split_and_join(line)
    print(result)
