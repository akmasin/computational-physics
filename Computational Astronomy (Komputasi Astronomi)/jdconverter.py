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