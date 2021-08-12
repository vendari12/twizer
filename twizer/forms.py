import os
from django import forms



class DataForm(forms.Form):  
    filename = forms.CharField(label="Enter file name", max_length=50)
    file = forms.FileField()

    #file extension validation
    #def clean(self):
     #   data = self.cleaned_data.get('file')
        #super(DataForm, self).clean()
        #if data:
            #filename = data
            #ext = os.path.splitext(data)[1]
            #ext = ext.lower()
            #if ext != '.csv':
             #   raise forms.ValidationError("Filetype not allowed!")
        #return self.cleaned_data
