# coding: cp1251
from odbcAccess import expODBC
import xlwt as xls

db = expODBC(r"D:\work\NIIM\db-work2.accdb")
exp_code = 'c649-01'
xls_file_name = exp_code+'.xls'
experiment = db.getExperimentData(exp_code)
wb = xls.Workbook()
ws = wb.add_sheet(exp_code)
ws.write(0, 0, 'Установка')
ws.write(1, 0, 'Нагружающий мерный стержень')
b1 = db.getBarData(experiment.bars[0])
ws.write(2, 0, 'E, МПа')
ws.write(2, 1, b1.E)
ws.write(3, 0, 'c, м/c')
ws.write(3, 1, b1.c)
ws.write(4, 0, 'D, мм')
ws.write(4, 1, b1.d)
ws.write(5, 0, 'тарировочный коэффициент, 1/В')
ws.write(5, 1, experiment.tarir[0])
ws.write(6, 0, 'расстояние от образца до датчиков, мм')
ws.write(6, 1, experiment.datPosition[0])

ws.write(7, 0, 'Опорный мерный стержень')
b1 = db.getBarData(experiment.bars[1])
ws.write(8, 0, 'E, МПа')
ws.write(8, 1, b1.E)
ws.write(9, 0, 'c, м/c')
ws.write(9, 1, b1.c)
ws.write(10, 0, 'D, мм')
ws.write(10, 1, b1.d)
ws.write(11, 0, 'тарировочный коэффициент, 1/В')
ws.write(11, 1, experiment.tarir[1])
ws.write(12, 0, 'расстояние от образца до датчиков, мм')
ws.write(12, 1, experiment.datPosition[1])

ws.write(13, 0, 'Образец')
ws.write(14, 0, 'Длина, мм')
ws.write(14, 1, experiment.l0)
ws.write(15, 0, 'Диаметр, мм')
ws.write(15, 1, experiment.d0)

ws.write(16, 0, 'Ударник')
ws.write(17, 0, 'Длина, мм')
ws.write(17, 1, db.getStrickerData(experiment.striker).l)
ws.write(18, 0, 'Скорость, м/c')
ws.write(18, 1, experiment.V)

ws.write(0, 5, 'Сигналы с мерных стержней')
ws.write(0, 6, 'время, мкс')
ws.write(0, 7, 'нагружающий стержень, В')
ws.write(0, 8, 'опорный стержень, В')
for i in range(len(experiment.osc['t'])):
    ws.write(1+i, 6, experiment.osc['t'][i]*1e6)
    ws.write(1+i, 7, experiment.osc['rays'][0][i])
    ws.write(1+i, 8, experiment.osc['rays'][1][i])

wb.save(xls_file_name)
