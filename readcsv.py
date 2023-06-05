import pandas as pd

def read_csv_to_arrays(csv_file, val1='Time (s)', val2='Pressure (psi)'):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert the DataFrame columns to NumPy arrays
    array1 = df[val1].values
    array2 = df[val2].values

    return array1, array2


# # Example usage
# csv_file = r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\CFC1000_Drop_33.csv"  # Replace with the path to your CSV file
# array1, array2 = read_csv_to_arrays(csv_file)
#
# # Print the arrays
# print('Array 1:', array1)
# print('Array 2:', array2)

