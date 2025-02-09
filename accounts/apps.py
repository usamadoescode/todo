from django.apps import AppConfig

class AccountsConfig(AppConfig):  # Change 'UsersConfig' to 'AccountsConfig'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'  # Keep this consistent with the folder name
