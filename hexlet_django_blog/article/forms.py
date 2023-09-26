from django.forms import ModelForm, ValidationError
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

    def is_valid(self):
        valid = super().is_valid()
        
        if valid:
            # Дополнительная логика валидации
            name = self.cleaned_data.get('name')
            body = self.cleaned_data.get('body')
            if len(name) < 3:
                self.add_error('name', 'Заголовок должен содержать не менее 3 символов.')
            if len(body) < 5:
                self.add_error('body', 'Текст должен содержать не менее 5 символов.')
            if self.errors:
                return False
                
        return valid

