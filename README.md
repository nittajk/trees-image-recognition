# Tree species image classifier

This project is a deep learning image recognition system for classifying tree species using transfer learning with a ResNet18 model. The project was completed as part of a school course focused on machine learning and image processing.

## Overview

The goal was to build a machine learning model that can recognize different tree species based on image data. We collected our own dataset of tree images and fine-tuned a pre-trained ResNet18 model using PyTorch.

## The model

- Pre-trained ResNet18 (transfer learning)
- Modified final fully-connected layer for 6 tree species
- Trained using cross-entropy loss and Adam optimizer
- Implemented training/validation loops and confusion matrix evaluation

## 🌳 Classes
- kataja (juniper)
- koivu (birch)
- kuusi (spruce)
- mänty (pine)
- pihlaja (rowan)
- vaahtera (maple)

## Features

- Visualization using confusion matrix
- The trained model can perform inference on a single image to predict the tree species. A simple interactive UI built with Gradio allows users to upload an image and get an instant prediction in real time.
  
## Technologies

- Python
- PyTorch
- torchvision
- scikit-learn
- matplotlib
- Gradio


## Contributors

This project was completed as a group assignment at HAMK University of Applied Sciences. Each member contributed to data collection, coding, model tuning, and presentation.


