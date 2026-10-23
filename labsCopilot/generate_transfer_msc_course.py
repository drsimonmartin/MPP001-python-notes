import json
from pathlib import Path
import pandas as pd

# =====================================================
# DIRECTORY SETUP
# =====================================================

ROOT = Path(".")
DATA_DIR = ROOT / "datasets"
DATA_DIR.mkdir(exist_ok=True)

# =====================================================
# CREATE DATASETS
# =====================================================

materials_density = pd.DataFrame({
    "material": ["Aluminium", "Steel", "Titanium", "Copper", "Magnesium"],
    "density_kgm3": [2700, 7850, 4500, 8960, 1740],
    "elastic_modulus_gpa": [69, 210, 116, 117, 45]
})

materials_density.to_csv(
    DATA_DIR / "materials_density.csv",
    index=False
)

materials_stress_strain = pd.DataFrame({
    "strain": [0.000,0.001,0.002,0.003,0.004,0.005],
    "stress_mpa": [0,210,420,620,740,790]
})

materials_stress_strain.to_csv(
    DATA_DIR / "materials_stress_strain.csv",
    index=False
)

patient_vitals = pd.DataFrame({
    "patient_id":[1,2,3,4,5],
    "heart_rate":[72,85,110,95,58],
    "resp_rate":[15,18,24,20,12],
    "spo2":[98,97,92,95,99]
})

patient_vitals.to_csv(
    DATA_DIR / "biomed_patient_vitals.csv",
    index=False
)

ecg = pd.DataFrame({
    "time":[0,1,2,3,4,5,6,7,8,9],
    "voltage":[0.10,0.14,0.20,0.85,0.18,0.10,0.12,0.82,0.20,0.09]
})

ecg.to_csv(
    DATA_DIR / "biomed_ecg.csv",
    index=False
)

speed_cycle = pd.DataFrame({
    "time_s":[0,1,2,3,4,5,6,7,8,9],
    "speed_ms":[0,2,4,6,8,10,10,9,8,7]
})

speed_cycle.to_csv(
    DATA_DIR / "auto_speed_cycle.csv",
    index=False
)

auto_mpg = pd.DataFrame({
    "vehicle":["A","B","C","D","E"],
    "weight_kg":[1100,1250,1500,1800,2200],
    "horsepower":[75,95,130,180,250],
    "mpg":[58,48,42,34,25]
})

auto_mpg.to_csv(
    DATA_DIR / "auto_mpg.csv",
    index=False
)

ev_battery = pd.DataFrame({
    "trip_km":[0,20,40,60,80,100],
    "battery_percent":[100,89,77,66,54,42]
})

ev_battery.to_csv(
    DATA_DIR / "ev_battery.csv",
    index=False
)

# =====================================================
# NOTEBOOK HELPERS
# =====================================================

def md(text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": text.splitlines(True)
    }

def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "outputs": [],
        "metadata": {},
        "source": text.splitlines(True)
    }

def notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

# =====================================================
# SHARED INTRODUCTION
# =====================================================

sources_cell = md("""
# Engineering Data Sources

## Materials Engineering

Materials Project
https://materialsproject.org

## Biomedical Engineering

MIMIC-IV Demo
https://physionet.org/content/mimic-iv-demo/

## Automotive Engineering

UCI Auto MPG
https://archive.ics.uci.edu/ml/datasets/Auto+MPG

FuelEconomy.gov
https://www.fueleconomy.gov/feg/download.shtml

Small teaching datasets are supplied locally in the
datasets directory.
""")

# =====================================================
# LAB 1
# =====================================================

lab1_cells = [
md("# Lab 1 - Python Fundamentals"),
sources_cell,
md("## Learning Outcomes"),
md("""
- Variables
- Mathematical operators
- Functions
- Engineering calculations
"""),

md("## Worked Example 1"),

code("""
mass = 12
volume = 0.005

density = mass / volume
print(density)
"""),

md("## Exercise 1"),

code("""
def calculate_density(mass, volume):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),

code("""
# Local test
# assert abs(calculate_density(10,0.005)-2000) < 1e-6
"""),

md("## Exercise 2 Biomedical"),

code("""
def calculate_bmi(weight, height):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),

md("## Exercise 3 Automotive"),

code("""
def calculate_vehicle_range(tank_size, consumption):

    # YOUR CODE HERE
    raise NotImplementedError()
""")
]

for i in range(4,16):
    lab1_cells.append(md(f"## Practice Exercise {i}"))
    lab1_cells.append(code("# Complete this engineering calculation"))

