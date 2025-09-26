# Circuit Detection Application

Currently over several python scrpits I can decode an image of a hand drawn image and return a Spice NETLIST. This was developed solo by myself during the summer. I plan to add an interface that has drag and drop functionality within some sort of frontend application.

**Ill use this example image to demonstrate the workflow.**

<p align="center">
  <img src="Assets/Demo_circuit.jpg" alt="DEMO" width="300" height="300">
</p>  

**The workflow consists of:**
1. Detection of components using an object detection model I have trained using my own synthetic data then finetuned using real data.

<p align="center">
  <img src="Assets/Demo_Ob_det.png" alt="DEMO_ob" width="300" height="300">
</p>  

2. Cleaning of the image to 'remove' the circuits and using CV2 library using the coordinates generated from the model
   
<p align="center">
  <img src="Assets/cleaned_circuit.png" alt="DEMO_clean" width="300" height="300">
</p>  

3. Now the image is cleaned, there are still the values on but this doesnt matter, as this cleaned image is passed into an instance segmentor to gather a bitmap of bundles of wires which represent nodes at this point where we have deleted the components we can the find where the components attach to these nodes and build the Netlist
