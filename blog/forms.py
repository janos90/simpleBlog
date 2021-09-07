from django.forms import ModelForm, TextInput, Select, Textarea

from blog.models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'category')

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'title_tag': TextInput(attrs={'class': 'form-control'}),
            'author': Select(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }