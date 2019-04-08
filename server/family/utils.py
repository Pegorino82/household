from datetime import datetime, date


def date_transform(date_str, format_="%Y-%m-%d"):
    '''Преобразует строку формата 2001-01-01 в объект datetime'''
    return datetime.strptime(date_str, format_).date()


def calculate_age(born, format_="%Y-%m-%d"):
    '''
    Считает возраст по дате рождения
    :param born: дата рождения, datetime или str
    :param format_: формат строки для даты (в случае если передается строковое представление)
    :return:int
    '''
    today = date.today()
    if isinstance(born, datetime):
        pass
    elif isinstance(born, str):
        born = date_transform(born, format_=format_)
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
