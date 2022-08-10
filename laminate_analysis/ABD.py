import math
import numpy as np

def ABD(layup, h_ply, Q_bar):

    A = np.zeros(3,3)
    B = np.zeros(3,3)
    D = np.zeros(3,3)

    n_ply = len(layup)
    plies = []

    for i in range(1,n_ply+1):
        plies.append(i)

    h = n_ply * h_ply

    ## for loop
    ## for i = 1:n_ply:
        # z_bar(i) = -(h+h_ply)/2 + i*h_ply
        # A = A + Q_bar(:,:,i) * h_ply
        # B = B + Q_bar(:,:,i) * h_ply * z_bar(i)
        # D = D + Q_bar(:,:,i) *(h_ply * z_bar(i)^2 + h_ply^3 / 12)
    ## end

    for i in plies:
        z_bar = -(h + h_ply)/2 + i * h_ply 
        A = A + Q_bar * h_ply

    # print(z_bar)

    #ABD_mat = np.array([[A, B],[B, D]])

