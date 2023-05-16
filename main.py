### Graphical User Interface
### all coded and debugged together with help from Amanda, 8 hours

import psychopy
import numpy as np
import tkinter as tk
from tkinter import messagebox
import os
import subprocess

def run_experiment1():
    subprocess.call(["python", "LDT_results!.py"]) #calling Maizy's experiment

def run_experiment2():
    subprocess.call(["python", "rotation_experiment.py"]) # calling Liv's experiment

def run_experiment3():
    subprocess.call(["python", "stroop_experiment_final.py"]) #calling Sophia's experiment

root = tk.Tk()
root.title("PsychoPy Experiments")

experiment1_button = tk.Button(root, text="Lexical Decision Task", command=run_experiment1)
experiment1_button.pack(fill=tk.X)

experiment2_button = tk.Button(root, text="Mental Rotation Task", command=run_experiment2)
experiment2_button.pack(fill=tk.X)

experiment3_button = tk.Button(root, text="Stroop Task", command=run_experiment3)
experiment3_button.pack(fill=tk.X)

root.mainloop()
