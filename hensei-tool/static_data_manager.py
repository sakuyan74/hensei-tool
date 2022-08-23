import pandas as pd
from pathlib import Path


root_path = Path(__file__).resolve().parent


class StaticDataManager():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls.static_busyo_data = BusyoDataManager()
            cls.static_heiho_data = HeihoDataManager()
            cls.static_senpo_data = SenpoDataManager()
            cls._instance = super().__new__(cls)
        return cls

    @classmethod
    def get_busyo_list(cls, exclude_list):
        return cls.static_busyo_data.get_busyo_list(exclude_list)
    
    @classmethod
    def get_senpo_list(cls, include_list=[]):
        return cls.static_senpo_data.get_senpo_list(include_list)

    @classmethod
    def get_busyo_id_by_name(cls, name):
        return cls.static_busyo_data.get_busyo_id_by_name(name)

    @classmethod
    def get_busyo_by_id(cls, busyo_id):
        return cls.static_busyo_data.get_busyo_by_id(busyo_id)

    @classmethod
    def get_senpo_by_id(cls, senpo_id):
        return cls.static_senpo_data.get_senpo_by_id(senpo_id)
    
    @classmethod
    def get_senpo_name_by_id_list(cls, id_list):
        return cls.static_senpo_data.get_senpo_name_by_id_list(id_list)
    
    @classmethod
    def get_heiho_name_by_id_list(cls, id_list):
        return cls.static_heiho_data.get_heiho_name_by_id_list(id_list)
    
    @classmethod
    def get_heiho_id_by_name(cls, name):
        return cls.static_heiho_data.get_heiho_id_by_name(name)
    
    @classmethod
    def get_senpo_id_by_name(cls, name):
        return cls.static_senpo_data.get_senpo_id_by_name(name)
    
    @classmethod
    def get_suitable_by_id(cls, senpo_id):
        return cls.static_senpo_data.get_suitable_by_id(senpo_id)


class BusyoDataManager():
    def __init__(self) -> None:
        self.busyo_org_df = pd.read_table(root_path.joinpath("data/busyo.tsv"), encoding="utf-8")

    def get_busyo_list(self, exclude_list):
        df_busyo_list = self.busyo_org_df.copy()
        df_busyo_list = df_busyo_list[["id", "name", "country", "rare", "cost", "horse", "shield", "bow", "rance", "weapon", "water"]]
        if len(exclude_list) != 0:
            df_busyo_list = df_busyo_list[~df_busyo_list["id"].isin(exclude_list)]

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
    
    def get_heiho_name_by_id_list(self, id_list):
        df_heiho_list = self.heiho_org_df.copy()
        name_list = []
        for id in id_list:
            if id == -1:
                name_list.append("")
                continue
            df_result = df_heiho_list.query('id == ' + str(id))
            name_list.append(df_result["name"].values.tolist()[0])
        return name_list

    def get_heiho_id_by_name(self, name):
        df_heiho_list = self.heiho_org_df.copy()
        df_heiho_list = df_heiho_list[["id", "name"]]
        df_heiho_list = df_heiho_list.query('name == "' + name + '"')
        s_heiho_list = df_heiho_list["id"]
        return s_heiho_list.values.tolist()[0]


class SenpoDataManager():
    def __init__(self) -> None:
        self.senpo_org_df = pd.read_table(root_path.joinpath("data/senpo.tsv"), encoding="utf-8")
        pass

    def get_senpo_by_id(self, senpo_id):
        df_senpo_list = self.senpo_org_df.copy()
        df_senpo_list = df_senpo_list.query('id == ' + str(senpo_id))
        return df_senpo_list.to_dict(orient="records")[0]

    def get_suitable_by_id(self, senpo_id):
        df_senpo_list = self.senpo_org_df.copy()
        df_senpo_list = df_senpo_list.query('id == ' + str(senpo_id))
        df_senpo_list = df_senpo_list[["horse", "shield", "bow", "rance", "weapon"]]
        return df_senpo_list.values.tolist()[0]

    def get_senpo_name_by_id_list(self, id_list):
        df_senpo_list = self.senpo_org_df.copy()
        if len(id_list) != 0:
            df_senpo_list = df_senpo_list[df_senpo_list["id"].isin(id_list)]
        df_senpo_list = df_senpo_list[["id", "name"]]
        df_senpo_list = df_senpo_list.set_index("id")
        return df_senpo_list.to_dict(orient="dict")["name"]

    def get_senpo_list(self, include_list=[]):
        df_senpo_list = self.senpo_org_df.copy()
        df_senpo_list = df_senpo_list[["id", "name", "keisyo", "rare", "type", "horse", "shield", "bow", "rance", "weapon", "effect", "rate", "cap", "desc_easy"]]

        df_senpo_list = df_senpo_list[df_senpo_list["keisyo"] == True]
        df_senpo_list = df_senpo_list.drop("keisyo", axis=1)

        if len(include_list) != 0:
            df_senpo_list = df_senpo_list[df_senpo_list["id"].isin(include_list)]
        df_senpo_list = df_senpo_list.drop("id", axis=1)

        df_senpo_list["rare"] = df_senpo_list["rare"].astype(str)
        df_senpo_list["rate"] = df_senpo_list["rate"].astype(str) + '%'
        df_senpo_list["cap"] = df_senpo_list["cap"].astype(str)
        df_senpo_list["horse"] = df_senpo_list["horse"].astype(str)
        df_senpo_list["horse"] = df_senpo_list["horse"].str.replace("True", "○")
        df_senpo_list["horse"] = df_senpo_list["horse"].str.replace("nan", "")
        df_senpo_list["shield"] = df_senpo_list["shield"].astype(str)
        df_senpo_list["shield"] = df_senpo_list["shield"].str.replace("True", "○")
        df_senpo_list["shield"] = df_senpo_list["shield"].str.replace("nan", "")
        df_senpo_list["bow"] = df_senpo_list["bow"].astype(str)
        df_senpo_list["bow"] = df_senpo_list["bow"].str.replace("True", "○")
        df_senpo_list["bow"] = df_senpo_list["bow"].str.replace("nan", "")
        df_senpo_list["rance"] = df_senpo_list["rance"].astype(str)
        df_senpo_list["rance"] = df_senpo_list["rance"].str.replace("True", "○")
        df_senpo_list["rance"] = df_senpo_list["rance"].str.replace("nan", "")
        df_senpo_list["weapon"] = df_senpo_list["weapon"].astype(str)
        df_senpo_list["weapon"] = df_senpo_list["weapon"].str.replace("True", "○")
        df_senpo_list["weapon"] = df_senpo_list["weapon"].str.replace("nan", "")

        return df_senpo_list.values.tolist()

    def get_senpo_id_by_name(self, name):
        df_senpo_list = self.senpo_org_df.copy()
        df_senpo_list = df_senpo_list[["id", "name"]]
        df_senpo_list = df_senpo_list.query('name == "' + name + '"')
        s_senpo_list = df_senpo_list["id"]
        return s_senpo_list.values.tolist()[0]
