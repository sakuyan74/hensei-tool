class StatusManager():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls.selected_hensei = 1
            cls.main_heiho_2_3_tuple_list = []
            cls.sub_1_heiho_2_3_tuple_list = []
            cls.sub_2_heiho_2_3_tuple_list = []
        return cls
