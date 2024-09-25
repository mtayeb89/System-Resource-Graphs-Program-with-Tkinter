import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a Tkinter window
root = tk.Tk()
root.title("System Resource Graphs")

# Set window size
root.geometry("800x600")

# Create a tabbed layout
tab_control = ttk.Notebook(root)

# Create two tabs: CPU and Memory
cpu_tab = ttk.Frame(tab_control)
memory_tab = ttk.Frame(tab_control)

tab_control.add(cpu_tab, text="CPU Usage")
tab_control.add(memory_tab, text="Memory Usage")

tab_control.pack(expand=1, fill="both")

# Lists to hold data for plotting
cpu_usage_data = []
memory_usage_data = []

# Matplotlib figure and axes for CPU graph
fig_cpu, ax_cpu = plt.subplots()
ax_cpu.set_title("CPU Usage (%)")
ax_cpu.set_xlabel("Time (s)")
ax_cpu.set_ylabel("CPU Usage (%)")

# Matplotlib figure and axes for Memory graph
fig_memory, ax_memory = plt.subplots()
ax_memory.set_title("Memory Usage (%)")
ax_memory.set_xlabel("Time (s)")
ax_memory.set_ylabel("Memory Usage (%)")


# Update the CPU usage graph
def update_cpu_graph(i):
    cpu_usage_data.append(psutil.cpu_percent())

    if len(cpu_usage_data) > 60:
        cpu_usage_data.pop(0)

    ax_cpu.clear()
    ax_cpu.set_title("CPU Usage (%)")
    ax_cpu.set_xlabel("Time (s)")
    ax_cpu.set_ylabel("CPU Usage (%)")
    ax_cpu.plot(cpu_usage_data, color='blue')


# Update the Memory usage graph
def update_memory_graph(i):
    memory_usage_data.append(psutil.virtual_memory().percent)

    if len(memory_usage_data) > 60:
        memory_usage_data.pop(0)

    ax_memory.clear()
    ax_memory.set_title("Memory Usage (%)")
    ax_memory.set_xlabel("Time (s)")
    ax_memory.set_ylabel("Memory Usage (%)")
    ax_memory.plot(memory_usage_data, color='green')


# Create a canvas for CPU plot
canvas_cpu = FigureCanvasTkAgg(fig_cpu, master=cpu_tab)
canvas_cpu.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a canvas for Memory plot
canvas_memory = FigureCanvasTkAgg(fig_memory, master=memory_tab)
canvas_memory.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Animate the graphs every second
ani_cpu = animation.FuncAnimation(fig_cpu, update_cpu_graph, interval=1000)
ani_memory = animation.FuncAnimation(fig_memory, update_memory_graph, interval=1000)

# Run the Tkinter event loop
root.mainloop()
