from easipy.easing import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_easing(index):
    easing_types = ['Exponential', 'Quad', 'Back', 'Bounce', 'Elastic', 'Sine', 'Circ', 'Cubic', 'Quart', 'Quint']
    easing_type = easing_types[index]
    
    easing_class = get_easing_class(easing_type)()
    t_values = np.linspace(0, 1, 500)
    in_values = [easing_class.in_(t) for t in t_values]
    out_values = [easing_class.out(t) for t in t_values]
    in_out_values = [easing_class.in_out(t) for t in t_values]
    out_in_values = [easing_class.out_in(t) for t in t_values]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(t_values, in_values, label='In')
    ax.plot(t_values, out_values, label='Out')
    ax.plot(t_values, in_out_values, label='InOut')
    ax.plot(t_values, out_in_values, label='OutIn')
    ax.set_title(f'Easing Functions: {easing_type}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    
    root = tk.Tk()
    root.withdraw()
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800
    window_height = 600
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    window = tk.Toplevel(root)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')
    window.title(f'Plot: {easing_type}')
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def next_example():
        nonlocal index
        index += 1
        if index >= len(easing_types):
            index = 0
        window.destroy()
        plot_easing(index)

    next_button = tk.Button(window, text="Next example", command=next_example)
    next_button.pack(side=tk.BOTTOM, pady=10)
    
    window.mainloop()

easing_types = ['Exponential', 'Quad', 'Back', 'Bounce', 'Elastic', 'Sine', 'Circ', 'Cubic', 'Quart', 'Quint']
current_index = 0
plot_easing(current_index)