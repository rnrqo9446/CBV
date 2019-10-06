from django import forms
from .models import Post, Product

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'text', 'price')