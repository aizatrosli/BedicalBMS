from django.contrib import admin
from django.apps import apps


models = apps.get_models()

for model in models:
    if "Bedical" in model.__name__:
        admin.site.register(model)
