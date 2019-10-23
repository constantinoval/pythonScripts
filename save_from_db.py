# coding: cp1251
from odbcAccess import expODBC
import xlwt as xls

db = expODBC(r"D:\work\NIIM\db-work2.accdb")
exp_code = 'c649-01'
xls_file_name = exp_code+'.xls'
experiment = db.getExperimentData(exp_code)
wb = xls.Workbook()
ws = wb.add_sheet(exp_code)
ws.write(0, 0, '���������')
ws.write(1, 0, '����������� ������ ��������')
b1 = db.getBarData(experiment.bars[0])
ws.write(2, 0, 'E, ���')
ws.write(2, 1, b1.E)
ws.write(3, 0, 'c, �/c')
ws.write(3, 1, b1.c)
ws.write(4, 0, 'D, ��')
ws.write(4, 1, b1.d)
ws.write(5, 0, '������������ �����������, 1/�')
ws.write(5, 1, experiment.tarir[0])
ws.write(6, 0, '���������� �� ������� �� ��������, ��')
ws.write(6, 1, experiment.datPosition[0])

ws.write(7, 0, '������� ������ ��������')
b1 = db.getBarData(experiment.bars[1])
ws.write(8, 0, 'E, ���')
ws.write(8, 1, b1.E)
ws.write(9, 0, 'c, �/c')
ws.write(9, 1, b1.c)
ws.write(10, 0, 'D, ��')
ws.write(10, 1, b1.d)
ws.write(11, 0, '������������ �����������, 1/�')
ws.write(11, 1, experiment.tarir[1])
ws.write(12, 0, '���������� �� ������� �� ��������, ��')
ws.write(12, 1, experiment.datPosition[1])

ws.write(13, 0, '�������')
ws.write(14, 0, '�����, ��')
ws.write(14, 1, experiment.l0)
ws.write(15, 0, '�������, ��')
ws.write(15, 1, experiment.d0)

ws.write(16, 0, '�������')
ws.write(17, 0, '�����, ��')
ws.write(17, 1, db.getStrickerData(experiment.striker).l)
ws.write(18, 0, '��������, �/c')
ws.write(18, 1, experiment.V)

ws.write(0, 5, '������� � ������ ��������')
ws.write(0, 6, '�����, ���')
ws.write(0, 7, '����������� ��������, �')
ws.write(0, 8, '������� ��������, �')
for i in range(len(experiment.osc['t'])):
    ws.write(1+i, 6, experiment.osc['t'][i]*1e6)
    ws.write(1+i, 7, experiment.osc['rays'][0][i])
    ws.write(1+i, 8, experiment.osc['rays'][1][i])

wb.save(xls_file_name)
