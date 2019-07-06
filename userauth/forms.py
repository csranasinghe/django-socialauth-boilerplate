from django import forms


class UserAccountSignUpForm(forms.Form):
    '''
    Since we use django-allauth we don't need to add username, email or passowrd fields here.
    These fields added automatically.
    '''
    name = forms.CharField(max_length=30, label='Name', required=True, widget=forms.TextInput(attrs=
                                                                                              {'placeholder': 'Name'}))

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.save()
