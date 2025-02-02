import math
from ADCS_Constants import J_CS, RW_MOI

def rotisserie(j_cs, w_z, j_rw, w_rw):
        # Rotisserie function if we don't get TLE. This function will spin
        # the satellite along the z axis at a chosen rate (w_z_des) and
        # take pictures hoping to eventually get one while it's pointed at earth.
        # Desired angular momentum is determined using conservation of angular
        # momentum.

        # Variables:                                    Equation        Variable
        # Moment of Inertia of Reaction Wheel           Irw     =       j_rw
        # Moment of Inertia of Cube Sat                 Ics     =       j_cs
        # Initial Angular Speed of Reaction Wheel       Ωrw1    =       w_rw
        # Initial Angular Speed of Cube Sat             Ωcs1    =       w_z
        # Desired Angular Speed of Cube Sat             Ωcs2    =       w_z_desired
        # Desired Angular Speed of Reaction Wheel       Ωrw2    =       w_rw_desired  


        #Enter desired CUBESAT angular momentum in RAD/S:
        # The 5 is deg/sec and completely arbitrary. Feel free to change it.
        w_z_des = (5*math.pi)/180 #rad/s

        w_rw_desired = ((j_cs * (w_z - w_z_des)) + (j_rw * w_rw)) / j_rw

        return w_rw_desired

        # INSERT    P H O T O G R A P H Y

# test case
w_z = 0
w_rw = 100
rotisserie(J_CS, w_z, RW_MOI, w_rw)


# Yuvraj Jadav
