import sqlite3

DB_NAME = "hensei.db"
HENSEI_TABLE_NAME = "hensei"
HENSEI_TABLE_COLUMN = "hensei_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                       main_unit INTEGER,\
                       sub_1_unit INTEGER,\
                       sub_2_unit INTEGER,\
                       level INTEGER,\
                       kind INTEGER,\
                       heisen_level INTEGER,\
                       kyoryoku_level INTEGER"

UNIT_TABLE_NAME = "unit"
UNIT_TABLE_COLUMN = "unit_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                            busyo INTEGER,\
                            skill_2 INTEGER,\
                            skill_3 INTEGER,\
                            heihousyo INTEGER,\
                            heihou_1 INTEGER,\
                            heihou_2 INTEGER,\
                            heihou_3 INTEGER,\
                            rankup INTEGER,\
                            hizo INTEGER,\
                            anime INTEGER,\
                            buf_str INTEGER,\
                            buf_def INTEGER,\
                            buf_int INTEGER,\
                            buf_spd INTEGER,\
                            buf_eq_str INTEGER,\
                            buf_eq_def INTEGER,\
                            buf_eq_int INTEGER,\
                            buf_eq_spd INTEGER,\
                            eq_skill_list IntList"

UNIT_INSERT_TABLE_COLUMN = "(busyo,skill_2,skill_3,heihousyo,heihou_1,heihou_2,heihou_3,rankup,hizo,anime,buf_str,buf_def,buf_int,buf_spd,buf_eq_str,buf_eq_def,buf_eq_int,buf_eq_spd,eq_skill_list)"

IntList = list
sqlite3.register_adapter(IntList, lambda l: ';'.join([str(i) for i in l]))
sqlite3.register_converter("IntList", lambda s: [int(i) for i in s.split(';')])


class HenseiDataManager():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls.hensei_dao = HenseiDAO()
            if len(cls.hensei_dao.select_all(HENSEI_TABLE_NAME)) != 10:
                cls.hensei_dao.delete_all(HENSEI_TABLE_NAME)
                cls.hensei_dao.delete_all(UNIT_TABLE_NAME)
                cls.hensei_dao.create_hensei_table()
                cls.hensei_dao.create_unit_table()
                cls.hensei_dao.initialize_hensei_table()
            cls._instance = super().__new__(cls)
        return cls

    @classmethod
    def get_hensei_data(cls, hensei_id):
        return cls.hensei_dao.select_hensei_data(hensei_id)

    @classmethod
    def get_selected_busyo_list(cls):
        return cls.hensei_dao.get_selected_busyo_list()
    
    @classmethod
    def set_busyo(cls, busyo_id, unit, hensei_id):
        return cls.hensei_dao.set_busyo(busyo_id, unit, hensei_id)

class HenseiDAO():
    def __init__(self) -> None:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        try:
            cur.execute(
                'CREATE TABLE IF NOT EXISTS ' + HENSEI_TABLE_NAME + '(' + HENSEI_TABLE_COLUMN + ')')
            cur.execute(
                'CREATE TABLE IF NOT EXISTS ' + UNIT_TABLE_NAME + '(' + UNIT_TABLE_COLUMN + ')')
            conn.commit()
        except sqlite3.OperationalError as e:
            print("couldn't create table")
            print(e)

        conn.close()

    def select_hensei_data(self, hensei_id):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT ' + '*' + ' from ' + HENSEI_TABLE_NAME + ' WHERE hensei_id = ?', (hensei_id,))
        hensei_result = {"hensei": dict(cur.fetchone())}
        if hensei_result["hensei"]['main_unit'] is not None:
            cur.execute('SELECT ' + '*' + ' from ' + UNIT_TABLE_NAME + ' WHERE unit_id = ?', (hensei_result["hensei"]['main_unit'],))
            hensei_result["main_unit"] = dict(cur.fetchone())
        if hensei_result["hensei"]['sub_1_unit'] is not None:
            cur.execute('SELECT ' + '*' + ' from ' + UNIT_TABLE_NAME + ' WHERE unit_id = ?', (hensei_result["hensei"]['sub_1_unit'],))
            hensei_result["sub_1_unit"] = dict(cur.fetchone())
        if hensei_result["hensei"]['sub_2_unit'] is not None:
            cur.execute('SELECT ' + '*' + ' from ' + UNIT_TABLE_NAME + ' WHERE unit_id = ?', (hensei_result["hensei"]['sub_2_unit'],))
            hensei_result["sub_2_unit"] = dict(cur.fetchone())
        conn.close

        return hensei_result

    def get_selected_busyo_list(self):
        busyo_list = []
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT ' + '*' + ' from ' + HENSEI_TABLE_NAME)

        # TODO 選択済みの武将をリストアップ処理

        conn.close
        return busyo_list

    def select_all(self, table):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute('SELECT ' + '*' + ' from ' + table)
        item_list = []
        for item in cur.fetchall():
            item_list.append(item)
        conn.close

        return item_list

    def delete_all(self, table):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute('DROP TABLE ' + table)
        conn.commit()
        conn.close()

    def create_hensei_table(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        try:
            cur.execute(
                'CREATE TABLE IF NOT EXISTS ' + HENSEI_TABLE_NAME + '(' + HENSEI_TABLE_COLUMN + ')')
            conn.commit()
        except sqlite3.OperationalError:
            print("couldn't create table")

        conn.close()

    def create_unit_table(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        try:
            cur.execute(
                'CREATE TABLE IF NOT EXISTS ' + UNIT_TABLE_NAME + '(' + UNIT_TABLE_COLUMN + ')')
            conn.commit()
        except sqlite3.OperationalError:
            print("couldn't create table")

        conn.close()

    def initialize_hensei_table(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        try:
            for i in range(10):
                data = [i + 1, None, None, None, 1, 0, 0, 0]
                cur.execute('INSERT INTO ' + HENSEI_TABLE_NAME + ' values(?,?,?,?,?,?,?,?)', data)
            conn.commit()
        except sqlite3.OperationalError:
            print("couldn't insert table")
        conn.close()

    def set_busyo(self, busyo_id, unit, hensei_id):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        data = [busyo_id, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, []]
        cur.execute("INSERT INTO " + UNIT_TABLE_NAME + UNIT_INSERT_TABLE_COLUMN + " values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
        unit_id = cur.lastrowid
        if unit == 0:
            col = "main_unit"
        elif unit == 1:
            col = "sub_1_unit"
        elif unit == 2:
            col = "sub_2_unit"
        else:
            pass

        cur.execute("UPDATE " + HENSEI_TABLE_NAME + " set " + col + "=? where hensei_id=?", (unit_id, hensei_id))

        conn.commit()
        conn.close()

        return
