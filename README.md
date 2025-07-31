# Disease Prediction & Medicine Recommendation System

A comprehensive Django-based web application that uses machine learning to predict diseases based on symptoms and provides personalized medicine recommendations, precautions, diet plans, and workout suggestions.

## 🚀 Features

- **Disease Prediction**: Advanced ML model using Support Vector Classification (SVC) to predict diseases based on symptoms
- **Medicine Recommendations**: Personalized medication suggestions for predicted diseases
- **Health Guidance**: Comprehensive precautions, diet plans, and workout routines
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
- **Database**: SQLite (development), PostgreSQL ready
- **Deployment**: Configured for Heroku, Railway, Render

## 📊 Machine Learning Models

The system implements and compares multiple ML algorithms:
- **Support Vector Classification (SVC)** - Primary model
- **Random Forest Classifier**
- **Gradient Boosting Classifier**
- **K-Nearest Neighbors**
- **Multinomial Naive Bayes**

### Model Performance
- **Training Accuracy**: 100%
- **Testing Accuracy**: 100%
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
   cd medirec
   pip install -r requirements.txt
   ```

4. **Configure settings**
   ```bash
   # Update ALLOWED_HOSTS in settings.py
   ALLOWED_HOSTS = ['localhost', '127.0.0.1']
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000`

## 🚀 Deployment

### Heroku Deployment
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

### Railway Deployment
```bash
# Install Railway CLI
npm install -g @railway/cli
railway login
railway new
railway deploy
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
   - Precautions and diet suggestions
   - Workout recommendations

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
