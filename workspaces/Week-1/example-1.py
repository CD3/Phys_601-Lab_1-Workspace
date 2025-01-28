import numpy
import sys

def magnitude(x):
    return numpy.sqrt( dot(x,x) )

def dot(x,y):
    result = 0
    for i in range(len(x)):
        result += x[i]*y[i]
        
    return result

def cross(x,y):
    result = numpy.zeros([4])

    result[0] =  x[1]*y[2] - x[2]*y[1]
    result[1] = -x[0]*y[2] + x[2]*y[0]
    result[2] =  x[0]*y[1] - x[1]*y[0]

    return result

def parallel_component(x,y):
    '''
    compute the component of x that points along the direction of y
    '''
    return dot(x,y/magnitude(y))*y/magnitude(y)


def perpendicular_component(x,y):
    '''
    compute the component of x that points perpindicular to the direction of y
    '''
    return x - parallel_component(x,y)



u = numpy.zeros([3])
v = numpy.zeros([3])

u[0] = 1
u[1] = 1
u[2] = 1

v[0] = 1
v[1] = 1
v[2] = 0

print("u:",u)
print("v:",v)

print("Checking for sanity...")

u_mag = magnitude(u)
v_mag = magnitude(v)

if u_mag < 1e-10 or v_mag < 1e-10:
    print("One of the vectors appears to have zero length...")
    sys.exit(1)

# v x u should be perpindicualr to both u and v
v_dot_v_cross_u = dot(v,cross(v,u))
v_cross_u_dot_u = dot(cross(v,u),u)


if v_dot_v_cross_u > 0.1 or v_cross_u_dot_u > 0.1:
    print("Something is not right, u and v should both be perpindicular to u x v.")
    sys.exit(1)

print( "Computing the magnitude of the compoent of u that points along the direction of v")
print( "Retuls:" , magnitude(parallel_component(u,v)))
