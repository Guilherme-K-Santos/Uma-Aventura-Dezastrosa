

class Item:
    def __init__(self, nome_item: str, att_extra: int, hp_extra: int):
        self.__nome_item = nome_item
        self.__att_extra = att_extra
        self.__hp_extra = hp_extra

    @property
    def nome_item(self):
        return self.__nome_item

    @nome_item.setter
    def nome_item(self, nome_item: str):
        if isinstance(nome_item, str):
            self.__nome_item = nome_item

    @property
    def att_extra(self):
        return self.__att_extra

    @att_extra.setter
    def att_extra(self, att_extra: int):
        if isinstance(att_extra, int):
            self.__att_extra = att_extra

    @property
    def hp_extra(self):
        return self.__hp_extra

    @hp_extra.setter
    def hp_extra(self, hp_extra: int):
        if isinstance(hp_extra, int):
            self.__hp_extra = hp_extra


manopla_basica = Item("Manopla do Buggy", 10, 0)
chuteira_pele = Item("Chuteira do Pelé", 20, 10)
excalibur = Item("Excalibur", 40, 31)
passagem_para_dubai = Item("Passagem para Dubai", 9999999999, 9999)

itens_monstros = [chuteira_pele, excalibur, passagem_para_dubai]
