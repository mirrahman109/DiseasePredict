# Disease Prediction & Medicine Recommendation System

A comprehensive Django-based web application that uses machine learning to predict diseases based on symptoms and provides personalized medicine recommendations, precautions, diet plans, and workout suggestions.

## 🚀 Features

- **Disease Prediction**: Advanced ML model using Support Vector Classification (SVC) to predict diseases based on symptoms
- **Medicine Recommendations**: Personalized medication suggestions for predicted diseases
- **Symptom Analysis**: Detailed breakdown of how each symptom contributes to the diagnosis
- **User-Friendly Interface**: Clean, responsive web interface for easy interaction
- **Multiple Predictions**: Shows top 3 most likely diseases with confidence scores

## 🛠️ Technologies Used

- **Backend**: Django 5.1.3, Python 3.11
- **Machine Learning**: 
  - Scikit-learn (SVC, Random Forest, Gradient Boosting)
  - Pandas, NumPy for data processing
  - Joblib for model persistence
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (development)


## 📊 Machine Learning Models

The system implements and compares multiple ML algorithms:
- **Support Vector Classification (SVC)** - Primary model
- **Random Forest Classifier**
- **Gradient Boosting Classifier**
- **K-Nearest Neighbors**
- **Multinomial Naive Bayes**

### Model Performance
- **Training Accuracy**: 100%
- **Testing Accuracy**: 99.19%
- **Disease Classes**: 41 different diseases
- **Symptoms**: 132 different symptoms

## 📁 Project Structure

```
medicine_recommendation_system/
├── medirec/                    # Main Django project
│   ├── medirec/               # Project settings
│   │   ├── settings.py        # Django configuration
│   │   ├── urls.py           # URL routing
│   │   └── wsgi.py           # WSGI application
│   ├── recommender/           # Main application
│   │   ├── models.py         # Database models
│   │   ├── views.py          # Business logic
│   │   ├── urls.py           # App routing
│   │   └── templates/        # HTML templates
│   ├── staticfiles/          # Static files (CSS, JS, images)
│   ├── manage.py             # Django management script
│   └── requirements.txt      # Python dependencies
├── Dataset/                   # Training data and CSV files
├── medicine_model.ipynb      # ML model development notebook
└── README.md                 # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mirrahman109/DiseasePredict.git
   cd DiseasePredict
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to Django project**
   ```bash
   cd medirec
   ```

5. **Configure settings (optional)**
   ```bash
   # Set environment variables or update settings.py
   # DEBUG=True for development
   # ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000`

## 🚀 Deployment

### Heroku Deployment
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```


### Environment Variables
For production deployment, set these environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False`
- `ALLOWED_HOSTS`: Your domain names

## 📈 Usage

1. **Home Page**: Navigate to the main page
2. **Select Symptoms**: Choose from 132 available symptoms
3. **Get Prediction**: Submit symptoms to receive disease predictions
4. **View Results**: See top 3 predictions with:
   - Disease name and confidence score
   - Symptom contribution analysis
   - Medicine recommendations
<img width="796" height="832" alt="Screenshot 2025-07-31 190925" src="https://github.com/user-attachments/assets/10021e61-8079-42c5-983f-c049cad75858" />
<img width="742" height="796" alt="Screenshot 2025-07-31 190944" src="https://github.com/user-attachments/assets/b3275e18-3e73-428b-8a0e-2017bb852574" />
<img width="1063" height="913" alt="Screenshot 2025-07-31 191038" src="https://github.com/user-attachments/assets/0694a448-0022-4a8b-91d8-4f6383914b03" />
<img width="1069" height="649" alt="Screenshot 2025-07-31 191045" src="https://github.com/user-attachments/assets/0bcde71d-38e6-40f1-8ba5-0c1b812c9f43" />

   

## 🤖 Machine Learning Pipeline

1. **Data Preprocessing**: 
   - Label encoding for diseases
   - Feature scaling for specific models
   - Noise addition for data augmentation

2. **Model Training**:
   - Multiple algorithm comparison
   - Cross-validation and testing
   - Best model selection based on accuracy

3. **Prediction Engine**:
   - Symptom-to-vector conversion
   - Probability calculation
   - Contribution analysis for interpretability

## 📊 Dataset Information

- **Training Data**: Medical symptom-disease mappings
- **Symptoms Database**: 132 unique symptoms
- **Disease Database**: 41 different diseases
- **Additional Data**: Medicines, precautions, diets, workouts

## 🔒 Security Features

- CSRF protection enabled
- Secure static file serving with WhiteNoise
- Debug mode disabled in production
- Environment-based configuration

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mir Rahman**
- GitHub: [@mirrahman109](https://github.com/mirrahman109)
- Project: [DiseasePredict](https://github.com/mirrahman109/DiseasePredict)

## ⚠️ Disclaimer

This system is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact the development team.

---

**Made with ❤️ for better healthcare accessibility**
