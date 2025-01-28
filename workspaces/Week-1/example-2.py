import numpy
import sys



def magnitude(x):
    mod_squared = dot(x,x)
    if mod_squared < 0:
        print("Something is wrong, the magnitude squared of a vector cannot be negative.")
        sys.exit(1)
    mag = numpy.sqrt(mod_squared)

    
def dot(x,y):
    return sum(x*v)

def angle_between(x,y):
    '''
    Compute the angle between two vectors.

    Parameters
    ----------
    x : numpy.array
        A 3D vector.
    y : numpy.array
        A 3D vector.

    Returns
    -------
    Angle expressed in RADIAN.
    '''
    d = dot(x,y)
    cos_theta = d / magnitude(x) / magnitude(y)
    
    return numpy.arccos(cos_theta)
    
def rad2deg(x):
    return x*180/numpy.pi

xhat = numpy.array([1,0,0])
yhat = numpy.array([0,1,0])
zhat = numpy.array([0,0,1])


u = 2*xhat + 1*yhat
v = zhat + 2*yhat

print("u:",u)
print("v",v)

print("Angle between u and v:", angle_between(u,v),"rad = ",rad2deg(angle_between(u,v)),"deg")