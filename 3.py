import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
plt.subplots(figsize=(20, 15))
map = Basemap(width=1200000,height=900000,projection='lcc',resolution='l',
                    llcrnrlon=67,llcrnrlat=5,urcrnrlon=99,urcrnrlat=37,lat_0=28,lon_0=77)

map.drawmapboundary ()
map.drawcountries ()
map.drawcoastlines ()

lg=[72.8777]
lt=[19.0760]
nc=['mumbai']
x, y = map(lg, lt)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='cyan')
for ncs, xpt, ypt in zip(nc, x, y):
    plt.text(xpt+60000, ypt+30000, ncs, fontsize=10, fontweight='bold')
    lk=[77.1025]
li=[28.7041]
mn=['delhi ']
x,y=map(lk,li)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='orange')
for mns, xpt, ypt in zip(mn, x, y):
    plt.text(xpt+60000, ypt+30000, mns, fontsize=10, fontweight='bold')
    la=[77.5946]
lb=[12.9716]
na=['Bengaluru']
x, y = map(la, lb)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='green')
for nas, xpt, ypt in zip(na, x, y):
    plt.text(xpt+60000, ypt+30000, nas, fontsize=10, fontweight='bold')
    lc=[78.4867]
ld=[17.3850]
nb=['Hyderabad ']
x, y = map(lc, ld)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='maroon')
for nbs, xpt, ypt in zip(nb, x, y):
    plt.text(xpt+60000, ypt+30000, nbs, fontsize=10, fontweight='bold')
    lf=[72.5713621]
lh=[23.022505]
nd=['Ahmadabad ']
x, y = map(lf, lh)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='blue')
for nds, xpt, ypt in zip(nd, x, y):
    plt.text(xpt+60000, ypt+30000, nds, fontsize=10, fontweight='bold')
    li=[80.2707184]
lj=[13.0826802]
ne=['Chennai ']
x, y = map(li, lj)
plt.scatter(x, y, marker="o")
map.plot(x,y,'k^',markersize=50,alpha=0.5,color='magenta')
for nes, xpt, ypt in zip(ne, x, y):
    plt.text(xpt+60000, ypt+30000, nes, fontsize=10, fontweight='bold')
    lk=[88.363895]
ll=[22.572646]
nf=['Kolkata ']
x, y = map(lk, ll)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='lightgreen')
for nfs, xpt, ypt in zip(nf, x, y):
    plt.text(xpt+60000, ypt+30000, nfs, fontsize=10, fontweight='bold')
    lm=[72.8310607]
ln=[21.1702401]
ng=['Surat ']
x, y = map(lm, ln)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='red')
for ngs, xpt, ypt in zip(ng, x, y):
    plt.text(xpt+60000, ypt+30000, ngs, fontsize=10, fontweight='bold')
    
    lr=[75.7872709]
ls=[26.9124336]
ni=['Jaipur ']
x, y = map(lr, ls)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='violet')
for nis, xpt, ypt in zip(ni, x, y):
    plt.text(xpt+60000, ypt+30000, nis, fontsize=10, fontweight='bold')
    
lu=[77.888000]
lv=[29.854263]
nk=['Roorkee ']
x, y = map(lu, lv)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='yellow')
for nks, xpt, ypt in zip(nk, x, y):
    plt.text(xpt+60000, ypt+30000, nks, fontsize=10, fontweight='bold')
    lx=[85.824539]
lz=[20.296059]
nj=['Bhubaneswar']
x, y = map(lx, lz)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='red')
for njs, xpt, ypt in zip(nj, x, y):
    plt.text(xpt+60000, ypt+30000, njs, fontsize=10, fontweight='bold')
e=[78.01667]
f=[27.18333]
nl=['Agra ']
x, y = map(e, f)
plt.scatter(x, y, marker="o")
map.plot(x,y,'k^',markersize=50,alpha=0.5,color='gold')
for nls, xpt, ypt in zip(nl, x, y):
    plt.text(xpt+60000, ypt+30000, nls, fontsize=10, fontweight='bold')
g=[77.40289]
h=[23.25469]
nm=['Bhopal ']
x, y = map(g, h)
plt.scatter(x, y, marker="o")
map.plot(x,y,'k^',markersize=50,alpha=0.5,color='indigo')
for nms, xpt, ypt in zip(nm, x, y):
    plt.text(xpt+60000, ypt+30000, nms, fontsize=10, fontweight='bold')
i=[76.96612]
j=[11.00555]
nn=['Coimbatore ']
x, y = map(i, j)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='magenta')
for nns, xpt, ypt in zip(nn, x, y):
    plt.text(xpt+60000, ypt+30000, nns, fontsize=10, fontweight='bold')
k=[75.85229]
l=[30.90015]
no=['Ludhiana ']
x, y = map(k, l)
plt.scatter(x, y, marker="o")
map.plot(x,y,'k^',markersize=50,alpha=0.5,color='brown')
for nos, xpt, ypt in zip(no, x, y):
    plt.text(xpt+60000, ypt+30000, nos, fontsize=10, fontweight='bold')
m=[85.11936]
n=[25.60222]
np=['Patna ']
x, y = map(m, n)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='black')
for nps, xpt, ypt in zip(np, x, y):
    plt.text(xpt+60000, ypt+30000, nps, fontsize=10, fontweight='bold')
o=[74.80298]
p=[34.08842]
nq=['Srinagar ']
x, y = map(o, p)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='purple')
for nqs, xpt, ypt in zip(nq, x, y):
    plt.text(xpt+60000, ypt+30000, nqs, fontsize=10, fontweight='bold')
q=[83.20161]
r=[17.68009]
nr=['Visakhapatnam ']
x, y = map(q, r)
plt.scatter(x, y, marker="o")
map.plot(x,y,'k^',markersize=50,alpha=0.5,color='black')
for nrs, xpt, ypt in zip(nr, x, y):
    plt.text(xpt+60000, ypt+30000, nrs, fontsize=10, fontweight='bold')
s=[74.87476]
t=[31.63661]
nt=['Amritsar ']
x, y = map(s, t)
plt.scatter(x, y, marker="o")
map.plot(x,y,'ko',markersize=50,alpha=0.5,color='orange')
for nts, xpt, ypt in zip(nt, x, y):
    plt.text(xpt+60000, ypt+30000, nts, fontsize=10, fontweight='bold')
u=[91.7458]
v=[26.1844]
nu=['Guwahati ']
x, y = map(u, v)
plt.scatter(x, y, marker="o")
map.plot(x,y,'k^',markersize=50,alpha=0.5,color='green')
for nus, xpt, ypt in zip(nu, x, y):
    plt.text(xpt+60000, ypt+30000, nus, fontsize=10, fontweight='bold')
plt.title('Temperature of 20 cities in India on May 26',fontsize=20)
print("enter temperature")
a=int(input())
print("temperature =",a,"°C")