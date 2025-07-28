# Game-Bot-Training-ML
# 🤖 AI Game Bot for 2D Fighting Game – MLP-Based Action Prediction

A machine learning-powered bot trained to mimic player behavior in a 2D fighting game. The bot uses real-time game state data to predict and simulate player button presses using a **Multi-Layer Perceptron (MLP)** model trained on historical gameplay.

---

## 🚀 Key Features

### 🎮 Real-Time Action Prediction  
- Predicts player button combinations (A, B, X, Y, etc.) based on current game state  
- Supports dynamic behavior for both Player 1 and Player 2

### 🧠 Deep Learning with MLP  
- Trained using a custom neural network built with **TensorFlow/Keras**  
- Uses `binary_crossentropy` loss for multi-label classification  
- Trained on realistic gameplay collected through manual keyboard inputs

### 📦 Data Pipeline  
- Preprocessed gameplay logs from `GameState.csv`  
- Cleans and scales data, handles missing values, normalizes input features  
- Applies threshold-based binary conversion to model predictions

### 🎯 Button Mapping & Automation  
- Maps predictions directly to virtual button states using custom logic  
- Simulates real player control using keyboard-style mappings (left, right, jump, crouch, etc.)

---

## 🛠 Technologies Used

- Python  
- Pandas, NumPy, CSV – for data preprocessing  
- TensorFlow, Keras – for model building and training  
- Matplotlib – for training visualization  
- Custom keyboard & game command classes – for in-game input control  

---

## 🧠 Concepts Practiced

- ✅ Binary multi-label classification for button prediction  
- ✅ Neural network training with validation and early stopping  
- ✅ Game state parsing and CSV-based learning  
- ✅ Action simulation through predicted button states  
- ✅ Real-time AI bot behavior in fighting game scenarios  

---

