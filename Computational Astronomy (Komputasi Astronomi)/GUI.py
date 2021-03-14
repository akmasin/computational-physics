from tkinter import *
from waktusholat import waktu_sholat
from tkinter import ttk
from tkinter import messagebox as msg
import pandas as pd 
import numpy as np
root = Tk()
root.title('Aplikasi Jadwal Sholat (Akmal Adnan Attamami)')
canvas = Canvas(root, height = 600, width = 500)#bg='#2E933C'
canvas.pack()
gambar_background = PhotoImage(file = 'greenbg.png')
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



#INPUT
# masukan = Entry(root)
# masukan.pack()
# masukan.insert(0, "Masukkan Nama Kota")
tahunl = Label(frame, text = 'Tahun', font = 35 ,bg = '#2E933C')
tahunl.place(relx = 0.01, rely = 0, relwidth = 0.2, relheight = 0.3)

tahun_entered = Entry(frame, textvariable = IntVar(), font = 35, bg = '#2E933C') #DoubleVar()
tahun_entered.place(relx = 0.01, rely = 0.4, relwidth = 0.2, relheight = 0.3)

a1 = list(range(1,32))
a2 = list(range(1,31))
a3 = list(range(1,30))
a4 = list(range(1,29))
#list(range(1,13))
df = [['JAN', 1], ['FEB', 2], ['MAR',3], ['APR',4], ['MEI',5], ['JUN',6], ['JUL',7], ['AGU',8],
 ['SEP',9], ['OKT',10], ['NOV',11], ['DES',12]]
b = pd.DataFrame(df, columns = ['bulan', 'urutan']) 



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

data = pd.read_excel('atakotasholat2.xlsx')#E:/Learn/
kota = StringVar()
kota_chosen = ttk.Combobox(frame, textvariable = kota)
kota_chosen['values'] = list(data['kota'])
#kota_entered = Entry(frame, textvariable = kota, font = 35, bg = '#2E933C')
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
    #dhr = Label(mylabel2, )
    #dhr.place(relx = 0.525, rely = 0.23, relwidth = 0.45, relheight = 0.15)

#Button / tombol
mybutton1 = Button(frame1, text="Waktu Sholat",padx=50,pady=15, command=myclick, fg='black',bg='#2E933C',font = 35) #padx=20,pady=15 #state = DISABLED agar tak bisa diklik
mybutton1.place(relx = 0.05, rely = 0.05, relwidth = 3, relheight = 3)
mybutton1.pack()





root.mainloop()