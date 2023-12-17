from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PredictionData
from .serializers import PredictionDataSerializer
import joblib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import re
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle

'''
Ceci concerne la vue du test1 prédiction des logements
'''
class PredictionHouseAPIView(APIView):
    serializer_class = PredictionDataSerializer

    def post(self, request, format=None):
        # Charger le modèle
        regression_model = joblib.load('../Jupyter_code/HousePrediction_modele.pkl')

        # Sérialiser les données du modèle
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Effectuer la prédiction
        RM = serializer.validated_data.get('RM')
        LSTAT = serializer.validated_data.get('LSTAT')
        PTRATIO = serializer.validated_data.get('PTRATIO')
        prediction = regression_model.predict([[RM, LSTAT, PTRATIO]])

        # Retourner uniquement les résultats des prédictions
        return Response({'prediction': prediction[0]}, status=status.HTTP_200_OK)
    

'''
Ceci concerne la vue du test2 annalyse des sentiments
'''
def preprocess_text(text):
    # Suppression des balises HTML
    text = re.sub(r'<.*?>', '', text)
    
    # Suppression des stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_text = [word for word in tokens if word.lower() not in stop_words]
    text = ' '.join(filtered_text)
    
    # Suppression de la ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Suppression des lettres isolées
    text = re.sub(r'\b\w\b', '', text)
    return text

model = keras.models.load_model('../api/review')
with open('../api/review/tokenizer.pkl', 'rb') as f:
    tokenizer= pickle.load(f)
class PredictionReviewAPIView(APIView):
    def post(self, request):
        new_review = request.data.get('new_review')
        print(new_review)
        
        # Prétraitement de la revue 
        new_review=preprocess_text(new_review)
        # Encodage de la revue
        encoded_review = tokenizer.texts_to_sequences([new_review])

        # Ajustement de la longueur de la séquence
        encoded_review = pad_sequences(encoded_review, maxlen=100)
        # Passage de la revue au modèle
        prediction = model.predict(encoded_review)
        print(prediction)

        # Formatage de la réponse
        response = {
            'prediction': prediction.tolist()
        }
        
        return Response(response)
