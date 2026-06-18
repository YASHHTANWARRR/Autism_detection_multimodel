# Autism Detection using Multi-Model Deep Learning

## Overview

Autism Spectrum Disorder (ASD) is a neurodevelopmental condition that affects communication, social interaction, and behavior. Early identification can significantly improve intervention outcomes and quality of life.

This project presents a multi-model deep learning framework for autism detection using facial image analysis. Multiple convolutional neural network (CNN) architectures are trained independently and their predictions are combined to improve classification performance and robustness.

The objective is to leverage the strengths of different deep learning models and reduce the limitations associated with a single-model approach.

---

## Features

* Deep learning-based autism classification
* Multiple CNN architectures
* Ensemble prediction framework
* Image preprocessing and augmentation
* Training and evaluation pipelines
* Performance comparison between models
* Visualization of training metrics
* Modular and extensible implementation

---

## Models Used

The project utilizes multiple deep learning architectures, including:

* VGG16
* VGG19
* MobileNetV1
* EfficientNet-B4

The final prediction is generated using an ensemble strategy that combines outputs from individual models.

---

## Dataset

The project uses a facial image dataset containing images of:

* Children diagnosed with Autism Spectrum Disorder (ASD)
* Typically Developing (TD) children

### Dataset Structure

```text
dataset/
├── train/
│   ├── autistic/
│   └── non_autistic/
│
├── validation/
│   ├── autistic/
│   └── non_autistic/
│
└── test/
    ├── autistic/
    └── non_autistic/
```

---

## Project Workflow

```text
Dataset Collection
          │
          ▼
Image Preprocessing
          │
          ▼
Data Augmentation
          │
          ▼
Model Training
(VGG16, VGG19,
MobileNet, EfficientNet)
          │
          ▼
Individual Predictions
          │
          ▼
Ensemble Fusion
          │
          ▼
Final Classification
```

---

## Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* OpenCV
* Matplotlib
* Scikit-learn

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YASHHTANWARRR/Autism_detection_multimodel.git
cd Autism_detection_multimodel
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Training

Train an individual model:

```bash
python train.py
```

Adjust hyperparameters and dataset paths according to your environment.

---

## Evaluation

Evaluate trained models:

```bash
python evaluate.py
```

Metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC

---

## Ensemble Prediction

The ensemble module combines predictions from multiple models to generate a final classification.

Possible fusion methods include:

* Majority Voting
* Soft Voting
* Weighted Averaging

This approach improves robustness and generalization performance compared to individual models.

---

## Results

The multi-model architecture demonstrates improved classification performance compared to standalone CNN models by leveraging complementary feature representations learned by different networks.

Performance metrics may vary depending on dataset splits, augmentation settings, and training configurations.

---

## Future Work

* Vision Transformer (ViT) integration
* Explainable AI (Grad-CAM)
* Real-time webcam-based inference
* Mobile deployment
* Multimodal autism screening systems
* Federated learning approaches

---

## Disclaimer

This project is intended for research and educational purposes only. It is not designed to replace professional medical diagnosis or clinical assessment.

---

## Author

**Yash Tanwar**

Computer Engineering Undergraduate
Thapar Institute of Engineering and Technology

GitHub: https://github.com/YASHHTANWARRR
