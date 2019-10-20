# -- coding: cp1251
from odbcAccess import odbc, expODBC
import sys
import os
indb = odbc(os.path.abspath(
    'ЭкспериментальныеДанныеДляОтладки.accdb'))
outdb = odbc(os.path.abspath('db-work2.accdb'))

for exp in indb.getInfo('Эксперимент', ['КодМатериала', 'ТипЭксперимента'],
                        ['659', 't'], ['КодОбразца', 'Диаметр', 'Примечание']):
    print(exp)
    outdb.putInfo('Эксперимент', ['Диаметр', 'Примечание'],
                  [exp['Диаметр'], exp['Примечание']],
                  'КодОбразца', exp['КодОбразца'])
