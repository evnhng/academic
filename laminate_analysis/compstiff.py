## Calculates the compliance and stiffness matrices for the laminate in local and global orientations. 
## 

import math
#from numpy import array, zeros, ones, arange, dot, linalg, cos, sin, transpose, radians
import numpy as np

def compstiff(E1, E2, v12, G12, theta):

    c = np.cos(theta)
    s = np.sin(theta)

    v21 = (E2 * v12)/E1

    T_eps = np.array([[c**2, s**2, c*s],[s**2, c**2, -c*s],[-2*c*s, 2*c*s, c**2-s**2]])

    T_sig = np.array([[c**2, s**2, 2*c*s],[s**2, c**2, -2*c*s],[-c*s, c*s, c**2-s**2]])

    S = np.array([[1/E1, -v12/E1, 0],[-v12/E1, 1/E2, 0],[0, 0, 1/G12]])

    Q = np.linalg.inv(S)

    S_bar = np.transpose(T_sig) @ S @ T_sig
    Q_bar = np.transpose(T_eps) @ Q @ T_eps
    print(Q_bar)

# compstiff(21.3, 1.5, 0.27, 1.0, np.radians(20))
# print(S_bar)
