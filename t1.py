import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Original array
arr = np.array([3, 7, 1, 9, 4, 6])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Initialize bar chart
bars = ax.bar(range(len(arr)), arr, color='blue')
ax.set_ylim(0, max(arr) + 2)
ax.set_title("Array Reversal Animation")

# Function to update the animation
def update(frame):
    global arr
    n = len(arr)
    i = frame
    if i < n // 2:
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]  # Swap elements

    for bar, height in zip(bars, arr):
        bar.set_height(height)  # Update bar heights

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(arr) // 2 + 1, interval=500, repeat=False)

plt.show()
