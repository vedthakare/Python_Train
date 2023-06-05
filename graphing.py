

import matplotlib.pyplot as plt
import numpy as np
import binoutprogram as bin
import readcsv as rcsv

def plot_multiple_graphs(file_paths:str,csv:str,shift:float = 0,title:str = "graph",xaxis:str='x',yaxis:str='y'):
    #
    """
    Plots multiple graphs iteratively from an array of file paths.

    Args:
        file_paths (list): The list of file paths containing data for the graphs.
        csv takes a string where the real data is at
        shift is to move the simulation plots to the correct position when comparing real from sim
        title, xaxis, yaxis takes on strings to label the graph

    """
    for file_path in file_paths:
        plt.figure(1)
        plt.xlim((0,2))
        try:
            # Read data from file
            x = bin.get_ab(directory=file_path,val='time')/1000 + shift
            y= bin.get_ab(directory=file_path,val='pressure')# Assuming the data is in CSV format
            x = np.array(x)
            y = (np.array(y)*145037.738)-14.6959488
            # Extract x and y data

            # Plot the graph
            plt.plot(x, y)
            plt.grid(True)

        except FileNotFoundError:
            print("File not found:", file_path)
        except Exception as e:
            print("An error occurred while plotting the graph:", e)
    xreal, yreal = rcsv.read_csv_to_arrays(csv_file=csv)
    plt.plot(xreal, yreal)
    plt.title(title)  # Replace with your desired title
    plt.xlabel(xaxis)  # Replace with your desired x-axis label
    plt.ylabel(yaxis)  # Replace with your desired y-axis label
    plt.grid(True)
    plt.show()
file_paths = [r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\4inch\finished sim\drop_vent_d4.0_start1000_term2000_height12_blow_v14000_blow_s300_ea0.75_sim",
r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\4inch\finished sim\drop_vent_d4.0_start1000_term2000_height24_blow_v14000_blow_s300_ea0.75_sim",
r"C:\Users\ved.thakare\OneDrive - University of Virginia\Non Vanilla\4inch\finished sim\drop_vent_d4.0_start1000_term2000_height30_blow_v14000_blow_s300_ea0.75_sim",]

plot_multiple_graphs(file_paths,r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\CFC1000_Drop_33.csv",.4,'graph name','xaxis','yaxis')
plt.legend(['x acceleration','resultant acceleration','real data'])
#plot Drop 28,31,32


