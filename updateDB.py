# -- coding: cp1251
from odbcAccess import odbc
import sys
import os
kwds = sys.argv
if len(kwds) < 3:
    exit
indb = odbc(os.path.abspath(kwds[1]))
outdb = odbc(os.path.abspath(kwds[2]))

print('������������� ������')
table_names = ['�����������', '��������', '��������',
               '��������������', '���������������', '�������', '�������������������']
for table_name in table_names:
    print('���������������� �������', table_name)
    in_data = indb.getInfo(table_name)
    out_data = outdb.getInfo(table_name)
    out = []
    for d in out_data:
        out.append(str(list(d.values())[1]))
    for d in in_data:
        record = str(list(d.values())[1])
        if not record in out:
            print('���������:', record)
            if '���'in d:
                d.pop('���')
            if '�����'in d:
                d.pop('�����')
            if '������������'in d:
                d.pop('������������')
            if d:
                outdb.insertInfo(table_name, list(
                    d.keys()), list(d.values()))

ec1 = indb.getInfo('�����������', getFields='����������')
ec1 = set([k['����������'] for k in ec1])
ec2 = outdb.getInfo('�����������', getFields='����������')
ec2 = set([k['����������'] for k in ec2])
newec = ec1-ec2
print('���������� �������������:')
print('����� ������� ��� ����������:', len(newec))
newec = list(newec)
N = len(newec)
newec.sort()
for i, ec in enumerate(newec):
    print(ec)
    d = indb.getInfo('�����������', '����������', ec)
    if len(d):
        d = d[0]
    else:
        continue
    print(ec, '��������', N-i-1)
    d.pop('����������')
    d.pop('���')
    outdb.insertInfo('�����������',
                     list(d.keys()), list(d.values()))
