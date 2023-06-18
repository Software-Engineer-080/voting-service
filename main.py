auto_model = ''
voting_model = ''


def win_m(voting_model):
    big_model = ''
    big_count = 0
    for model in voting_model.split(";"):
        if model == '':
            break
        number = voting_model.count(model)

        if number > big_count:
            big_count = number
            big_model = model

    return big_model, big_count


def voting(auto_model, voting_model):
    print('Выберите модель из списка:', auto_model)
    print('Для подсчета голосов введите 0')

    choice = input('\nВаш выбор? ')

    while choice != '0':

        found = False
        info = ''
        for model in auto_model.split(";"):
            if model.startswith(choice):
                info = model
                found = True

        if found:
            voting_model += info + ';'
            print('Ваш голос принят!')
            choice = input('\nВаш выбор? ')

        else:
            print('Введите модель автомобиля из списка!')
            choice = input('\nВаш выбор? ')

    win_model, win_voting = win_m(voting_model)

    print('\nГолосование завершено!')
    print('Лучший автомобиль года', win_model)
    print('Количество голосов:', win_voting)


def main_menu(auto_model, voting_model):
    number = int(input('Сколько автомобилей участвует в голосовании?: '))

    for number_auto in range(number):
        auto = input(f'Введите модель {number_auto + 1} автомобиля: ')
        if auto not in auto_model:
            auto_model += auto + ';'
        else:
            print('Данная модель уже есть в биллютене!')

    print('\nГолосование создано!')
    voting(auto_model, voting_model)


print('Голосование за автомобиль года\n')

main_menu(auto_model, voting_model)
