from django.shortcuts import render
from .forms import DataForm
import json
from django.http.response import HttpResponse
from .utils.fileread import json_parse as parser


def IndexView(request):
    form = DataForm()
    if request.method == 'POST' and request.FILES['file']:	
        filename = 'userfile'
        file_obj = firstname= form.cleaned_data.get("file")
        file = parser(file_obj)
        filepath = filename + '.json'
        with open(filepath, "w",encoding='utf8') as write_file:
            json.dump(file, write_file)
            response = HttpResponse(json.dumps(file), content_type='application/json')
            response['Content-Disposition'] = "attachment; filename=%s" % filepath
                # Return the response value
            return response
    else:
        form = DataForm()
    return render(request, 'index.html', {'form': form})
