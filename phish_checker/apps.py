from django.apps import AppConfig
from sklearn.externals import joblib

class PhishCheckerConfig(AppConfig):
    name = 'phish_checker'


def load_model():
	filename = 'trained_model.sav'
	loaded_model = joblib.load(filename)
