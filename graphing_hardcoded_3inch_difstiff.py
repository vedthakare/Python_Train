import matplotlib.pyplot as plt
import numpy as np
import binoutprogram as bin
import readcsv as rcsv
import math

title = ['12ft', '24ft Acceleration vs Time', '30ft Acceleration vs Time']
xaxis = 'time (sec)'
yaxis = 'acceleration (g)'
shift = [0, .339-0.0922, .526-0.1044]
xmin = [0,1.2,1.4]
ymin =[-30,-30,-30]
xmax =[2,1.47,1.632]
ymax =[30,30,30]

# File paths for simulation data
file_paths = [
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\30ft drop\finished sim\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.5_sim",
r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\30ft drop\finished sim\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.75_sim",
r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\30ft drop\finished sim\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea1_sim"]

# File paths for CSV data
csv = [
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_32B.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_32B.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_32B.csv"
]

H = 1
for file_path in file_paths:
    # Create a new figure
    plt.figure(H)
    plt.xlim((xmin[H-1], xmax[H-1]))
    plt.ylim((-30, 30))

    # Read time and acceleration data from the simulation
    x = bin.get_ab(directory=file_path, val='time') / 1000 + shift[H - 1]
    y = bin.get_nod(directory=file_path, val='x_acceleration') * 1000 / 9.81

    # Convert data to NumPy arrays
    x = np.array(x)
    y = np.array(y)

    # Plot the simulation data
    plt.plot(x, y)

    # Read x, y, and z acceleration data from the simulation
    a = np.array(bin.get_nod(directory=file_path, val='x_acceleration'))
    b = np.array(bin.get_nod(directory=file_path, val='y_acceleration'))
    c = np.array(bin.get_nod(directory=file_path, val='z_acceleration'))

    # Calculate resultant acceleration using Euclidean norm
    y = ((np.sqrt(a**2 + b**2 + c**2)) * 1000) / 9.81

    # Plot the resultant acceleration
    plt.plot(x, y)

    # Read time and acceleration data from the CSV file
    xreal, yreal = rcsv.read_csv_to_arrays(csv_file=csv[H - 1], val1='Time (s)', val2='Chest Acceleration X (g)')

    # Plot the CSV data
    plt.plot(xreal, -yreal)

    # Set the title, x-axis label, y-axis label, and grid
    plt.title(title[H - 1])
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid(True)
    plt.legend(['x acceleration','resultant acceleration','real data'])

    # Show the plot
    plt.show()

    H = H + 1

print('done')
