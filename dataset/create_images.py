import os
import random

components = ["Voltage_Source", "Current_source", "Resistor", "Capacitor", "Inductor", "Diode", "BJT", "MOSFET", "OpAMP"]

sourcedir = "datasets/components"

for component in components:
    component_dir = os.path.join(sourcedir, component)

    image = random.choice(os.listdir(component_dir))
