# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 10:57:41 2025

@author: VK
"""
#chatGPT numerical method to calculate view factor
import numpy as np

# Plate dimensions
plate1_width = 1.0
plate1_height = 1.0
plate2_width = 2.0
plate2_height = 5.0

# Distance between plates
H = 2.0

# Number of divisions for numerical integration
nx1, ny1 = 40, 40  # plate 1
nx2, ny2 = 80, 200  # plate 2

# Create grid of points on each plate (center of each differential area)
x1 = np.linspace(-plate1_width/2, plate1_width/2, nx1)
y1 = np.linspace(-plate1_height/2, plate1_height/2, ny1)
x2 = np.linspace(-plate2_width/2, plate2_width/2, nx2)
y2 = np.linspace(-plate2_height/2, plate2_height/2, ny2)

dx1 = plate1_width / nx1
dy1 = plate1_height / ny1
dx2 = plate2_width / nx2
dy2 = plate2_height / ny2

dA1 = dx1 * dy1
dA2 = dx2 * dy2

F12_total = 0.0

# Numerical integration
for xi in x1:
    for yi in y1:
        for xj in x2:
            for yj in y2:
                S2 = (xi - xj)**2 + (yi - yj)**2 + H**2
                dF = dA2 * H**2 / (np.pi * S2**2)
                F12_total += dF

# Normalize by area of plate 1
F12 = F12_total / (plate1_width * plate1_height)

print(f"Numerical view factor F12: {F12:.4f}")