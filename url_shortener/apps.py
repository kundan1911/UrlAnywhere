from django.apps import AppConfig

#this must be added to the setting INstalled_APp list to make the django understand this is a new app
class UrlShortenerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'url_shortener'
