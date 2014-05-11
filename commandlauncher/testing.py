def main():
    object = ""
    second_method(object)
    print(object)


def second_method(object):
    object += ' Sofia'

if __name__ == '__main__':
    main()