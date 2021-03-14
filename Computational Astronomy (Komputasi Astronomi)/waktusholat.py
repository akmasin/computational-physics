from jdconverter import jdconverter
import math as mt
import numpy as np
import pandas as pd
from tabulate import tabulate

class jdconverter:
    def __init__ (self, year, month, day, jd):
        self.year = year
        self.month = month
        self.day = day
        self.jd = jd
    def masehikejd(year,month,day):
        if month>2:
            month=month
        else:
            month = month+12
            year = year-1
        if year > 1582:
            a = int(year/100)
            b = 2 + int(a/4)-a
        elif year<=1582:
            b=0
        JD = 1720994.5 + int(365.25*year) + int(30.6001*(month + 1)) + b + day
        return JD


    def jdkemasehi(jd):
        jd1 = jd+0.5
        z=int(jd1)
        f = jd1-z
        if z < 2299161:
            a=z
        elif z>=2299161:
            aa = int((z-1867216.25)/36524.25)
            a = z + 1 + aa - int(aa/4)
        b = a + 1524
        c = int((b - 122.1)/365.25)
        d = int(365.25*c)
        e = int((b - d)/30.6001)
        tanggal = b - d - int(30.6001*e) + f
        if e == 14 or e == 15:
            m = e - 13
        elif e < 14:
            m = e - 1
        if m == 1 or m == 2:
            y = c - 4715
        elif m>2:
            y = c - 4716
        return ('{}-{}-{}'.format(int(tanggal),m,y))

