from django.http import HttpResponse, HttpResponseRedirect
from showpdf.models import Pdf, PdfManager, Html
from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    return render_to_response('showpdf/index.html', {})

def load_pdf(request):
    pdf=Pdf.fromUrl(request.GET["url_pdf"])
    pdf.save()
    return HttpResponseRedirect("/show/"+pdf.id)

def show_pdf(request, id_pdf):
    pdfSaved=Pdf.objects.get(id=id_pdf)
    html=None
    
    try:
        html=Html.objects.get(pdf=pdfSaved)
    except Html.DoesNotExist:
        html=Html()
        pdfManager=PdfManager(pdfSaved);
        pdfManager.outToHtml(html)
        html.save()
    
    return HttpResponse(html.toString())
    
