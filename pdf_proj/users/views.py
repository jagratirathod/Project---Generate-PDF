import html
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from . models import User
from django.views.generic import ListView
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

def hello(request):
    return HttpResponse("Hello world !")

class UserListView(ListView):
    model = User
    template_name = 'main.html'


def users_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user = get_object_or_404(User, pk=pk)
    template_path = 'generate_pdf.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # to directly download the pdf we need attachment 
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to view on browser we can remove attachment 
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response





