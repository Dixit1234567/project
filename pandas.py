import matplotlib.pyplot as plt

def plot_simple_line():
    # Data for the plot (x and y values)
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 1, 3, 5]

    # Create the plot
    plt.plot(x_values, y_values, marker='o', linestyle='-')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_simple_line()
