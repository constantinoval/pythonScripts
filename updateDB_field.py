# -- coding: cp1251
from odbcAccess import odbc, expODBC
import sys
import os
indb = odbc(os.path.abspath(
    '���������������������������������.accdb'))
outdb = odbc(os.path.abspath('db-work2.accdb'))


for exp in indb.getInfo('�����������', ['������������', '���������������'],
                        ['660', 'b']):
    print(exp['����������'])
    outdb.putInfo('�����������', ['�������������', '��������������������������2(������)'],
                  [exp['�������������'],
                      exp['��������������������������2(������)']],
                  '����������', exp['����������'])
