from abc import ABC, abstractmethod
import pickle


class AbstractDAO(ABC):
    @abstractmethod
    def __init__(self, nome_arquivo = ""):
        self.__nome_arquivo = nome_arquivo
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self):
        self.__cache = pickle.load(open(self.__nome_arquivo, 'rb'))

    def __dump(self):
        pickle.dump(self.__cache, open(self.__nome_arquivo, 'wb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            return None

    def get_all(self):
        return list(self.__cache.values())

    def update_key(self, old_key, new_key, new_obj):
        self.remove(old_key)
        self.add(new_key, new_obj)