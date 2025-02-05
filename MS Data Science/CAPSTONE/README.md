# 🧠 Brain Tumor Diagnosis Using Deep Learning  

## **Author**  
**Swetha Yanamandhalla**  
**Date**: May 3, 2024  

## **Project Overview**  
This repository contains deep learning models for **brain tumor classification and segmentation** using MRI scans. By leveraging **Convolutional Neural Networks (CNNs), ResNet-50, and VGG19**, we explore how different architectures perform in diagnosing brain tumors. The project demonstrates **custom model building, transfer learning, and model interpretability** through various techniques.  

---  

## **Repository Structure**  

### 📂 **1. `CNN.ipynb` - Custom CNN Model**  
This notebook walks through the creation of a **Convolutional Neural Network (CNN) from scratch** for tumor classification.  

🔹 **Key Highlights:**  
✔️ Designing a **custom CNN architecture** for image classification  
✔️ **Preprocessing & Augmentation**: Optimizing MRI images for training  
✔️ **Training & Optimization**: Using Adam optimizer and categorical cross-entropy loss  
✔️ **Performance Metrics**: Accuracy, loss visualization, and confusion matrix  

👀 **Why Use This?**  
Perfect for understanding **how CNNs process medical images** and their core functionality.  

---  

### 📂 **2. `RESNET50.ipynb` - Transfer Learning with ResNet-50**  
This notebook implements **ResNet-50**, a pre-trained model known for its efficiency in **image recognition tasks**.  

🔹 **Key Highlights:**  
✔️ **Transfer Learning**: Fine-tuning ResNet-50 for MRI classification  
✔️ **Data Augmentation**: Improving generalization with transformations  
✔️ **Performance Evaluation**: Confusion matrix, precision-recall, and accuracy metrics  
✔️ **Advanced Features**: Learning rate scheduling and dropout layers for better regularization  

👀 **Why Use This?**  
ResNet-50 helps improve model accuracy with **fewer labeled images** and speeds up training.  

---  

### 📂 **3. `VGG19.ipynb` - Deep Feature Extraction with VGG19**  
This notebook applies **VGG19**, a deeper network that excels at feature extraction.  

🔹 **Key Highlights:**  
✔️ Understanding the **layer-by-layer functionality** of VGG19  
✔️ **Fine-Tuning & Optimization**: Hyperparameter tuning for better predictions  
✔️ **Model Interpretability**: Using **Grad-CAM** to visualize which areas influence model decisions  
✔️ **Performance Metrics**: Accuracy comparison and validation scores  

👀 **Why Use This?**  
Great for exploring **deep network architectures** and their ability to capture intricate patterns in MRI images.  

---  

## **Installation & Setup**  

### **🔧 Requirements**  
Ensure you have the following dependencies installed:  
- **Python 3.7+**  
- **TensorFlow / PyTorch** (choose based on your preference)  
- **NumPy, Matplotlib, scikit-learn** for analysis  
- **Jupyter Notebook** for running and experimenting  
- **OpenCV / PIL** for image processing  

### **📥 Install Dependencies**  
Run the following command to install required packages:  
```bash
pip install -r requirements.txt
```  

---

## **How to Use This Project**  

1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/your-repo/brain-tumor-diagnosis.git  
cd brain-tumor-diagnosis  
```  

2️⃣ **Open the Notebooks**  
```bash
jupyter notebook CNN.ipynb  
```  
or  
```bash
jupyter notebook RESNET50.ipynb  
```  

3️⃣ **Follow the Instructions in the Notebook**  
Each notebook contains step-by-step guidance on **loading data, training the model, and evaluating performance**.  

---

## **How You Can Contribute**  

 Found a way to improve accuracy?  
 Have an idea for enhancing model interpretability?  
 Want to experiment with different architectures?  

Feel free to **fork the repository**, make your improvements, and submit a **pull request**! Contributions are always welcome.  

---

## **license**  
This project is **open-source** and licensed under the **MIT License**. Check the `LICENSE` file for more details.  

---

## Contact
For any inquiries or suggestions, feel free to reach out:
- **Name**: Swetha
- **Email**: swethachowdhary33@gmail.com
- **GitHub**: [SWETHAY9](https://github.com/swethay9)


🔹 **Happy coding and happy learning!** 🧠✨
