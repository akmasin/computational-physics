from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from pandas import read_excel, DataFrame
import numpy as np

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
        data = read_excel('atakotasholat2.xlsx')#E:/Learn/
        bujur = data['B'][data['kota']==kota]
        return bujur
    def lintang(kota):
        data = read_excel('atakotasholat2.xlsx')
        lintang = data['L'][data['kota']==kota]
        return lintang
    def zona(kota):
        data = read_excel('atakotasholat2.xlsx')
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
        L0 = (280.46607 + 36000.7698*U)*np.pi/180
        ET = (-(1789 + 237*U)*np.sin(L0)-(7146 - 62*U)*np.cos(L0) + (9934-14*U)*np.sin(2*L0) - (29+ 5*U)
        *np.cos(2*L0) + (74 + 10*U)*np.sin(3*L0) + (320 - 4*U)*np.cos(3*L0) - 212*np.sin(4*L0))/1000
        transit1 = 12 + Z - B/15 - ET/60
        L = Li*np.pi/180
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

root = Tk()
root.title('Aplikasi Jadwal Sholat (Akmal Adnan Attamami)')
canvas = Canvas(root, height = 600, width = 500)#bg='#2E933C'
canvas.pack()
gambar_background = PhotoImage(file = 'E:/Learn/APLIKASI JADWAL SHOLAT/greenbg.png')
label_background = Label(root, image = gambar_background)
label_background.place(relwidth = 1, relheight = 1)
frame = Frame(root, bg = "#81C14B", bd = 7 )
frame.place(relx = 0.5, rely = 0.05, relwidth = 0.9, relheight = 0.2, anchor = 'n')
frame1 = Frame(root, bg = "#81C14B", bd = 5 )
frame1.place(relx = 0.5, rely = 0.3, relwidth = 0.9, relheight = 0.1, anchor = 'n')
frame2 = Frame(root, bg = "#81C14B", bd = 5 )
frame2.place(relx = 0.5, rely = 0.425, relwidth = 0.9, relheight = 0.55, anchor = 'n')

label1 = Label(frame2,  bg = "#2E933C")
label1.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.9)


sbh1 = Label(label1, text = 'Shubuh', bg = '#81C14B', font = 35)
sbh1.place(relx = 0.025, rely = 0.03, relwidth = 0.45, relheight = 0.12)

sbh = Label(label1, bg = '#81C14B', font = 35)
sbh.place(relx = 0.525, rely = 0.03, relwidth = 0.45, relheight = 0.12)

trb1 = Label(label1, text = 'Terbit', bg = '#81C14B', font = 35)
trb1.place(relx = 0.025, rely = 0.19, relwidth = 0.45, relheight = 0.12)

trb = Label(label1, bg = '#81C14B', font = '35')
trb.place(relx = 0.525, rely = 0.19, relwidth = 0.45, relheight = 0.12)

dhr1 = Label(label1, text = 'Dzuhur', bg = '#81C14B', font = 35)
dhr1.place(relx = 0.025, rely = 0.35, relwidth = 0.45, relheight = 0.12)
dhr = Label(label1, bg = '#81C14B', font = '35')
dhr.place(relx = 0.525, rely = 0.35, relwidth = 0.45, relheight = 0.12)

ash1 = Label(label1, text = 'ashar', bg = '#81C14B', font = 35)
ash1.place(relx = 0.025, rely = 0.51, relwidth = 0.45, relheight = 0.12)

ash = Label(label1, bg = '#81C14B', font = '35')
ash.place(relx = 0.525, rely = 0.51, relwidth = 0.45, relheight = 0.12)

mgh1 = Label(label1, text = 'Maghrib', bg = '#81C14B', font = 35)
mgh1.place(relx = 0.025, rely = 0.67, relwidth = 0.45, relheight = 0.12)

mgh = Label(label1, bg = '#81C14B', font = '35')
mgh.place(relx = 0.525, rely = 0.67, relwidth = 0.45, relheight = 0.12)

