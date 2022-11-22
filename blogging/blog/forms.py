from django import forms
from .models import Member,Category

choices=Category.objects.all().values_list('name','name')

choice_list=[]
for item in choices:
    choice_list.append(item)


class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=['title', 'author','category','blog_image','body','snippet']


        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'authorId','type':'hidden'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}), 
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['title','category','blog_image','body','snippet']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

            }
