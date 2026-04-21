# EuroSAT Land Cover Classifier

A PyTorch image classifier that categorizes 64x64 Sentinel-2 satellite tiles into 10 land-cover classes. Built using transfer learning on a pretrained ResNet18.

Land cover classification is used for envionmental applications like wetland delineation, vegetation mapping, and land use change detection.

<img width="384" height="344" alt="image" src="https://github.com/user-attachments/assets/d66528c8-2585-429e-9b35-cb7e90aa58fc" />


## What it does?

For any input satellite image tile, the model predicts one of 10 classes:

`AnnualCrop`, `Forest`, `HerbaceousVegetation`, `Highway`, `Industrial`, `Pasture`, `PermanentCrop`, `Residential`, `River`, `SeaLake`

## Approach

- **Transfer learning** from ImageNet pretrained ResNet18
- **Feature layers frozen**, only the final classifier head is trained
- **Trainable parameters**: ~5,000 out of ~11 million (0.05%)
- Input resized from 64x64 to 224x224 to match ResNet's expected input
- Data augmentation on training set: random horizontal and vertical flips
- ImageNet normalization (required to use the pretrained weights)

## Stack

- Python 3.13
- PyTorch, torchvision (ResNet18, dataloaders, transforms)
- scikit-learn (confusion matrix, classification report)
- matplotlib (visualization)
- PIL / Pillow (image loading)

# To run:
Open the notebook to train from scratch
jupyter notebook eurosat_classifier.ipynb
