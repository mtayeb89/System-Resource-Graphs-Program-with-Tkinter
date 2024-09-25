# System Resource Graphs Program

## Description
This Python program monitors and displays real-time system resource usage (CPU and memory) using a graphical interface. It shows the current percentage of CPU and memory usage as animated line graphs. The program is ideal for IT managers who need to visualize system performance in real-time.

## Features
- Real-time CPU and memory monitoring.
- Tabbed layout with separate tabs for CPU and memory usage graphs.
- Graphs update every second to reflect changes in system performance.

## Requirements
- **Python 3.x**
- **psutil**: To install, run `pip install psutil`
- **matplotlib**: To install, run `pip install matplotlib`
- **Tkinter**: Built-in with Python.

## Installation
1. **Install Required Libraries**:
   ```bash
   pip install psutil matplotlib
Run the Program: Navigate to the directory where the script is located and run:

bash

    python system_resource_graphs.py

Usage

    CPU Tab:
        The CPU Usage graph updates every second, showing the percentage of CPU utilization over time.
    Memory Tab:
        The Memory Usage graph updates every second, showing the percentage of memory used over time.

Example Output

    CPU Usage Graph: Displays real-time CPU usage on a percentage scale (Y-axis) over time (X-axis).

    Memory Usage Graph: Displays real-time memory usage, also as a percentage scale (Y-axis) over time (X-axis).

    نظرة عامة:

هذا البرنامج مكتوب بلغة Python ويستخدم مكتبة Tkinter لإنشاء واجهة رسومية تفاعلية، ومكتبة Matplotlib لعرض الرسوم البيانية التي تتتبع في الوقت الفعلي استخدام وحدة المعالجة المركزية (CPU) والذاكرة (RAM) في النظام. البرنامج مفيد جداً لمديري تقنية المعلومات لمراقبة أداء النظام بشكل سهل ومرئي.
المكتبات المستخدمة:

    Tkinter: لإنشاء واجهة المستخدم الرسومية (GUI).
    Matplotlib: لعرض الرسوم البيانية.
    psutil: لجمع بيانات النظام (استخدام المعالج والذاكرة).
    Matplotlib Animation: لتحديث الرسوم البيانية بشكل دوري، مما يجعلها تفاعلية.

شرح الكود بالتفصيل:
استيراد المكتبات:

python

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

    tkinter: لإنشاء النافذة والتبويبات.
    ttk: لتحسين مظهر العناصر الرسومية.
    FigureCanvasTkAgg: لدمج الرسوم البيانية التي تم إنشاؤها باستخدام Matplotlib في نافذة Tkinter.
    psutil: لجمع بيانات النظام مثل استخدام المعالج والذاكرة.
    matplotlib.pyplot: لإنشاء الرسوم البيانية.
    animation: لتحديث الرسوم البيانية في الوقت الفعلي.

إنشاء النافذة الرئيسية والتبويبات:

python

root = tk.Tk()
root.title("System Resource Graphs")
root.geometry("800x600")

tab_control = ttk.Notebook(root)

cpu_tab = ttk.Frame(tab_control)
memory_tab = ttk.Frame(tab_control)

tab_control.add(cpu_tab, text="CPU Usage")
tab_control.add(memory_tab, text="Memory Usage")

tab_control.pack(expand=1, fill="both")

    يتم إنشاء نافذة Tkinter وتحديد العنوان والحجم.
    يتم استخدام عنصر Notebook لإضافة تبويبات (CPU وMemory) داخل النافذة.

قوائم لحفظ البيانات الخاصة باستخدام النظام:

python

cpu_usage_data = []
memory_usage_data = []

    هنا يتم إنشاء قوائم فارغة لتخزين بيانات استخدام المعالج والذاكرة التي سيتم رسمها على الرسوم البيانية.

إعداد الرسوم البيانية للمعالج والذاكرة:

python

fig_cpu, ax_cpu = plt.subplots()
ax_cpu.set_title("CPU Usage (%)")
ax_cpu.set_xlabel("Time (s)")
ax_cpu.set_ylabel("CPU Usage (%)")

fig_memory, ax_memory = plt.subplots()
ax_memory.set_title("Memory Usage (%)")
ax_memory.set_xlabel("Time (s)")
ax_memory.set_ylabel("Memory Usage (%)")

    يتم إنشاء رسمين بيانيين: واحد لاستخدام المعالج (CPU) والآخر لاستخدام الذاكرة (RAM).
    set_title(): لتعيين عنوان الرسم البياني.
    set_xlabel() و set_ylabel(): لتعيين العناوين للمحورين السيني (الوقت) والصادي (نسبة الاستخدام).

تحديث رسم المعالج في الوقت الفعلي:

python

def update_cpu_graph(i):
    cpu_usage_data.append(psutil.cpu_percent())
    
    if len(cpu_usage_data) > 60:
        cpu_usage_data.pop(0)
        
    ax_cpu.clear()
    ax_cpu.set_title("CPU Usage (%)")
    ax_cpu.set_xlabel("Time (s)")
    ax_cpu.set_ylabel("CPU Usage (%)")
    ax_cpu.plot(cpu_usage_data, color='blue')

    psutil.cpu_percent(): يقوم بجلب نسبة استخدام المعالج.
    يتم تحديث الرسم البياني بإضافة البيانات الجديدة إلى القائمة.
    إذا تجاوز عدد البيانات 60، يتم إزالة أول قيمة للحفاظ على الرسم البياني بحجم ثابت.
    يتم إعادة رسم البيانات على الرسم البياني باستخدام ax_cpu.plot().

تحديث رسم الذاكرة في الوقت الفعلي:

python

def update_memory_graph(i):
    memory_usage_data.append(psutil.virtual_memory().percent)
    
    if len(memory_usage_data) > 60:
        memory_usage_data.pop(0)
        
    ax_memory.clear()
    ax_memory.set_title("Memory Usage (%)")
    ax_memory.set_xlabel("Time (s)")
    ax_memory.set_ylabel("Memory Usage (%)")
    ax_memory.plot(memory_usage_data, color='green')

    psutil.virtual_memory().percent: يقوم بجلب نسبة استخدام الذاكرة.
    مشابه لطريقة تحديث رسم المعالج، يتم تحديث الرسم البياني باستخدام نفس المنهجية.

إنشاء عناصر Canvas لعرض الرسوم البيانية في واجهة Tkinter:

python

canvas_cpu = FigureCanvasTkAgg(fig_cpu, master=cpu_tab)
canvas_cpu.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas_memory = FigureCanvasTkAgg(fig_memory, master=memory_tab)
canvas_memory.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    يتم دمج الرسوم البيانية التي تم إنشاؤها باستخدام Matplotlib داخل نافذة Tkinter باستخدام FigureCanvasTkAgg.

تحديث الرسوم البيانية بشكل دوري باستخدام animation:

python

ani_cpu = animation.FuncAnimation(fig_cpu, update_cpu_graph, interval=1000)
ani_memory = animation.FuncAnimation(fig_memory, update_memory_graph, interval=1000)

    FuncAnimation: تستخدم لتحديث الرسم البياني كل ثانية (interval=1000 يعني 1000 مللي ثانية = ثانية واحدة).
    يتم ربط وظيفة update_cpu_graph لتحديث رسم المعالج ووظيفة update_memory_graph لتحديث رسم الذاكرة.

بدء نافذة Tkinter:

python

root.mainloop()

    root.mainloop(): يدخل البرنامج في حلقة مستمرة ليظل التطبيق قيد التشغيل ويستجيب لتحديثات الرسوم البيانية.

كيف يعمل البرنامج:

    البرنامج يجمع بيانات النظام في الوقت الفعلي (استخدام المعالج والذاكرة).
    يتم عرض هذه البيانات على هيئة رسوم بيانية يتم تحديثها كل ثانية.
    الواجهة الرسومية تسهل على المستخدم التفاعل مع البرنامج ومعرفة أداء النظام بشكل مرئي وسهل.

المخرجات المتوقعة:

    رسم بياني يعرض نسبة استخدام المعالج (CPU) في تبويب CPU Usage.
    رسم بياني يعرض نسبة استخدام الذاكرة (RAM) في تبويب Memory Usage.
