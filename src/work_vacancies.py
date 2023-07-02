from abc import ABC, abstractmethod
import datetime


class Vacancies(ABC):

    @abstractmethod
    def __init__(self):
        pass


class VacanciesHH(Vacancies):

    def __init__(self, info):
        self.url = info['alternate_url']
        self.title = info['name']
        self.city = info['area']['name']
        if info['salary'] == None:
            self.salary = 'Зарплата не указана'
        else:
            self.salary = f"Зарплата {info['salary']['from']} {info['salary']['currency']}"
        self.date = self.date_convesion(info['created_at'])

    @staticmethod
    def date_convesion(data):
        data_format = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S%z')
        return f"Дата создания вакансии: {datetime.datetime.strftime(data_format, '%d %B %Y %H:%M:%S %Z')}"


class VacanciesSJ(Vacancies):

    def __init__(self, info):
        self.url = info['link']
        self.title = info['profession']
        self.city = info['town']['title']
        self.salary = f"Зарплата {info['payment_from']} {info['currency']}"
        self.date = self.date_convesion(info['date_published'])

    @staticmethod
    def date_convesion(data):
        return f"Дата создания вакансии: {datetime.datetime.fromtimestamp(data).strftime('%d %B %Y %H:%M:%S')}"
