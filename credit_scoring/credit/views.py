from django.shortcuts import render
from . import ai
import numpy as np
from keras import backend
from .forms import CreditForm

def index(request):
    out =""

    if request.method == 'POST':
        cf = CreditForm(request.POST)
        train = ai.loadModelAndWeight()
        if(cf.is_valid()):
            result = train.predict(np.array([[cf.cleaned_data['ru'],cf.cleaned_data['age'],
                                              cf.cleaned_data['times30'],cf.cleaned_data['dr'],
                                              cf.cleaned_data['mi'],cf.cleaned_data['loans'],
                                              cf.cleaned_data['late'],cf.cleaned_data['lines'],
                                              cf.cleaned_data['times60'],cf.cleaned_data['nd']
                                              ]]))
            out = result[0][0]
            if(out>0.5):
                    out = "The person is SeriousDlqin2yrs"
            else:
                    out = "The person is not SeriousDlqin2yrs"

            backend.tensorflow_backend.clear_session()
        else:
            out="Please specify the correct values"

        return render(request,'test.html', {'result': out, 'form': cf})
    else:
        cf=CreditForm()
        return render(request,'test.html', {'result':out,'form':cf})