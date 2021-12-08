#coding=utf-8
import numpy as np 
nu =14.8*10**(-6)     # viscosity
kg =0.0411            # Gas thermal conductivity
Cpg=1007.0            # Gas specific heat capacity
rhog=1.16             # gas density
rho_a= 1.16
D  =3.514*10**(-5)    # diffusion coefficient
g =9.8 				  # gravity const 
R =8.314              # gas const

u_f=1.0               # (fuel)ui
u_o=4#1.98            # (oxygen)ui
Q_g=-25900.*10**(3)   # heat of combustion
Uf = 0.00042          # spread rate

rho_s=1160.	          # density of solid
Ac =2.82*10**(9)      # Pre exponential factor of solid pyrolysis reaction
Ec =129872.994        # Activation energy of solid pyrolysis reaction
ks =0.188             # Solid thermal conductivity
Cps=1460.             # solid specific heat capacity
thick=2.7*10**(-3)    # solid thickness
#mesh
nx=120*5+1
ny=20*8+1
Lx=0.012*5
Ly=0.002*8
xmin = 0
xmax = Lx
ymin = 0
ymax = Ly
dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)
x  = np.linspace(xmin, xmax, nx)
y  = np.linspace(ymin, ymax, ny)
[x,y]=np.meshgrid(x,y)
indxG_S=int(thick/dx)

# specify solid zone
Solid_matrix =np.zeros([ny,nx],dtype=np.bool)
Solid_matrix[0:indxG_S,:]=True
a_s=ks/(Cps*rho_s)
a_g=kg/(Cpg*rhog)
a=np.zeros([ny,nx])
a[0:indxG_S,:]=a_s
a[indxG_S:,:]=a_g

dt=0.00002      # time step
plotintv = 1000 # save interval 
