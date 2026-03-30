import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file):
    try:
        # Read dataset
        data = pd.read_csv(file)

        print("\nDataset Preview:\n")
        print(data.head())

        # Ask user which columns to plot
        x_col = input("\nEnter column name for X-axis: ")
        y_col = input("Enter column name for Y-axis: ")

        # Plot
        plt.figure()
        plt.plot(data[x_col], data[y_col], marker='o')

        plt.title(f"{y_col} vs {x_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)

        plt.grid()

        plt.show()

    except Exception as e:
        print("Error:", e)


# Input file
file = input("Enter CSV file name: ")

visualize_data(file)