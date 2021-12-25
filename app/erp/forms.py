from django.forms import ModelForm

from app.erp.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'