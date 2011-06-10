"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from showpdf import views
from showpdf.models import Pdf, PdfManager, Html

url="http://martinfowler.com/apsupp/spec.pdf"

class PdfBehaviours(TestCase):
    def test_can_initialize_pdf_from_url(self):
        pdf=Pdf.fromUrl(url)
        self.assertIsNotNone(pdf, "Can't initialize pdf from url")
    
    def test_can_get_existing_pdf_from_url(self):
        pdf=Pdf.fromUrl(url)
        pdf.save()
        pdf2=Pdf.fromUrl(url)
        
        self.assertEquals(pdf,pdf2, "Can't get existing pdf from url")
        self.assertEquals(pdf.getPath(), pdf2.getPath(), "Can't get existing pdf from url")
    
    def test_can_get_pdf_path(self):
        pdf=Pdf.fromUrl(url)    
        self.assertIsNotNone(pdf.getPath(), "Can't get pdf path")
    
    def test_cant_initialize_pdf_from_url_that_is_not_pdf(self):
        pass
    
    def test_can_advise_if_file_doesnt_exists(self):
        pass
    
class HtmlBehaviours(TestCase):
    def test_can_write(self):
        html=Html(url)
        
        html.write("juas")
        
        self.assertEquals("juas",html.toString())
        
class PdfManagerBehaviours(TestCase):
    pdf=Pdf.fromUrl(url)
    
    def test_can_initialize_pdf_manager_with_pdf(self):  
        pdfManager=PdfManager(self.pdf)
        self.assertIsNotNone(pdfManager, "Can't initialize pdf manager")
    
    def test_can_get_pdf_as_html(self):
        pdfManager=PdfManager(self.pdf)
        html=Html(url)
        
        pdfManager.outToHtml(html)
        self.assertNotEqual("",html.toString(), "Can't get pdf as html")
        self.assertEquals(self.pdf, html.pdf)
        
    
        