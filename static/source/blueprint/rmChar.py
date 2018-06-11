def rmChar(txt:str='', ch:list=[''], new:str=''):
    '''
    Usuwanie znaków
    :param txt - tekst:
    :param ch - lista znaków do usunięcia:
    :param new - opcjonalnie nowy znak na miejsce starych:
    :return:
    '''
    licznik = 0
    for char in ch:
        if txt.find(char) >= 0:
            txt = txt.replace(char, new)
    return txt
