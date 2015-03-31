from django.http import HttpResponse
from django.template import RequestContext, loader
import json

def graph(request):
    template = loader.get_template('graph.html')
    
    result = json.dumps([
      { "x_axis": 30, "y_axis": 30, "radius": 20, "color" : "green" },
      { "x_axis": 70, "y_axis": 70, "radius": 20, "color" : "purple"},
      { "x_axis": 110, "y_axis": 100, "radius": 20, "color" : "red"}])

    context = RequestContext(request, {
        'result': result,
    })

    return HttpResponse(template.render(context))
