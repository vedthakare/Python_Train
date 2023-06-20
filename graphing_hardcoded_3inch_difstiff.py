import matplotlib.pyplot as plt
import numpy as np
import binoutprogram as bin
import readcsv as rcsv
import os
title = ['12ft accel(g) vs time (sec)', '24ft accel (g) vs time (sec)', '30ft accel (g) vs time (sec)']
xaxis = 'Time (sec)'
yaxis = 'Acceleration (g)'

shift = [-0.0953, [ 0.225, 0.225-0.01616, 0.225, 0.225-0.01616, 0.225, 0.225-0.01616], 0.41]

shift_new = [0,0,0]

xmin = [0.85, 1.2, 1.38]
xmax = [1.25, 1.475, 1.625]

ymin = [-2, -2, -2]
ymax = [25, 25, 25]

# File paths for simulation data
# file_paths = [
#     # 12 ft
#     [
#
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.3_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.5_sim"
#     ],
#     # 24 ft
#     [
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\drop_6_7_0.01_to_0.1\finished sim\drop_6_7_0.01_to_0.1\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.01_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\drop_6_7_0.01_to_0.1\finished sim\drop_6_7_0.01_to_0.1\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.05_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\24ft\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\24ft\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.3_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\24ft\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.5_sim"
#     ],
#     # 30 ft
#     [
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.3_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.5_sim"
#     ]
# ]

# file_paths = [
#     # 12 ft
#     [
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.3_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.5_sim"
#     ],
#     # 24 ft
#     [r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\24ft\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\drop_vent_d3.0_start1000_term2000_height24.0_blow_v20000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\drop_vent_d3.0_start1000_term2000_height24.0_blow_v25000_blow_s300_ea0.1_sim",
#          r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\drop_vent_d3.0_start1000_term2000_height24.0_blow_v30000_blow_s300_ea0.1_sim",
#          r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\drop_vent_d3.0_start1000_term2000_height24.0_blow_v35000_blow_s300_ea0.1_sim",
#          r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\drop_vent_d3.0_start1000_term2000_height24.0_blow_v40000_blow_s300_ea0.1_sim"
#
#     ],
#     # 30 ft
#     [
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.3_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.5_sim"
#     ]
# ]


# file_paths = [
#     # 12 ft
#     [
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.3_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.5_sim"
#     ],
#     # 24 ft
#     [   r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\Blower_VENT_CASES\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.1_simw",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\Blower_VENT_CASES\drop_vent_d3.0_start1000_term2000_height24_blow_v20000_blow_s300_ea0.1_simw",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\Blower_VENT_CASES\drop_vent_d3.0_start1000_term2000_height24_blow_v25000_blow_s300_ea0.1_simw"
#     ],
#     # 30 ft
#     [
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.3_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.5_sim"
#     ]
# ]


file_paths = [
    # 12 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.1_sim",

    ],


    # 24 ft
    [   r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\24ft\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.1_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\newdummytests\blowertestsea0.1\finished\blowertestsea0.1\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.1_sim",

        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft ea 0.1\Finished Sims\drop_vent_d3.0_start1000_term2000_height24.0_blow_v20000_blow_s300_ea0.1_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\newdummytests\blowertestsea0.1\finished\blowertestsea0.1\drop_vent_d3.0_start1000_term2000_height24_blow_v20000_blow_s300_ea0.1_sim",

        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\24ft ea 0.1\Finished Sims\drop_vent_d3.0_start1000_term2000_height24.0_blow_v25000_blow_s300_ea0.1_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\newdummytests\blowertestsea0.1\finished\blowertestsea0.1\drop_vent_d3.0_start1000_term2000_height24_blow_v25000_blow_s300_ea0.1_sim"

    ],
    # 30 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.1_sim",


    ]
]

# File paths for CSV data
#12ft 29b
#24ft 30b
#20ft 33b
csv = [
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_29b.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_30b.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_33b.csv"
]


H = 1
for i, paths in enumerate(file_paths):
    # Create a new figure
    plt.figure(H)

    # Plot the simulation data
    for f, file_path in enumerate(paths):
        # Read time and pressure data from the simulation
        if i == 1:
            x = bin.get_ab(directory=file_path, val='time') / 1000 + shift[i][f]
        else:
            x = bin.get_ab(directory=file_path, val='time') / 1000 + shift[i]
        if f == 1 or f == 3 or f == 5:
            y= bin.get_nod_new_dummy(directory=file_path,val='x_acceleration') * 1000 / 9.81
        else:
            y = bin.get_nod(directory=file_path, val='x_acceleration') * 1000 / 9.81
        print(f)
        # Convert data to NumPy arrays
        x = np.array(x)
        y = np.array(y)

        # Plot the simulation data
        plt.plot(x, y)

    # Read time and pressure data from the CSV file
    xreal, yreal = rcsv.read_csv_to_arrays(csv_file=csv[i], val1='Time (s)', val2='Chest Acceleration X (g)')

    # Plot the CSV data
    plt.plot(xreal, -yreal)

    # Set the title, x-axis label, y-axis label, and grid
    plt.title(title[i])
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid(True)
    # if H == 2:
    if i == 1:
        plt.legend(['14000_old','14000_new','20000_old','20000_new','25000_old','25000_new', 'Drop Test'])
    else:
        plt.legend(['Simulation', 'Drop Test'])
    # else:
    #     plt.legend(['Simulation', 'Drop Test'])
    # Set the x and y axis limits
    # plt.xlim(xmin[i], xmax[i])
    # plt.ylim(ymin[i], ymax[i])

    # Show the plot
    plt.show()
    # # Specify the directory and filename
    # directory = r"C:\Users\ved.thakare\OneDrive - University of Virginia\Pictures\final-plots-6-13\acceleration"
    # filename = title[i] +'.png'

    # Create the directory if it doesn't exist
    # if not os.path.exists(directory):
    #     os.makedirs(directory)
    #
    # # Save the figure to the specific path
    # save_path = os.path.join(directory, filename)
    # plt.savefig(save_path)
    H += 1


print('done')
