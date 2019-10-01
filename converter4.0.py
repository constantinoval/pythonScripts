from __future__ import division
import os
import shutil
from math import pi
import struct
import array
import numpy as np
from functools import partial
import io, base64

sampleData=b'f36AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA\ngICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIB/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/\nf39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f39/f4F/foKC\ngoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKC\ngoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKC\ngoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKC\ngoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKC\ngoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKDg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4OD\ng4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4SEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISE\nhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISE\nhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISE\nhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISE\nhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhIQyNS0w\nOS0yMDA4ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0\nZW5zICAgICAgICAgICAgICAgIFN0ZWVsICAgICAgICAgICAgICAg4a+rruitrqkgICAgICAgICAg\nICAAAAAACwABACAgICAgICAgICAgICAgICAgICAgkJGDLTIwIHRlbnNpb24gICAgICBTdGVlbCAg\nICAgICAgICAgICAgIFN0ZWVsICAgICAgICAgICAgICAg/QP9Aw4BDgEGAgYCAAAAAAAAAAAAAAAA\nAAQABFECAAAAAAAAAAAAAAAAAAAAAAAAZmYeQc3MnEAAAAAAAAAAAPrblkEAUENIAAD6RAAAoEEA\nAAAAAACWQwAAoEEAAAAAAAAAAAAAgD/icyc9AACAPwAAgD8AAIA/AACAPwAAAAABAPo/AAAAAKwR\nAToAAAAAPf/HOQAAAAAAAAAAAAAAAAAAAAAAqjRIAACdQzMzm0AAqjRIAACdQzMzm0AAAHpEAACg\nQQAAAAAAgDtFAACgQQAAAAAzM6NAAABIRM3MDEAAAIhCMzOjQAAASETNzAxAAACIQgAAAAAAAAIA\nAQAAAA8AAAAAAAAAAAAAAAAAAQAyAAAAAwAAAAAA//8CAP3/BQAAAAAAAAAAAAAAMzEwMw==\n'
sampleFile=io.BytesIO(sampleData)

def resample(y,points):
    nx=[len(y)/points*i for i in range(points)]
    x=range(len(y))
    ny=np.interp(nx, x, y)
    return ny

def float_to_byte(y,mini=1,maxi=254):
    max=y.max()
    min=y.min()
    if min==0:
        min=1e-20
    if abs(max-min)<=1e-12:
        k=1
        b=0
    else:
        k=(maxi-mini)/(max-min)
        b=1./(max/min-1)*(max/min*mini-maxi)
    by=array.array("B")
    for yy in y:
        by.append( int(np.round(k*yy+b)) )
    return by,1./k

def write_byte_rays(filename, rayA=None, rayB=None):
    f = open(filename,"r+b")
    if rayA!=None:
        if len(rayA)==1024:
            f.seek(0,0)
#            s=""
           # for r in rayA:
#                s+=chr(r)
            f.write(bytearray(rayA))
#            f.write(bytearray(s, 'utf-8'))
    if rayB!=None:
        if len(rayB)==1024:
            f.seek(1024,0)
 #           s=""
            #for r in rayB:
#                s+=chr(r)
            f.write(bytearray(rayB))
 #           f.write(bytearray(s, 'utf-8'))

def write_float_rays(filename,y1,y2, dt=1):
    ndt=dt*len(y1)/1024.0
    yy=resample(y1,1024)
    by1, dA1 = float_to_byte(yy)
    yy=resample(y2,1024)
    by2, dA2 = float_to_byte(yy)
    write_byte_rays(filename,rayA=by1,rayB=by2)
    dat=dat_file(filename)
    dat.diapA=dA1
    dat.diapB=dA2
    dat.dt=ndt*1e6
    print("Float rays was written to file!\n")


