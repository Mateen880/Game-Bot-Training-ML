import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam

from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

path = "GameState.csv" 
df = pd.read_csv(path)

print("Original data shape:", df.shape)
print(df.info())
# print("Null values before cleaning:", df.isnull().sum().sum())

# # data cleaning
df = df[~df['fight_result'].isin(['P2 ', 'P1'])]
print(df.head(4))
df.drop(columns=['fight_result', 'Player1_move_id', 'Player2_move_id'], inplace=True)
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            # Try converting to numeric (float/int)
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            # Skip columns that can't be converted (e.g., strings like 'Yes', 'No')
            print(f"Skipped column: {col}")


df = df.replace(True, 1)
df = df.replace(False, 0)
print(df.info())


# handle missing values before proceeding
print("null values after initial cleaning:", df.isnull().sum().sum())
df.dropna(inplace=True)
print("final data shape after cleaning:", df.shape)

# Feature scaling
columns = df.columns
for col in columns:
    if col in ['Player1_player_id', 'Player2_player_id']:
        df[col] = df[col] / 100
        continue
    
    maxVal = df[col].max()
    if maxVal > 1: 
        df[col] = df[col] / maxVal 

#  output columns 
output_columns = [
    "Player1_player_buttons_A",
    "Player1_player_buttons_B",
    "Player1_player_buttons_L",
    "Player1_player_buttons_R",
    "Player1_player_buttons_Y",
    "Player1_player_buttons_X",
    "Player1_player_buttons_up",
    "Player1_player_buttons_down",
    "Player1_player_buttons_left",
    "Player1_player_buttons_right",
    "Player1_player_buttons_select",
    "Player1_player_buttons_start"
]

# Split data into features 
X = df.drop(output_columns, axis=1)
y = df[output_columns]

print("feature shape:", X.shape)
print("target shape:", y.shape)

normalizer = StandardScaler()
x = normalizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("training samples:", X_train.shape[0])
print("testing samples:", X_test.shape[0])

# Build the MLP model 
model = Sequential()

# Input layer + Hidden layers
model.add(Dense(units=128, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=16, activation='relu'))

model.add(Dense(units=12, activation='sigmoid'))

# Compile with proper loss function 
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])

# add early stopping to prevent overfitting
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# Train the model with smaller batch size 
history = model.fit(X_train, y_train, epochs=30, batch_size=64,validation_split=0.2,callbacks=[early_stopping])

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

plt.figure(figsize=(12, 5))

# Plot accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy')
plt.legend()

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Model Loss')
plt.legend()

plt.tight_layout()
plt.show()

# make predictions
y_pred = model.predict(X_test)

threshold = 0.5
y_pred_binary = (y_pred > threshold).astype(int)
model.save("game_model.h5")

# show examples of predictions vs actual values
def display_sample_predictions(X_sample, y_true, y_pred, n=5):
    button_names = [col.replace('Player1_player_buttons_', '') for col in output_columns[1:]]
    
    for i in range(min(n, len(y_true))):
        print(f"\n--- Prediction {i+1} ---")
        
        print("Button     Actual  Predicted")
        print("-" * 40)
        
        for j in range(len(button_names)):
            button = button_names[j]
            actual = y_true.iloc[i, j + 1]
            pred = y_pred_binary[i, j + 1]

            print(button.ljust(10), "\t", int(actual), "\t", int(pred))


display_sample_predictions(X_test, y_test, y_pred_binary)
