A Smart Food Diary is a digital application that helps users log their meals, track nutritional intake, and receive personalized dietary insights. Your version, as mentioned earlier, involves advanced features like image recognition, nutrient analysis, and dietary recommendations.

🎯 Objective:
To help users maintain a healthy diet by tracking their daily food intake, analyzing nutrition, and providing AI-driven recommendations.

Key Features:
User Authentication
Profile management with age, gender, weight, and dietary preferences
Meal Logging
Manual entry of meals
Option to upload a food image
Image Recognition
Uses ViT (Vision Transformer) to detect food items from images
Nutrient Analysis
Progress Tracking by Daily/weekly reports on calorie intake, nutritional balance
Visualizations of nutrients(graphs, pie charts)
Admin Dashboard to manage users, view usage statistics

# **Setup**
```bash
git clone https://github.com/11anagha/smart_food_diary.git
cd SmartFood_CalorieCode

python -m venv env
source env/bin/activate  # On Windows use `source env/Scripts/activate`

pip install -r requirements.txt

create an .env file and store your env keys their

eg:
EMAIL_ADDRESS=YOUR_EMAIL_ADDRESS
EMAIL_PASS=GOOGLE_APP_PASS
API_APP_KEY=YOUR_API_APP_KEY
API_APP_ID=YOUR_APP_ID
pdf_path=YOUR_PDF_PATH (To setup please refer: https://youtu.be/PFUsPlyMB00?si=QwHGRsmWYcpcRQ1m)
```