class dat_file(object):
    _addr = {"diapA":[2392, 4],
            "diapB":[2400, 4],
            "tarirA":[2368, 4],
            "tarirB":[2376, 4],
            "time_to_point": [2384, 4],
            "E1": [2420, 4],
            "E2": [2432, 4],
            "S1": [2424, 4],
            "S2": [2436, 4],
            "D1": [2448, 4],
            "D2": [2460, 4],
            "V0": [2352, 4],
            "l" : [2304, 4],
            "d" : [2308, 4],
            "d0": [2312, 4],
            "s" : [2320, 4],
            "n1" : [2552, 2],
            "n2" : [2554, 2],
            "c1" : [2428, 4],
            "c2" : [2440, 4]
        }
    def __init__(self,filename):
        self.filename=filename

    def read_data(self,name,fmt='<f'):
        f = open(self.filename,"rb")
        f.seek(self._addr[name][0],0)
        d=f.read(self._addr[name][1])
        f.close()
        return struct.unpack(fmt,d)[0]

    def write_data(self,val=None,name=None, fmt='<f'):
        if val==None: return
        f = open(self.filename,"r+b")
        f.seek(self._addr[name][0],0)
        d=struct.pack(fmt,val)
        f.write(d)
        f.close()

    diapA=property(partial(read_data,name="diapA"),partial(write_data,name="diapA"))
    diapB=property(partial(read_data,name="diapB"),partial(write_data,name="diapB"))
    tarirA=property(partial(read_data,name="tarirA"),partial(write_data,name="tarirA"))
    tarirB=property(partial(read_data,name="tarirB"),partial(write_data,name="tarirB"))
    E1=property(partial(read_data,name="E1"),partial(write_data,name="E1"))
    E2=property(partial(read_data,name="E2"),partial(write_data,name="E2"))
    D1=property(partial(read_data,name="D1"),partial(write_data,name="D1"))
    D2=property(partial(read_data,name="D2"),partial(write_data,name="D2"))
    C1=property(partial(read_data,name="c1"),partial(write_data,name="c1"))
    C2=property(partial(read_data,name="c2"),partial(write_data,name="c2"))
    S1=property(partial(read_data,name="S1"),partial(write_data,name="S1"))
    S2=property(partial(read_data,name="S2"),partial(write_data,name="S2"))
    V0=property(partial(read_data,name="V0"),partial(write_data,name="V0"))
    l=property(partial(read_data,name="l"),partial(write_data,name="l"))
    d=property(partial(read_data,name="d"),partial(write_data,name="d"))
    d0=property(partial(read_data,name="d0"),partial(write_data,name="d0"))
    s=property(partial(read_data,name="s"),partial(write_data,name="s"))
    dt=property(partial(read_data,name="time_to_point"),partial(write_data,name="time_to_point"))
    n1=property(partial(read_data,name="n1", fmt='h'),partial(write_data,name="n1", fmt='h'))
    n2=property(partial(read_data,name="n2", fmt='h'),partial(write_data,name="n2", fmt='h'))

    @property
    def byte_rays(self):
        f = open(self.filename,"rb")
        f.seek(0,0)
        rayA=f.read(1024)
        f.seek(1024,0)
        rayB=f.read(1024)
        f.close()
        rA=array.array("b")
        rB=array.array("b")
        for r1,r2 in zip(rayA,rayB):
            rA.append(ord(r1)-128)
            rB.append(ord(r2)-128)
        return [rA,rB]

    def _readMarkers(self):
        f = open(self.filename,"rb")
        f.seek(2256,0)
        mmA=f.read(24)
        f.seek(2280,0)
        mmB=f.read(24)
        f.close()
        mA=struct.unpack('hhhhhhhhhhhh', mmA)
        mB=struct.unpack('hhhhhhhhhhhh', mmB)
#        mB=array.array("i")
        return [mA,mB]

    def _writeMarkers(self, m):
        mA=(m[0]+[0]*(12-len(m[0])))[:12]
        mB=(m[1]+[0]*(12-len(m[1])))[:12]
#        print mA
        mmA=struct.pack('hhhhhhhhhhhh', *mA)
        mmB=struct.pack('hhhhhhhhhhhh', *mB)
        f = open(self.filename,"r+b")
        f.seek(2256,0)
        f.write(mmA)
        f.seek(2280,0)
        f.write(mmB)
        f.close()
        mB=array.array("i")
    markers=property(_readMarkers, _writeMarkers)

