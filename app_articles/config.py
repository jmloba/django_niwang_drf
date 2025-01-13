from app_product import urls
from django.conf import settings
localhost = settings.ALLOWED_HOSTS

BASE_HTTP = 'http://'
BASE_URL =  str(localhost[0]) +'/'
BASE_APP = 'app_articles/'

def get_base_http():
  return BASE_HTTP + BASE_URL
  