isy1 = Label(label1, text = 'Isya', bg = '#81C14B', font = 35)
isy1.place(relx = 0.025, rely = 0.83, relwidth = 0.45, relheight = 0.12)

isy = Label(label1, bg = '#81C14B', font = '35')
isy.place(relx = 0.525, rely = 0.83, relwidth = 0.45, relheight = 0.12)


tahunl = Label(frame, text = 'Tahun', font = 35 ,bg = '#2E933C')
tahunl.place(relx = 0.01, rely = 0, relwidth = 0.2, relheight = 0.3)

tahun_entered = Entry(frame, textvariable = IntVar(), font = 35, bg = '#2E933C') #DoubleVar()
tahun_entered.place(relx = 0.01, rely = 0.4, relwidth = 0.2, relheight = 0.3)
a1 = list(range(1,32))
df = [['JAN', 1], ['FEB', 2], ['MAR',3], ['APR',4], ['MEI',5], ['JUN',6], ['JUL',7], ['AGU',8],
 ['SEP',9], ['OKT',10], ['NOV',11], ['DES',12]]
b = DataFrame(df, columns = ['bulan', 'urutan']) 
bulanl = Label(frame, text = 'Bulan', font = 35 ,bg = '#2E933C')
bulanl.place(relx = 0.25, rely = 0, relwidth = 0.2, relheight = 0.3)
bulan = StringVar()
bulan_chosen = ttk.Combobox(frame, textvariable = bulan)
bulan_chosen['values'] = list(b['bulan'])
bulan_chosen.place(relx = 0.25, rely = 0.4, relwidth = 0.2, relheight = 0.3)
bulan_chosen.current(0)
tanggall = Label(frame, text = 'Tanggal', font = 35 ,bg = '#2E933C')
tanggall.place(relx = 0.5, rely = 0, relwidth = 0.2, relheight = 0.3)
tanggal = StringVar()
tanggal_chosen = ttk.Combobox(frame, textvariable = tanggal)
tanggal_chosen['values'] = (a1)
tanggal_chosen.place(relx = 0.5, rely = 0.4, relwidth = 0.2, relheight = 0.3)
tanggal_chosen.current(0)
kotal = Label(frame, text = 'Tempat', font = 35 ,bg = '#2E933C')
kotal.place(relx = 0.75, rely = 0, relwidth = 0.24, relheight = 0.3)
data = read_excel('E:/Learn/APLIKASI JADWAL SHOLAT/atakotasholat2.xlsx')#
kota = StringVar()
kota_chosen = ttk.Combobox(frame, textvariable = kota)
kota_chosen['values'] = list(data['kota'])
kota_chosen.place(relx = 0.75, rely = 0.4, relwidth = 0.24, relheight = 0.3)

#LABEL
#mylabel1 = Label(root, text="gople")