lab1_cells.append(md("## Reflection Questions"))
lab1_cells.append(md("""
1. Why is density important?
2. What assumptions are present in the BMI calculation?
3. What factors affect vehicle range?
"""))

# =====================================================
# LAB 2
# =====================================================

lab2_cells = [
md("# Lab 2 - Decisions and Logic"),
sources_cell,
md("## Materials Quality Control"),
code("""
def passes_tensile_test(strength):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
md("## Biomedical Monitoring"),
code("""
def classify_heart_rate(hr):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
md("## Automotive Battery Monitoring"),
code("""
def battery_alert(charge):

    # YOUR CODE HERE
    raise NotImplementedError()
""")
]

for i in range(1,14):
    lab2_cells.append(md(f"### Conditional Exercise {i}"))
    lab2_cells.append(code("# Write conditional logic here"))

# =====================================================
# LAB 3
# =====================================================

lab3_cells = [
md("# Lab 3 - Loops and Lists"),
sources_cell,
md("## Materials Measurements"),
code("""
strengths = [412,421,430,425,419]
"""),
code("""
def average_strength(values):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
code("""
def count_above_threshold(values, threshold):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
code("""
def find_maximum(values):

    # YOUR CODE HERE
    raise NotImplementedError()
""")
]

for i in range(1,15):
    lab3_cells.append(md(f"### Loop Exercise {i}"))
    lab3_cells.append(code("# Use a loop to solve this problem"))

# =====================================================
# LAB 4
# =====================================================

lab4_cells = [
md("# Lab 4 - NumPy for Engineers"),
sources_cell,
code("import numpy as np"),
md("## Stress Calculations"),
code("""
def calculate_stress(force, area):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
md("## ECG Processing"),
code("""
def normalise_signal(signal):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
code("""
def rms_value(signal):

    # YOUR CODE HERE
    raise NotImplementedError()
""")
]

for i in range(1,15):
    lab4_cells.append(md(f"### NumPy Exercise {i}"))
    lab4_cells.append(code("# Vectorised solution required"))

# =====================================================
# LAB 5
# =====================================================

lab5_cells = [
md("# Lab 5 - Pandas Engineering Data Analysis"),
sources_cell,
code("""
import pandas as pd

materials = pd.read_csv('datasets/materials_density.csv')
materials.head()
"""),
code("""
def average_modulus(df):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
code("""
vitals = pd.read_csv('datasets/biomed_patient_vitals.csv')
vitals.head()
"""),
code("""
def count_tachycardia(df):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
code("""
vehicles = pd.read_csv('datasets/auto_mpg.csv')
vehicles.head()
"""),
code("""
def most_efficient_vehicle(df):

    # YOUR CODE HERE
    raise NotImplementedError()
""")
]

for i in range(1,16):
    lab5_cells.append(md(f"### Data Analysis Exercise {i}"))
    lab5_cells.append(code("# Pandas solution"))

# =====================================================
# LAB 6
# =====================================================

lab6_cells = [
md("# Lab 6 - Engineering Modelling and Visualisation"),
sources_cell,
code("""
import numpy as np
import matplotlib.pyplot as plt
"""),
code("""
def drug_decay(c0, k, t):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
code("""
def battery_model(start_charge, consumption):

    # YOUR CODE HERE
    raise NotImplementedError()
"""),
code("""
def stress_strain_values(force, area):

    # YOUR CODE HERE
    raise NotImplementedError()
""")
]

for i in range(1,18):
    lab6_cells.append(md(f"### Modelling Exercise {i}"))
    lab6_cells.append(code("# Implement and analyse a model"))

lab6_cells.append(md("""
# Mini Project

Choose ONE pathway:

- Materials Engineering
- Biomedical Engineering
- Automotive Engineering

Write a short engineering report interpreting your results.
"""))

# =====================================================
# SAVE NOTEBOOKS
# =====================================================

notebooks = {
    "Lab_01_Python_Fundamentals.ipynb": notebook(lab1_cells),
    "Lab_02_Decisions_and_Logic.ipynb": notebook(lab2_cells),
    "Lab_03_Loops_and_Lists.ipynb": notebook(lab3_cells),
    "Lab_04_NumPy_for_Engineers.ipynb": notebook(lab4_cells),
    "Lab_05_Pandas_Data_Analysis.ipynb": notebook(lab5_cells),
    "Lab_06_Modelling_and_Visualisation.ipynb": notebook(lab6_cells)
}

for filename, nb in notebooks.items():
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

print("Created datasets and notebooks successfully.")
