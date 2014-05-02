from django.http import HttpResponse
from django.http import HttpRequest
from django import forms
import graphs
import interactions
intrs  = interactions.getInteractions()
genes = sorted(intrs.keys())

def index(request):
    response = HttpResponse()
    f = open('static/index.html')
    lines = f.readlines()
    for line in lines:
        response.write(line)
    return response

def ribosomalmapping(request):
    graphs.generate_graph()
    response = HttpResponse()
    response.write("<html><head><title='hello'></title></head>")

    response.write( "<body><a href='index'>Main Menu</a><img src='/static/rp_positions.svg' width='100%' height='90%'/></body></html>")
    return response


class intrForm(forms.Form):
    gene = forms.ChoiceField(choices = [(a,a) for a in genes])

def selectinteractions(request):
    f = intrForm()
    response = HttpResponse()
    head = "<head><title>Interactions</title></head>"
    body = "<body><a href='index'>Main Menu</a><div style='text-align: center'><form action='getinteraction' method='get'>"+f.as_table()
    body+= "<input type='submit' value='submit'> </form></div></body>"
    
    return HttpResponse("<html>"+head+body+"</html>")
    

def getinteractions(request):
    response = HttpResponse()
    interactions.get_interaction(intrs,request.GET['gene'])
    response.write("<html><head><title='hello'></title></head>")

    response.write("<body><ul><li><a href='selectinteractions' >Change Gene</a> <li> <a href='index'>Main Menu</a></ul><img src='/static/rp_interactions.svg' width='100%' height='90%'/></body></html>")
    return response