def tofloat(s):
    i=0
    for c in s:
        if not c.isdigit() and c!='.':
            break
        i+=1
    if not i:
        return 0.0
    return float(s[:i])

def convert(dataSourceFile):
    datFile=dataSourceFile[:-3]+'dat'
#    if os.path.exists(datFile):
#        print(datFile+' exists...')
#        return
    print('Converting '+dataSourceFile)
#    shutil.copyfile(sampleFile, datFile)
    open(datFile, 'wb').write(base64.decodebytes(sampleFile.read()))
    dat=dat_file(datFile)
    sourceData=open(dataSourceFile, 'r').readlines()
    mode=None
    jacket=False
    for idx, l in enumerate(sourceData):
        if u'Стержни' in l:
            mode='bars'
            continue
        if u'Образец' in l:
            mode='sample'
            continue
        if u'Ударник' in l:
            mode='stricker'
            continue
        if mode=='bars' and u'ПлощадьПоперечногоСечения' in l:
            S1=tofloat(l.split()[0])
            
        if mode=='bars' and u'МодульУпругости' in l:
            E1=tofloat(l.split()[0])
        if mode=='bars' and u'СкоростьЗвука' in l:
            c1=tofloat(l.split()[0])
        if mode=='sample' and u'ПлощадьПоперечногоСечения' in l:
            S=tofloat(l.split()[0])
        if mode=='sample' and u'ДлинаРабочейЧасти' in l:
            L0=tofloat(l.split()[0])
        if mode=='stricker' and u'Скорость' in l:
            V=tofloat(l.split()[0])
            mode=None
            continue
        if u'Шаг по времени' in l:
            dt=float(l.split(',')[0])
            break
#            print(dt)
#       if u'Деформация от падающего' in l:
#           break
    ei=[]
    er=[]
    et=[]
    ej=[]
    for l in sourceData[idx+2:]:
        try:
            ll=l.split()
            ei.append(float(ll[0]))
            er.append(float(ll[1]))
            et.append(float(ll[2]))
        except:
            pass
    n=len(ei)
    bar1=ei+er
    bar2=[0]*n+et
    dat.S1=S1
    dat.S2=S1
    dat.E1=E1
    dat.E2=E1
    dat.s=S
    dat.l=L0
    dat.V0=V
    dat.C1=c1*1e-3
    dat.C2=c1*1e-3
    dat.tarirA=1.0
    dat.tarirB=1.0
    nn=512
    write_float_rays(datFile, bar1, bar2, dt)
    dat.markers=[[0, nn-1, nn, 2*nn-2], [nn, 2*nn-2]]
    dat.n1=4
    dat.n2=2
    if jacket:
        j_dat=dataSourceFile[:-4]+'_j.dat'
        shutil.copyfile(sampleFile, j_dat)
        dat=dat_file(j_dat)
        dat.d=D1j
        dat.d0=D0j
        dat.s=pi*(D1j**2-D0j**2)/4.0
        dat.E1=Ej
        dat.tarirA=1
        ray=n//2*[0]+ej
        ray+=[0]*(2*n-len(ray))
        write_float_rays(j_dat, ray, [0]*2*n, dt)
        dat.n1=2
        dat.n2=0
        dat.markers=[[256, 256+512], [0, 0]]
        d2=open(j_dat, 'rb').read(2560)
        f=open(datFile, 'r+b')
        f.seek(0,2)
        f.write(d2)
        f.close()
        os.remove(j_dat)

if __name__=="__main__":
    for f in os.listdir(os.curdir):
        if f[-3:].upper()=='LVM' and not u'и' in f:
#            try:
            convert(f)
#            except:
#                print('Can\'t convert file ', f)
#plt.plot(dat.byte_rays[0])
#plt.plot(dat.byte_rays[1])
#plt.plot(m[0], [0]*12, 'o')
#plt.plot(m[1], [0]*12, 'o')
#plt.show()