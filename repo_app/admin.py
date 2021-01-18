from django.contrib import admin
from repo_app.models import MyUser, Image

models = [MyUser, Image]
admin.site.register(models)