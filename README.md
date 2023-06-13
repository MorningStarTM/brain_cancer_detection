
# Brain Tumor Classification

This project focuses on the development of a deep learning model for brain tumor classification. The goal is to accurately classify brain tumor images into different categories, such as glioma or meningioma or pituitary or notumor using state-of-the-art deep learning techniques. 

# Actives
* Dataset Collection: A dataset of brain tumor images is collected from kaggle. The dataset consists of 4 types of tumor such are  glioma, meningioma, pituitary and notumor images, ensuring a diverse representation of brain tumor cases.


* Data Preprocessing: The collected dataset is preprocessed to prepare it for training. This includes tasks such as resizing images and normalizing pixel values.

* Model Selection: Different deep learning architectures, such as ResNet, VGG and custom model are evaluated for their performance on the brain tumor classification task. The model selection process involves training and evaluating these models using appropriate evaluation metrics.

* Model Training: The chosen deep learning model is trained on the preprocessed dataset.The aim is to achieve high accuracy and generalization on unseen brain tumor images.

* Model Evaluation: The trained model is evaluated using  evaluation metrics such as accuracy and confusion matrix. The model's performance is assessed on a separate test dataset to measure its effectiveness in classifying brain tumor images.




## Explainable AI for Model Interpretability using LIME
This project focuses on enhancing the interpretability of machine learning models using an Explainable AI (XAI) technique called LIME (Local Interpretable Model-Agnostic Explanations). The goal is to provide meaningful explanations for the predictions made by complex machine learning models, thereby increasing trust, transparency, and understanding of the underlying decision-making process.

* Model Development: A machine learning model, is trained on a brain tumor classification. The model serves as the black box whose predictions we aim to interpret using LIME.

* LIME Implementation: The LIME algorithm is implemented to generate local explanations for individual predictions made by the model. LIME approximates the behavior of the black box model by creating interpretable surrogate models on local subsets of the data. These surrogate models provide insights into how the black box model arrives at its predictions.


## DataSet
https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset

## Models
* Custom CNN Model 
* VGG-16


## Inteprete the model using LIME - XAI

### 1st Explaination of XAI
![App Screenshot](https://github.com/MorningStarTM/brain_cancer_detection/blob/main/screenshots/XAI-2.PNG?raw=true)

### 2nd Explaination of XAI
![App Screenshot](https://github.com/MorningStarTM/brain_cancer_detection/blob/main/screenshots/XAI-3.PNG?raw=true)

### 3rd Explaination of XAI
![App Screenshot](https://github.com/MorningStarTM/brain_cancer_detection/blob/main/screenshots/XAI.PNG?raw=true)

### Confusion matrix for explaining the accuracy of model
![App Screenshot](https://github.com/MorningStarTM/brain_cancer_detection/blob/main/screenshots/cm.PNG?raw=true)

