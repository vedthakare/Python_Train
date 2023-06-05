from lasso.dyna import d3plot, ArrayType, Binout
import os


def get_ab(directory: str = r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\finished sim\drop_vent_d3.0_start500_term2000_height6.0_blow_v25000_blow_s300_ea5_sim", val: str = 'pressure'):
    """
    Open key file and convert to string
    :param directory: (string)
    :param val: (string) - optional parameter with default value 'pressure'
    :return: ab[:,3]
    """
    val = str(val)
    path = os.path.join(directory, 'binout0000')
    binout = Binout(path)

    ab = binout.read('abstat', val)
    if val == 'time':
        return ab
    return ab[:, 3]

def get_nod(directory: str = r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\finished sim\drop_vent_d3.0_start500_term2000_height6.0_blow_v25000_blow_s300_ea5_sim", val: str = 'x_acceleration'):
    """
    # for val it can be x_acceleration or resultant_acceleration
    Open key file and convert to string
    :param directory: (string)
    :param val: (string) - optional parameter with default value 'pressure'
    :return: ab[:,3]
    """
    val = str(val)
    path = os.path.join(directory, 'binout0000')
    binout = Binout(path)

    nod = binout.read('nodout', val)
    if val == 'time' or val == 'resultant_acceleration':
        return nod
    return nod[:, 1]


get_nod(val='resultant_acceleration')
