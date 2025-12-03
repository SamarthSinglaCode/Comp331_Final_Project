import pandas as pd

# Load the dataset
file_name = "target_ten_whole_food_nutrition_info.csv"
data = pd.read_csv(file_name)

# Display the first few rows of the dataset to verify loading
print("Dataset preview:")
print(data.head())

# Separate the first 5 rows for training and the last 5 rows for testing
train_data = data.iloc[:5]
test_data = data.iloc[5:]

# Extract features and labels (if applicable, create a label column based on health criteria)
# Here we define 'health_criteria' for simplicity. Update based on your specific rules.
def classify_food(row):
    # Example health criteria: high protein (>20), low fat (<10), and low carbohydrate (<10)
    if row['protein'] > 20 and row['fat'] < 10 and row['carbohydrate'] < 10:
        return "Healthy"
    else:
        return "Unhealthy"

# Apply classification to the training data (optional step to create labels)
train_data['health_label'] = train_data.apply(classify_food, axis=1)

# Show processed training and test data
print("\nTraining Data:")
print(train_data)
print("\nTest Data:")
print(test_data)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Features (independent variables) and labels (dependent variable) from the training data
X_train = train_data[['protein', 'fat', 'carbohydrate']]  # Nutritional features
y_train = train_data['health_label']  # Health labels ("Healthy" or "Unhealthy")

# Features from the test data
X_test = test_data[['protein', 'fat', 'carbohydrate']]

# Encode labels into numerical values (Logistic Regression requires numeric labels)
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)  # Encode "Healthy" -> 1, "Unhealthy" -> 0

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train_encoded)

# Predict the health labels for test data
predictions_encoded = model.predict(X_test)
predictions = label_encoder.inverse_transform(predictions_encoded)  # Decode predictions to original labels

# Display predictions for test data
test_data['predicted_health_label'] = predictions
print("\nTest Data with Predictions:")
print(test_data)

# If you have true labels for the test set, calculate the accuracy (optional)
# Uncomment the next two lines if true labels are available in `test_data`
# y_test = label_encoder.transform(test_data['health_label'])  # Encode true labels
# print("\nAccuracy:", accuracy_score(y_test, predictions_encoded))

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data (replace this with your actual dataset or model)
data = {
    'food_name': ['egg', 'chicken_wings', 'beef', 'carrots', 'strawberries', 'blueberries', 'honey', 'banana', 'apple', 'mushrooms'],
    'protein': [48.1, 23.9, 27.3, 0.81, 0.64, 0.74, 0.3, 0.74, 0.1875, 2.890625],
    'fat': [39.8, 5.95, 11.4, 0.47, 0.22, 0.33, 0.0, 0.29, 0.2125, 0.3708],
    'carbohydrate': [1.87, 0.0, 0.0, 7.92, 7.63, 14.49, 82.4, 23.0, 14.7817, 4.079375],
    'health_status': ['healthy', 'unhealthy', 'unhealthy', 'healthy', 'healthy', 'healthy', 'unhealthy', 'healthy', 'healthy', 'healthy']
}

df = pd.DataFrame(data)

# Preprocessing
X = df[['protein', 'fat', 'carbohydrate']]
y = df['health_status']
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train a simple model (Logistic Regression)
model = LogisticRegression()
model.fit(X, y_encoded)

@app.route('/predict', methods=['POST'])
def predict():
    food_data = request.get_json()
    food_name = food_data['food_name']
    
    # Find the food item in the dataset
    food_item = df[df['food_name'].str.lower() == food_name.lower()]
    
    if not food_item.empty:
        # Get nutritional values
        protein = food_item['protein'].values[0]
        fat = food_item['fat'].values[0]
        carbohydrate = food_item['carbohydrate'].values[0]
        
        # Predict health status
        input_data = pd.DataFrame([[protein, fat, carbohydrate]], columns=['protein', 'fat', 'carbohydrate'])
        prediction = model.predict(input_data)
        health_status = label_encoder.inverse_transform(prediction)[0]
        
        return jsonify({
            "food_status": health_status,
            "protein": protein,
            "fat": fat,
            "carbohydrates": carbohydrate
        })
    else:
        return jsonify({"error": "Food item not found!"})

if __name__ == '__main__':
    app.run(debug=True)



