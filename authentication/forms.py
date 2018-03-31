from allauth.account.forms import LoginForm, SignupForm

#Tried to override the form, didn't work
class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['remember'].label = 'Stay signed in'
        self.fields['remember'].initial = True