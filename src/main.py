from src.utils import WorkToUser


def get_user(player, count):
    """Выполняет запрос пользователя"""

    player.choice_site()  # выбор ресурса
    player.get_request()  # запрос
    player.choice_city()  # Выбор региона для поиска вакансий
    player.quantity_vacancies()  # Количество вакансий

    print(f'\n{player}')  # Показывает запрос

    player.work_api(count)


def repeat_get(player):
    """Повторяет запрос пользователя"""

    while True:
        try:
            choice_user = int(input('\n1 - Да\n2 - Нет\nХотите повторить запрос?'))
            if choice_user == 1:
                get_user(player, 1)
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Некорректный ввод")


def find_get(player):
    """Ищет дополнительный запрос пользователя"""

    while True:
        try:
            choice_user = int(input('\n1 - Да\n2 - Нет\nХотите найти ключевое слово в вакансиях?'))
            if choice_user == 1:
                data = input('Введите Ваш запрос: ')
                print(player.find_word(data))
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Некорректный ввод")


def main():

    while input('Нажмите Enter, чтобы начать: ') != '':
        continue

    # Очищаем файл
    f = open('vacancies.json', 'w')
    f.close()

    print('\nПриветствую Вас! Подготовим Ваш запрос по поиску вакансий.')

    player = WorkToUser()

    get_user(player, 0)
    repeat_get(player)
    WorkToUser.sort_all()
    find_get(player)

    print('\nСписок вакансий отсортированных по зарплате Вы можете посмотреть в файле - vacancies.json')
    print('\nХорошего дня!')


if __name__ == "__main__":
    main()
