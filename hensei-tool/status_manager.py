class StatusManager():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls.selected_hensei = 1
        return cls
