📌 Crime Rate Prediction System

 📖 Overview

Crime Rate Predictor is a **Machine Learning powered web application** that predicts the likelihood of crimes in **19 Indian metropolitan cities**.
It helps law enforcement agencies, researchers, and policymakers to understand **crime patterns** and take proactive measures for **resource allocation and public safety**.

The system is built using **Flask** (backend), **scikit-learn Random Forest Regression** (ML model), and **HTML/CSS/Jinja2** (frontend).

<img width="1889" height="904" alt="project_ss" src="https://github.com/user-attachments/assets/aab2c983-8d72-4e9f-b1e8-9943e7ab8f99" />


🚀 Features

 🔎 Predicts crime rates for **10 crime categories**
 🏙️ Covers **19 major Indian cities**
 📊 Uses **historical NCRB crime data (2014–2021)**
 🤖 **Random Forest Regression model** with **93.2% accuracy**
 🌍 User-friendly **Flask web interface**
 📈 Estimates both **crime rate** and **expected number of cases**
 📌 Classifies areas as:

   Very Low Crime
   Low Crime
   High Crime
   Very High Crime



🧩 Crime Categories

1. Crime Committed by Juveniles
2. Crime Against Scheduled Castes (SC)
3. Crime Against Scheduled Tribes (ST)
4. Crime Against Senior Citizens
5. Crime Against Children
6. Crime Against Women
7. Cyber Crimes
8. Economic Offences
9. Kidnapping
10. Murder



🏗️ Tech Stack

**Frontend:** HTML, CSS, Jinja2
**Backend:** Flask (Python)
**Machine Learning:** scikit-learn (Random Forest Regressor)
**Server:** Gunicorn (for deployment)
**Dataset:** NCRB (2014–2021 crime statistics for 19 cities)



⚙️ Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/Crime-Rate-Prediction.git
   cd Crime-Rate-Prediction
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   python app.py
   ```

4. **Open in Browser**

   ```
   http://127.0.0.1:5000/
   ```

---

🎯 Usage

1. Select a **City** from the dropdown.
2. Choose a **Crime Type** (e.g., Cyber Crimes, Murder).
3. Enter a **Year** (e.g., 2025).
4. Click on **Predict** → The app will show:

   * Predicted crime rate
   * Estimated number of cases
   * City & crime details
   * Crime severity classification



📊 Model Validation

Run the model validation script:

```bash
python validate_model.py
```

 ✅ Confirms the model loads correctly
 ✅ Ensures prediction works on sample data



📈 Future Improvements

* Expand dataset to cover **more cities and years**
* Add **visualizations & trend graphs**
* Integrate **real-time police/incident data**
* Deploy on **cloud (Heroku/AWS/GCP)**


👨‍💻 Author

Rishant Raj
📧 [rishantraj03@gmail.com](mailto:rishantraj03@gmail.com)
https://www.linkedin.com/in/rishant-raj-a7974224b



