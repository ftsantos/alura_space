from django import forms 

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite seu login'
            }
        )
    )
        
    password = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):    
    
    nome_cadastro = forms.CharField(
        label = 'Nome completo',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Ex.: João Silva'
            }
        )
    )
    email = forms.CharField(
        label = 'E-mail',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    password = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite sua senha'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Confirmação de senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite sua senha mais uma vez'
            }
        )
    )
    # clean_nomeDoCampoASerValidado em que ser assim
    def clean_nome_cadastro(self):
        
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possível inserir espaços dentro do campo Nome de Cadastro')
            else:
                return nome
            
    def clean_password2(self):
        
        senha1 = self.cleaned_data.get('password')
        senha2 = self.cleaned_data.get('password2')
        
        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('Por favor, digite senhas iguais.')
            else:
                return senha2
        
        
    
    
