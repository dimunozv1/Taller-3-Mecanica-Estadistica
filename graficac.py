import matplotlib.pyplot as plt

UBL8=[]
TL8=[]
UBL10=[]
TL10=[]
UBL14=[]
TL14=[]
UBL20=[]
TL20=[]
UBL28=[]
TL28=[]

f8= open("G1L8.txt","r")
f10= open("G1L10.txt","r")
f14= open("G1L14.txt","r")
f20= open("G1L20.txt","r")
f28= open("G1L28real.txt","r")

for row in f8:
    row=row.split(" ")
    TL8.append(float(row[0]))
    UBL8.append(float(row[5]))

for row in f10:
    row=row.split(" ")
    TL10.append(float(row[0]))
    UBL10.append(float(row[5]))

for row in f14:
    row=row.split(" ")
    TL14.append(float(row[0]))
    UBL14.append(float(row[5]))
    
for row in f20:
    row=row.split(" ")
    TL20.append(float(row[0]))
    UBL20.append(float(row[5]))

for row in f28:
    row=row.split(" ")
    TL28.append(float(row[0]))
    UBL28.append(float(row[5]))


plt.plot(TL8,UBL8,label="L8")
plt.plot(TL10,UBL10,label="L10")
plt.plot(TL14,UBL14,label="L14")
plt.plot(TL20,UBL20,label="L20")
plt.plot(TL28,UBL28,label="L28")
plt.xlabel("T")
plt.ylabel("UL")
plt.axvline(2.279,0,1,marker="o",label="Tc=2.79")
plt.legend()
plt.grid()

plt.show()

