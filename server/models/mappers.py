import sqlite3
from family import FamilyMember


class DB:
    ENGINES = {'sqlite3': sqlite3}

    def __init__(self, db_name, engine='sqlite3'):
        self.db_name = db_name
        self._engine = __class__.ENGINES[engine]  # получаем движок бд
        self.conn = None  # соединение с бд
        self.cursor = None  # курсор бд

    @property
    def engine(self):
        return self._engine

    def connect(self):
        self.conn = self.engine.connect(self.db_name + '.db')
        self.cursor = self.conn.cursor()

    def create_table(self, tb_name, **kwargs):
        '''
        Создает таблицу
        :param tb_name: имя таблицы
        :param kwargs: поля - тип данных (в str, напр. 'VARCHAR(32)')
        :return: True or None
        '''
        try:
            params = ', '.join([key + ' ' + val for key, val in kwargs.items()])
            sql = f'CREATE TABLE IF NOT EXISTS {tb_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {params})'
            # print(sql)
            self.cursor.execute(sql)
            return True
        except Exception as err:
            print(f'creating table {tb_name} failed -> {err}')

    def drop_table(self, tb_name):
        '''
        :param tb_name: имя таблицы
        :return: True or None
        '''
        try:
            self.cursor.execute(f'DROP TABLE {tb_name}')
            return True
        except sqlite3.OperationalError:
            print(f'no table <{tb_name}> detected')

    def _insert_into_table(self, tb_name, **kwargs):
        '''
        добавляет запись в таблицу tb_name
        :param tb_name: имя таблицы
        :param kwargs: значения
        :return:
        '''

        try:
            keys = ', '.join(kwargs.keys())
            values = tuple(kwargs.values())
            params = ', '.join(['?' for _ in range(len(kwargs))])
            sql = f'INSERT INTO {tb_name}({keys}) VALUES ({params})'
            # print(sql)
            # print(values)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except Exception as err:
            print(err)

    def _get_by_id(self, table_name, id_):
        try:
            self.cursor.execute(f'SELECT * FROM {table_name} WHERE id=?', (id_,))
            result = self.cursor.fetchone()
            return result
        except Exception as err:
            print(f'fetching from {tb_name} by id failed -> {err}')

    def _delete_by_key(self, tb_name, param, key='id'):
        sql = f'DELETE FROM {tb_name} WHERE {key}=?'
        try:
            self.cursor.execute(sql, (param,))
            self.conn.commit()
            return True
        except Exception as err:
            print(f'deleting from {tb_name} by {key} failed -> {err}')


class FamilyMemberMapper(DB):

    def __init__(self, db_name, engine='sqlite3'):
        super().__init__(db_name, engine=engine)
        super().connect()
        self.tb_name = 'members'
        self._class = FamilyMember

    def insert(self, family_member: FamilyMember):
        return self._insert_into_table(self.tb_name, **family_member.__dict__)

    def get_by_id(self, id_):
        member = self._get_by_id(self.tb_name, id_)
        member = self._class(*member[1:])  # убираем из выборки id
        return member

    def delete_by_id(self, id_):
        return self._delete_by_key(self.tb_name, id_, key='id')


if __name__ == '__main__':
    # db = DB('household')
    # db.connect()
    # db.drop_table('members')
    # db.create_table(
    #     'members',
    #     name='VARCHAR(32)',
    #     patronymic='VARCHAR(32)',
    #     surname='VARCHAR(32)',
    #     birthdate='VARCHAR(32)'
    # )
    #
    # db.create_table(
    #     'sources',
    #     name='VARCHAR(32)',
    #     is_regular='BOOLEAN'
    # )

    mapper = FamilyMemberMapper('household')

    father = FamilyMember('John', 'D', 'Black', '1962-12-30')
    mapper.insert(father)

    mother = FamilyMember('Mary', 'D', 'Black', '1970-1-15')
    mapper.insert(mother)

    print(mapper.get_by_id(1))
    print(mapper.delete_by_id(1))
