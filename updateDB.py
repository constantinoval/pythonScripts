# -- coding: cp1251
from odbcAccess import odbc
import sys
import os
kwds = sys.argv
if len(kwds) < 3:
    exit
indb = odbc(os.path.abspath(kwds[1]))
outdb = odbc(os.path.abspath(kwds[2]))

print('Синхронизация таблиц')
table_names = ['ВидПоставки', 'Заказчик', 'Материал',
               'МерныйСтержень', 'ТипЭксперимента', 'Ударник', 'МатериалЭксперимент']
for table_name in table_names:
    print('Синхронизируется таблица', table_name)
    in_data = indb.getInfo(table_name)
    out_data = outdb.getInfo(table_name)
    out = []
    for d in out_data:
        out.append(str(list(d.values())[1]))
    for d in in_data:
        record = str(list(d.values())[1])
        if not record in out:
            print('Добавлено:', record)
            if 'Код'in d:
                d.pop('Код')
            if 'Номер'in d:
                d.pop('Номер')
            if 'Документация'in d:
                d.pop('Документация')
            if d:
                outdb.insertInfo(table_name, list(
                    d.keys()), list(d.values()))

ec1 = indb.getInfo('Эксперимент', getFields='КодОбразца')
ec1 = set([k['КодОбразца'] for k in ec1])
ec2 = outdb.getInfo('Эксперимент', getFields='КодОбразца')
ec2 = set([k['КодОбразца'] for k in ec2])
newec = ec1-ec2
print('Добавление экспериментов:')
print('Число записей для добавления:', len(newec))
newec = list(newec)
N = len(newec)
newec.sort()
for i, ec in enumerate(newec):
    print(ec)
    d = indb.getInfo('Эксперимент', 'КодОбразца', ec)
    if len(d):
        d = d[0]
    else:
        continue
    print(ec, 'осталось', N-i-1)
    d.pop('КодОбразца')
    d.pop('Код')
    outdb.insertInfo('Эксперимент',
                     list(d.keys()), list(d.values()))
