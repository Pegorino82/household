import sqlite3


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
            print(sql)
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

    def insert_into_table(self, tb_name, **kwargs):
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


if __name__ == '__main__':
    db = DB('household')
    db.connect()
    db.drop_table('members')
    db.create_table(
        'members',
        name='VARCHAR(32)',
        patronymic='VARCHAR(32)',
        surname='VARCHAR(32)',
        birthdate='VARCHAR(32)'
    )

    db.create_table(
        'sources',
        name='VARCHAR(32)',
        is_regular='BOOLEAN'
    )

    db.insert_into_table(
        'members_1',
        name='Fred',
        patronymic='D',
        surname='Flinstone',
        birthdate='1900-12-12'
    )