class waktu_sholat:
    def __init__(self, y, m, d, B, L, Z, H, kota):
        self.y = y
        self.m = m
        self.d = d
        self.B = B
        self.L = L
        self.Z = Z
        self.H = H
        self.kota = kota
    
    def bujur(kota):
        data = pd.read_excel('atakotasholat2.xlsx')#E:/Learn/
        bujur = data['B'][data['kota']==kota]
        return bujur
    def lintang(kota):
        data = pd.read_excel('atakotasholat2.xlsx')
        lintang = data['L'][data['kota']==kota]
        return lintang
    def zona(kota):
        data = pd.read_excel('atakotasholat2.xlsx')
        zona = data['Z'][data['kota']==kota]
        return zona
    def wkt(j): 
	    jam    = int(j)
	    menit0 = abs(j - jam)*60 
	    menit  = int(menit0)
	    detik0 = abs(menit0 - menit)*60
	    detik  = int(detik0)
	    waktu = '{}:{}:{}'.format(jam,menit,detik)
	    return waktu
    
    def delta(jdd):
        T = 2*np.pi*(jdd-2451545)/365.25
        delta = (0.37877 + 23.264*np.sin(57.297*T*np.pi/180-79.547*np.pi/180) 
        + 0.3812*np.sin(2*57.297*T*np.pi/180-82.682*np.pi/180)
        + 0.17132*np.sin(3*57.297*T*np.pi/180-59.722*np.pi/180))*np.pi/180
        return delta


    def transit(y,m,d,B,Li,Z,H):
        jd1 = jdconverter.masehikejd(y,m,d)
        T = 2*np.pi*(jd1-2451545)/365.25
        delta = (0.37877 + 23.264*np.sin(57.297*T*np.pi/180-79.547*np.pi/180) 
        + 0.3812*np.sin(2*57.297*T*np.pi/180-82.682*np.pi/180)
        + 0.17132*np.sin(3*57.297*T*np.pi/180-59.722*np.pi/180))*np.pi/180
        U = (jd1 - 2451545)/36525
        L0 = (280.46607 + 36000.7698*U)*mt.pi/180
        ET = (-(1789 + 237*U)*mt.sin(L0)-(7146 - 62*U)*mt.cos(L0) + (9934-14*U)*mt.sin(2*L0) - (29+ 5*U)
        *mt.cos(2*L0) + (74 + 10*U)*mt.sin(3*L0) + (320 - 4*U)*mt.cos(3*L0) - 212*mt.sin(4*L0))/1000
        transit1 = 12 + Z - B/15 - ET/60
        L = Li*np.pi/180
        #waktu dzuhur
        #dzuhur = transit1
        #waktu_dzuhur = waktu_sholat.wkt(dzuhur)

        #waktu ashar
        #ha = np.arctan(1/(1+np.tan(abs(delta-L))))
        #haa = np.arccos((np.sin(ha)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        #waktu_ashar = waktu_sholat.wkt(transit1 + haa/15)

        #waktu maghrib
        #akarhm = np.sqrt(H)
        #hm = (-0.0347*akarhm - 0.8333)*np.pi/180
        #ham = np.arccos((np.sin(hm)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        #waktu_maghrib = waktu_sholat.wkt(transit1 + ham/15)
        #waktu isya
        #hi = -18*np.pi/180
        #hai = np.arccos((np.sin(hi)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        #waktu_isya = waktu_sholat.wkt(transit1 + hai/15)
        #waktu subuh
        #hs = -20*np.pi/180
        #has = np.arccos((np.sin(hs)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        #waktu_subuh = waktu_sholat.wkt(transit1 - has/15)
        #terbit matahari
        #ht = (-0.8333 - 0.0347*np.sqrt(H))*np.pi/180
        #hat = np.arccos((np.sin(ht)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        #waktu_terbit = waktu_sholat.wkt(transit1 - hat/15)

        #waktu_array = ['subuh', 'terbit', 'dzuhur', 'ashar', 'maghrib', 'isya']
        #waktu_array2=[waktu_subuh, waktu_terbit, waktu_dzuhur, waktu_ashar, waktu_maghrib, waktu_isya]
        #gunakan dictionary
        return transit1

    def dzuhur(y,m,d,B,Li,Z,H):
        waktudzu = waktu_sholat.transit(y,m,d,B,Li,Z,H)
        waktu_dzuhur = waktu_sholat.wkt(waktudzu)
        return waktu_dzuhur
    
    def ashar(y,m,d,B,Li,Z,H):
        waktuas = waktu_sholat.transit(y,m,d,B,Li,Z,H)
        delta = waktu_sholat.delta(jdconverter.masehikejd(y,m,d))
        L = Li*np.pi/180
        ha = np.arctan(1/(1+np.tan(abs(delta-L))))
        haa = np.arccos((np.sin(ha)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        waktu_ashar = waktu_sholat.wkt(waktuas + haa/15)
        return waktu_ashar
    
    def maghrib(y,m,d,B,Li,Z,H):
        waktuma = waktu_sholat.transit(y,m,d,B,Li,Z,H)
        akarhm = np.sqrt(H)
        hm = (-0.0347*akarhm - 0.8333)*np.pi/180
        delta = waktu_sholat.delta(jdconverter.masehikejd(y,m,d))
        L = Li*np.pi/180
        ham = np.arccos((np.sin(hm)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        waktu_maghrib = waktu_sholat.wkt(waktuma + ham/15)
        return waktu_maghrib
    
    def isya(y,m,d,B,Li,Z,H):
        waktuis = waktu_sholat.transit(y,m,d,B,Li,Z,H)
        delta = waktu_sholat.delta(jdconverter.masehikejd(y,m,d))
        L = Li*np.pi/180
        hi = -18*np.pi/180
        hai = np.arccos((np.sin(hi)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        waktu_isya = waktu_sholat.wkt(waktuis + hai/15)
        return waktu_isya
    
    def subuh(y,m,d,B,Li,Z,H):
        waktusu = waktu_sholat.transit(y,m,d,B,Li,Z,H)
        delta = waktu_sholat.delta(jdconverter.masehikejd(y,m,d))
        L = Li*np.pi/180
        hs = -20*np.pi/180
        has = np.arccos((np.sin(hs)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        waktu_subuh = waktu_sholat.wkt(waktusu - has/15)
        return waktu_subuh
    
    def terbit(y,m,d,B,Li,Z,H):
        waktuter = waktu_sholat.transit(y,m,d,B,Li,Z,H)
        delta = waktu_sholat.delta(jdconverter.masehikejd(y,m,d))
        L = Li*np.pi/180
        ht = (-0.8333 - 0.0347*np.sqrt(H))*np.pi/180
        hat = np.arccos((np.sin(ht)-np.sin(L)*np.sin(delta))/(np.cos(L)*np.cos(delta))) * 180/np.pi
        waktu_terbit = waktu_sholat.wkt(waktuter - hat/15)
        return waktu_terbit

        
# tabulate([[waktu_array[0], waktu_array2[0]],
#         [waktu_array[1], waktu_array2[1]],
#         [waktu_array[2], waktu_array2[2]],
#         [waktu_array[3], waktu_array2[3]],
#         [waktu_array[4], waktu_array2[4]],
#         [waktu_array[5], waktu_array2[5]]], headers=['Jadwal', 'Waktu'])
#a = waktu_sholat.transit(2020,11,9,112,-7.56,7,5)
#print(a[0])
# nama_kota = input('Waktu sholat daerah : ')
# bujur1 = waktu_sholat.bujur(nama_kota)
# lintang1 = waktu_sholat.lintang(nama_kota)
# zona1 = waktu_sholat.zona(nama_kota)


# print(waktu_sholat.transit(2020,11,16,bujur1,lintang1,zona1,50))
# #print(jdconverter.masehikejd(2020,11,9))
