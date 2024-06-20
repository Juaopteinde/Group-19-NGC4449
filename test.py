import numpy as np

def boem(i, zp):
    c = 10**(((i-zp)/-2.5)+ np.log10(60))
    return c

list = (27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0)
zp = 26.38663145 + 0.0598

    


def std_mag(image, err_zp):
    return np.sqrt(((2.5*np.sqrt(image))/image*np.log(10))**2 + err_zp**2)

for i in list:
    print(f'f = {i} geeft {std_mag(boem(i, zp), 0.208442291)}')