# -- coding: cp1251
from odbcAccess import odbc, expODBC
import sys
import os
indb = odbc(os.path.abspath(
    'ЭкспериментальныеДанныеДляОтладки.accdb'))
outdb = odbc(os.path.abspath('db-work2.accdb'))


for exp in indb.getInfo('Эксперимент', ['КодМатериала', 'ТипЭксперимента'],
                        ['660', 'b']):
    print(exp['КодОбразца'])
    outdb.putInfo('Эксперимент', ['Осциллограмма', 'КалибровочныйКоэффициентОС2(Обоймы)'],
                  [exp['Осциллограмма'],
                      exp['КалибровочныйКоэффициентОС2(Обоймы)']],
                  'КодОбразца', exp['КодОбразца'])
