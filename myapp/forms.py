from django import forms
from .models import FriendsCrush 
class FormName(forms.ModelForm):
	class Meta:
		model=FriendsCrush
		fields="__all__"
	
	