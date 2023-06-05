
import matplotlib.pyplot as plt
import numpy as np
import binoutprogram as bin
import readcsv as rcsv

title = ['12ft pressure(psi) vs time (sec)', '24ft pressure(psi) vs time (sec)', '30ft pressure(psi) vs time (sec)']
xaxis = 'time (sec)'
yaxis = 'pressure (psi)'

shift = [0, 0, 0]

xmin = [0, 0, 0]
xmax = [5, 5, 5]

ymin = [0, 0, 0]
ymax = [2.3, 2.3, 2.3]

# File paths for simulation data
file_paths = [
    # 12 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.75_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v20000_blow_s300_ea0.75_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v25000_blow_s300_ea0.75_sim"
    ],
    # 24 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.75_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v20000_blow_s300_ea0.75_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v25000_blow_s300_ea0.75_sim"
    ],
    # 30 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.75_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v20000_blow_s300_ea0.75_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft drop\finished 24\drop_vent_d3.0_start1000_term2000_height24_blow_v25000_blow_s300_ea0.75_sim"
    ]
]

# File paths for CSV data
csv = [
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_30.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_30.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_30.csv"
]

H = 1
for i, paths in enumerate(file_paths):
    # Create a new figure
    plt.figure(H)

    # Plot the simulation data
    for file_path in paths:
        # Read time and pressure data from the simulation
        x = bin.get_ab(directory=file_path, val='time') / 1000 + shift[i]
        y = bin.get_ab(directory=file_path, val='pressure') * 145037.738 - 14.6959488

        # Convert data to NumPy arrays
        x = np.array(x)
        y = np.array(y)

        # Plot the simulation data
        plt.plot(x, y)

    # Read time and pressure data from the CSV file
    xreal, yreal = rcsv.read_csv_to_arrays(csv_file=csv[i], val1='Time (s)', val2='Pressure (psi)')

    # Plot the CSV data
    plt.plot(xreal, yreal)

    # Set the title, x-axis label, y-axis label, and grid
    plt.title(title[i])
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid(True)
    plt.legend(['0.1', '0.3', '0.5', 'Drop Test'])

    # Set the x and y axis limits
    plt.xlim(xmin[i], xmax[i])
    plt.ylim(ymin[i], ymax[i])

    # Show the plot
    plt.show()

    H += 1

print('done')
