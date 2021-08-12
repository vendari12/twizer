from django.shortcuts import render
from .forms import DataForm
import json
from django.http.response import HttpResponse
from .utils.fileread import json_parse as parser


def IndexView(request):
    form = DataForm()
    if request.method == 'POST' and request.FILES['file']:
        objects = DataForm(request.POST, request.FILES)
        if objects.is_valid():
            filename = objects.data.get('filename')
            file_obj = objects.files.get('file')
            print(file_obj)
            try:
                file = parser(file_obj)
            except Exception as e:
                raise e
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
