from urllib import request
from django import forms
from .models import Post

class post_form(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = [
            'title',
            'slug',
            'description',
            'Book_author',
            'uploaded_by',
            'file',
            'thumbnail',
        ]
        #*9-exclude = ['slug']
        #exclude = ["uploaded_by"]
        

       

        #def __init__(self):
        #   obj = post_form.fields.save(self, commit = False)
        #   obj.uploaded_by = self.request.user.username
        #   obj.save
    