#fungsi perintah
def myclick():
    bujur1 = waktu_sholat.bujur(kota_chosen.get())
    lintang1 = waktu_sholat.lintang(kota_chosen.get())
    zona1 = waktu_sholat.zona(kota_chosen.get())
    tanggal2 = int(tanggal_chosen.get())
    tahun2 = int(tahun_entered.get())
    bulan2 = bulan_chosen.get() #int(bulan_chosen.get())
    bulan3 = int(b['urutan'][b['bulan']==bulan2])
    #mylabel2.pack()
    sbh1 = Label(label1, text = 'Shubuh', bg = '#81C14B', font = 35)
    sbh1.place(relx = 0.025, rely = 0.03, relwidth = 0.45, relheight = 0.12)

    sbh = Label(label1, bg = '#81C14B', font = 35)
    sbh.place(relx = 0.525, rely = 0.03, relwidth = 0.45, relheight = 0.12)

    trb1 = Label(label1, text = 'Terbit', bg = '#81C14B', font = 35)
    trb1.place(relx = 0.025, rely = 0.19, relwidth = 0.45, relheight = 0.12)

    trb = Label(label1, bg = '#81C14B', font = '35')
    trb.place(relx = 0.525, rely = 0.19, relwidth = 0.45, relheight = 0.12)

    dhr1 = Label(label1, text = 'Dzuhur', bg = '#81C14B', font = 35)
    dhr1.place(relx = 0.025, rely = 0.35, relwidth = 0.45, relheight = 0.12)
    dhr = Label(label1, bg = '#81C14B', font = '35')
    dhr.place(relx = 0.525, rely = 0.35, relwidth = 0.45, relheight = 0.12)

    ash1 = Label(label1, text = 'ashar', bg = '#81C14B', font = 35)
    ash1.place(relx = 0.025, rely = 0.51, relwidth = 0.45, relheight = 0.12)

    ash = Label(label1, bg = '#81C14B', font = '35')
    ash.place(relx = 0.525, rely = 0.51, relwidth = 0.45, relheight = 0.12)

    mgh1 = Label(label1, text = 'Maghrib', bg = '#81C14B', font = 35)
    mgh1.place(relx = 0.025, rely = 0.67, relwidth = 0.45, relheight = 0.12)

    mgh = Label(label1, bg = '#81C14B', font = '35')
    mgh.place(relx = 0.525, rely = 0.67, relwidth = 0.45, relheight = 0.12)

    isy1 = Label(label1, text = 'Isya', bg = '#81C14B', font = 35)
    isy1.place(relx = 0.025, rely = 0.83, relwidth = 0.45, relheight = 0.12)

    isy = Label(label1, bg = '#81C14B', font = '35')
    isy.place(relx = 0.525, rely = 0.83, relwidth = 0.45, relheight = 0.12)

    shubuh = Label(label1, text=str(waktu_sholat.subuh(tahun2,bulan3,tanggal2,bujur1,lintang1,zona1,50)),bg = '#81C14B', font = '35') 
    shubuh.place(relx = 0.525, rely = 0.03, relwidth = 0.45, relheight = 0.12)
    terbit = Label(label1, text=str(waktu_sholat.terbit(tahun2,bulan3,tanggal2,bujur1,lintang1,zona1,50)),bg = '#81C14B', font = '35') 
    terbit.place(relx = 0.525, rely = 0.19, relwidth = 0.45, relheight = 0.12) 
    dzuhur = Label(label1, text=str(waktu_sholat.dzuhur(tahun2,bulan3,tanggal2,bujur1,lintang1,zona1,50)),bg = '#81C14B', font = '35')#
    dzuhur.place(relx = 0.525, rely = 0.35, relwidth = 0.45, relheight = 0.12)

    ashar = Label(label1, text=str(waktu_sholat.ashar(tahun2,bulan3,tanggal2,bujur1,lintang1,zona1,50)),bg = '#81C14B', font = '35')
    ashar.place(relx = 0.525, rely = 0.51, relwidth = 0.45, relheight = 0.12)
    
    maghrib = Label(label1, text=str(waktu_sholat.maghrib(tahun2,bulan3,tanggal2,bujur1,lintang1,zona1,50)),bg = '#81C14B', font = '35')
    maghrib.place(relx = 0.525, rely = 0.67, relwidth = 0.45, relheight = 0.12)

    isya = Label(label1, text=str(waktu_sholat.isya(tahun2,bulan3,tanggal2,bujur1,lintang1,zona1,50)),bg = '#81C14B', font = '35')
    isya.place(relx = 0.525, rely = 0.83, relwidth = 0.45, relheight = 0.12)
mybutton1 = Button(frame1, text="Waktu Sholat",padx=50,pady=15, command=myclick, fg='black',bg='#2E933C',font = 35) #padx=20,pady=15 #state = DISABLED agar tak bisa diklik
mybutton1.place(relx = 0.05, rely = 0.05, relwidth = 3, relheight = 3)
mybutton1.pack()





root.mainloop()
