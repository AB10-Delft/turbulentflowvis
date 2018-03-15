import scipy.io as sc
import numpy as np
import h5py
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#from enthought.mayavi import mlab


####  read the matlabfile
dt = sc.loadmat('raw_data_1.mat')

### using correct keys, obtain three 3D matrixes, representing u,v,w velocities
vel_u =  dt['u']
vel_w =  dt['w']
vel_v = dt['v']


### transform the matrixes into arrays, because arrays are "better"
vel_u = np.squeeze(np.asarray(vel_u))
vel_w = np.squeeze(np.asarray(vel_w))
vel_v = np.squeeze(np.asarray(vel_v))


#----------- PLOTS ------------------#


### simple 2D plot
#graph = vel_u*vel_u  # U^2  kinetic energy
#plt.pcolor(graph[0])
#plt.show()


### useless mesh
#mlab.mesh(vel_u[0],vel_w[0],vel_v[0])  #inputs are 2D arrays so its kinda useless atm
#mlab.outline()
#mlab.show()


### flow   (useful for non-torbulent flows, too lazy to explain this)
#mlab.flow(vel_u,vel_v,vel_w, seed_resolution = 175,seed_scale = 1, seed_visible = False, seedtype = 'sphere')
#mlab.outline()
#mlab.show()


### contour3d
#mlab.contour3d(vel_u)  #input is a single 3D array, so it could be useful for e.g. showing magnitude
#mlab.outline()         #further below there is a plot where i actually calculated the magnitudes
#mlab.show()


### quiver3d
#mlab.quiver3d(vel_u[:52],vel_v[:52],vel_w[:52])  #best function there, gives a real vector field
#mlab.outline()                                   #unfortunately python 32bit was only capable of doing ~52 columns
#mlab.show()


#------------PIPE LINE PLOTS ------- ----#
##the functions given before are equivalent to the following pipeline functions
##there is 0 difference, but i think pipeline functions can take more specific arguments as input


## vectors ==== quiver3d
#src = mlab.pipeline.vector_field(vel_u, vel_v, vel_w)
#mlab.pipeline.vectors(src, mask_points=2147483647, scale_factor=3.)  #this is suppoused to reduce the number of points
                                                                      #but it cannot do it efficiently enough

## vector_cut_plane ==== quiver3d
#src = mlab.pipeline.vector_field(vel_u, vel_v, vel_w)              #this one is very nice
#mlab.pipeline.vector_cut_plane(src, mask_points=1, scale_factor=1.)
#mlab.outline()
#mlab.show()

## vector_field + iso_surface ==== 3d_contour
#src = mlab.pipeline.vector_field(vel_u, vel_v, vel_w)  #i have made this one to actually show the magnitude
#magnitude = mlab.pipeline.extract_vector_norm(src) 
#mlab.pipeline.iso_surface(magnitude)
#mlab.outline()
#mlab.show()

## scalar_field + iso_surface ==== contour3d
#src = mlab.pipeline.scalar_field(vel_u)
#mlab.pipeline.iso_surface(src)
#mlab.outline()
#mlab.show()



A=np.zeros((192, 192,192),dtype='object') #you need specify it as an object array

for i in range(192):
    for j in range(192):
        for k in range(192):
            A[i,j,k]=[vel_u[i,j,k],vel_v[i,j,k],vel_w[i,j,k]]
        
