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
