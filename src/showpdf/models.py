from django.db import models
from pdfminer.converter import HTMLConverter
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.layout import LAParams
import hashlib
import urllib
import sys

# Create your models here.
class Pdf(models.Model):
        id=models.CharField(max_length=32,primary_key=True)
        __url=models.URLField()
        
        @staticmethod
        def fromUrl(url):
            try:
                pdf=Pdf.objects.get(id=Pdf.__getId(url))
            except Pdf.DoesNotExist:
                pdf=Pdf()
                pdf.id=None
                pdf.__url=url
                
            return pdf
        
        def getPath(self):
            return urllib.urlretrieve(self.__url)[0]
        
        def __eq__(self, pdf):
            return self.id==pdf.id
        
        def save(self):
            if self.id==None:
                self.id=self.__getId(self.__url)
            super(Pdf,self).save()
        
        @staticmethod
        def __getId(url):
            return hashlib.md5(url).hexdigest()
        
class Html(models.Model):
    pdf=models.ForeignKey("Pdf")
    __content=models.TextField()
        
    def write(self, text):
        self.__content+=text
        
    def toString(self):
        return self.__content

class   PdfManager():
    __pdf=None
    __caching=True
    __codec = 'utf-8'
    __scale=1
    __layoutmode = 'normal'
    __laparams = LAParams()
    __outdir = None
    __pagenos=set()
    __maxpages=0
    __password=''
    
    def __init__(self,pdf):
        self.__pdf=pdf
        
    def outToHtml(self, html):
        pdfFile=file(self.__pdf.getPath(), 'rb')
        rsrcmgr = PDFResourceManager(caching=self.__caching)
        device = HTMLConverter(rsrcmgr, html, codec=self.__codec, 
                               scale=self.__scale,layoutmode=self.__layoutmode, 
                               laparams=self.__laparams, outdir=self.__outdir)
        
        process_pdf(rsrcmgr, device, pdfFile, self.__pagenos, maxpages=self.__maxpages, password=self.__password,
                    caching=self.__caching, check_extractable=True)
        pdfFile.close()
        html.pdf=self.__pdf
        
        return html