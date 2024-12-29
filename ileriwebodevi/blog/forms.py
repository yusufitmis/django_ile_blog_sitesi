from django import forms
from .models import PostModel, Comment


# Post oluşturma formu
class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = PostModel
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        # Alan etiketlerini Türkçeye çeviriyoruz
        self.fields['title'].label = 'Başlık'
        self.fields['content'].label = 'İçerik'


# Post güncelleme formu
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        # Alan etiketlerini Türkçeye çeviriyoruz
        self.fields['title'].label = 'Başlık'
        self.fields['content'].label = 'İçerik'


# Yorum yapma formu
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Yorumunuzu buraya ekleyin...'}))

    class Meta:
        model = Comment
        fields = ('content',)
