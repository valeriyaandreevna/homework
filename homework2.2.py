while True:
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    print(my_list)
    number = int(input('введите число из списка выше: '))
    if number > 0:
        print('good')
    else:
        print('не правильно набран номер...')
        break