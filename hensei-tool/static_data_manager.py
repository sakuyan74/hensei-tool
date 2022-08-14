import pandas as pd
from pathlib import Path


root_path = Path(__file__).resolve().parent


class StaticDataManager():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls.static_busyo_data = BusyoDataManager()
            cls.static_heiho_data = HeihoDataManager()
            cls._instance = super().__new__(cls)
        return cls
    
    @classmethod
    def get_busyo_list(cls, exclude_list):
        return cls.static_busyo_data.get_busyo_list(exclude_list)
    
    @classmethod
    def get_busyo_id_by_name(cls, name):
        return cls.static_busyo_data.get_busyo_id_by_name(name)
    
    @classmethod
    def get_busyo_by_id(cls, busyo_id):
        return cls.static_busyo_data.get_busyo_by_id(busyo_id)


class BusyoDataManager():
    def __init__(self) -> None:
        self.busyo_org_df = pd.read_table(root_path.joinpath("data/busyo.tsv"), encoding="utf-8")

    def get_busyo_list(self, exclude_list):
        df_busyo_list = self.busyo_org_df.copy()
        df_busyo_list = df_busyo_list[["id", "name", "country", "rare", "cost", "horse", "shield", "bow", "rance", "weapon", "water"]]
        if len(exclude_list) != 0:
            df_busyo_list = df_busyo_list.query('id != ' + str(exclude_list))

        df_busyo_list = df_busyo_list.drop("id", axis=1)
        df_busyo_list["rare"] = df_busyo_list["rare"].astype(str)
        df_busyo_list["cost"] = df_busyo_list["cost"].astype(str)

        return df_busyo_list.values.tolist()

    def get_busyo_id_by_name(self, name):
        df_busyo_list = self.busyo_org_df.copy()
        df_busyo_list = df_busyo_list[["id", "name"]]
        df_busyo_list = df_busyo_list.query('name == "' + name + '"')
        s_busyo_list = df_busyo_list["id"]
        return s_busyo_list.values.tolist()[0]

    def get_busyo_by_id(self, busyo_id):
        df_busyo_list = self.busyo_org_df.copy()
        df_busyo_list = df_busyo_list.query('id == ' + str(busyo_id))
        return df_busyo_list.to_dict(orient="records")[0]


class HeihoDataManager():
    def __init__(self) -> None:
        self.heiho_org_df = pd.read_table(root_path.joinpath("data/heiho.tsv"), encoding="utf-8")
        pass
