from djando import forms
from mainCensus import models as mc_models
class GeneralForm(forms.ModelForm):

	class Meta:
		model = mc_models.General
		fields = ['']