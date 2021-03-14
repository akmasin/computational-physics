from waktusholat import waktu_sholat

bujur1 = waktu_sholat.bujur('Malang')
lintang1 = waktu_sholat.lintang('Malang')
zona1 = waktu_sholat.zona('Malang')
print(waktu_sholat.dzuhur(2020,11,30,bujur1,lintang1,zona1,50))