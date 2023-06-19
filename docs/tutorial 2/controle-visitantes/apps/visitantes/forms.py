from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento", "numero_casa", "placa_veiculo", "placa_veiculo_foto"
        ]
        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante é obrigatório para o registro"
            },
            "cpf": {
                "required": "O cpf do visitante é obrigatório para o registro"
            },
            "data_nascimento": {
                "required": "A data de nascimento do visitante é obrigatória para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "O número da casa a visitar é obrigatória para o registro"
            }
        }

class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(
        required=True
    )
    
    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]
        error_messages = {
            "morador_responsavel": {
                "required": "Por favor, informe o nome do morador responsável por autorizar a entrada do visitante."
            }
        }