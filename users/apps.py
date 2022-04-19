from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    
    def ready(self):
        from . import signals

# users/__init__.py 
default_app_config = 'users.apps.UsersConfig'