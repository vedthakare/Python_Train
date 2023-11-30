import matplotlib.pyplot as plt
import numpy as np
import binoutprogram as bin
import readcsv as rcsv
import os

title = ['12ft pressure (psi) vs time (sec)', '24ft pressure (psi) vs time (sec)', '30ft pressure (psi) vs time (sec)']
xaxis = 'time (sec)'
yaxis = 'pressure (psi)'

#shift = [-0.0934, [0.253-0.0269,0.253-0.0269-0.0117,0.253-0.0269,0.253-0.0269-0.0117,0.253-0.0269,0.253-0.0269-0.0117], 0.41]
shift = [-0.0934, 0.24+0.0136, 0.41]

xmin = [0.75, 1.15, 1.35]
xmax = [1.35, 1.55, 1.7]

ymin = [0, 0, 0]
ymax = [1.4,2.25, 2.5]

# File paths for simulation data
# file_paths = [
#     # 12 ft
#     [
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
#     [ r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\drop_vent_d3.0_start1000_term2000_height24_blow_v20000_blow_s300_ea0.1_sim",
#         r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\drop_vent_d3.0_start1000_term2000_height24_blow_v25000_blow_s300_ea0.1_sim"
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
file_paths = [
    # 12 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\12ft\drop_vent_d3.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.1_sim",

    ],


    # 24 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\drop_vent_d3.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.1_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\drop_vent_d3.0_start1000_term2000_height24_blow_v20000_blow_s300_ea0.1_sim",
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\wheight\Blower_VENT_CASES\finished\drop_vent_d3.0_start1000_term2000_height24_blow_v25000_blow_s300_ea0.1_sim"

    ],
    # 30 ft
    [
        r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\new_drop_3in_varting_ea_diff_heights\finished sims\30ft\drop_vent_d3.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.1_sim",


    ]
]


# File paths for CSV data
#12ft 29b
#24ft 30b
# weight drop
#20ft 33b
# csv = [
#     r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_29.csv",
#     r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_30.csv",
#     r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_33.csv"
# ]

csv = [
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_29.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_35.csv",
    r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\csv\CFC1000_Drop_33.csv"
]

H = 1
for i, paths in enumerate(file_paths):
    # Create a new figure
    plt.figure(i+1)

    # Plot the simulation dataa
    for f, file_path in enumerate(paths):
        # Read time and pressure data from the simulation
        if i == 1:
            x = bin.get_ab(directory=file_path, val='time') / 1000 + shift[i]#[f]
        else:
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
    if i == 1:
        plt.legend(['14000','20000','25000', 'Drop Test'])
    else:
        plt.legend(['Simulation', 'Drop Test'])
    # plt.legend(['Simulation_old_dummy','simulation_new_dummy', 'Drop Test'])

    # Set the x and y axis limits
    # plt.xlim(xmin[i], xmax[i])
    # plt.ylim(ymin[i], ymax[i])

    # Show the plot
    plt.show()
    # # Specify the directory and filename
    # directory = r"C:\Users\ved.thakare\OneDrive - University of Virginia\Pictures\final-plots-6-13\pressure"
    # filename = title[i] +'.png'
    #
    # # Create the directory if it doesn't exist
    # if not os.path.exists(directory):
    #     os.makedirs(directory)
    #
    # # Save the figure to the specific path
    # save_path = os.path.join(directory, filename)
    # plt.savefig(save_path)
    # H += 1

print('done')
