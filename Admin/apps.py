from django.apps import AppConfig

class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Admin'  # ✅ Must match folder name exactly (case-sensitive)
