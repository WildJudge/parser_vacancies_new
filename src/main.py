
def main():
    while True:

        # выбор ресурса
        site_list = ['hh.ru', 'superjob.ru']

        # запрос
        user_request = input("Введите Ваш зопрос по поиску вакансий: ")

        # Количество вакансий
        quantity = int(input("Введите количество вакансий для вывода в топ: "))

        # Фильтр запроса
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()


if __name__ == "__main__":
    main()
