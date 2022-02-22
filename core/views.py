from django.http import HttpResponse

def home(request):
   text = """<h1>GitHub_Actions</h1>"""
   return HttpResponse(text)
