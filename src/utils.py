import datetime
import json
import os
from abc import ABC, abstractmethod
from pprint import pprint

import requests as requests


class WorkApi(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Vacancies(ABC):

    @abstractmethod
    def __init__(self):
        pass


class WorkToFile(ABC):

    @staticmethod
    def read():
        pass

    @staticmethod
    def write():
        pass


class HaedHunter(WorkApi):
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, text, per_page, city):
        self.test = text
        self.per_page = per_page
        self.area = city

    def get_info(self):
        response = requests.get(self.url, params=self.__dict__)
        info = response.json()['items']
        return info


class SuperJob(WorkApi):
    API_KEY = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, text, city):
        self.keyword = text
        self.t = city

    def get_info(self):
        response = requests.get(self.url, headers=self.API_KEY, params=self.__dict__)
        info = response.json()['objects']
        return info


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


class ReadWriteToJSON(WorkToFile):

    @staticmethod
    def read_json():
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    @staticmethod
    def write_json(data):
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
