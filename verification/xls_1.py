import xlwings as xl
import numpy as np

b=xl.Book(r'd:\USER\Konstantinov\verification_tasks\exp_pars-ak4-1.xlsx')
b.app.visible=False
ws = b.sheets[1]
data=np.array(ws.range('A2:J15').options(transpose=True).value)

def get_by_conditions(data, v0, T, delta = 1):
    c1=data[4]>v0-delta
    c2=data[4]<v0+delta
    c3=abs(data[9]-T)<1e-3
    return data[:, c1&c2&c3]

print(get_by_conditions(data, 8.5, 20))