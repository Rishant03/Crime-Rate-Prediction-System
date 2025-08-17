import pickle

# Step 1: Try loading the model
try:
    with open("Model/model.pkl", "rb") as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    exit()

# Step 2: Check if model has 'predict' method
if hasattr(model, 'predict'):
    print("✅ Model has a 'predict' method.")
else:
    print("❌ Model does not have a 'predict' method.")
    exit()

# Step 3: Try a sample prediction
try:
    sample_input = [[2023, 4, 165.73, 9]]  # [year, city_code, population, crime_code]
    result = model.predict(sample_input)
    print(f"✅ Prediction successful. Result: {result}")
except Exception as e:
    print(f"❌ Model prediction failed: {e}")
