from pdfrw import PdfReader
import os, fnmatch

from django.shortcuts import render,redirect
from .models import*

# Create your views here.

def home(request):    
    keyword = None
    if request.method == 'POST':
            keyword = request.POST['keyword']       

            # def find_name(pattern, path):
            #     result = []
            #     files = []
            #     for root, dirs, files in os.walk(path):
            #         for name in files:
            #             try:
            #                 files.append((PdfReader(os.path.join(root, name)).Info['/barcode']))
            #                 if(keyword in PdfReader(os.path.join(root, name)).Info['/barcode']):
            #                     if fnmatch.fnmatch(name, pattern):
            #                         result.append(os.path.join(root, name))
            #             except:
            #                 pass
                        
            #     return files


            def find_path(pattern, path):
                result = []
                file_name = []
                for root, dirs, files in os.walk(path):
                    for name in files:
                        try:
                            files = (PdfReader(os.path.join(root, name)).Info['/barcode'])
                            if(keyword in PdfReader(os.path.join(root, name)).Info['/barcode']):
                                if fnmatch.fnmatch(name, pattern):
                                    result.append(os.path.join(root, name))
                                    
                                    file_name.append((os.path.basename(os.path.join(root, name))))                       
                        except:
                             pass
                context = {'result':result,'file_name':file_name}                
                return context

            data = find_path("*.pdf","E:\DJANGOPROJECTS\DocFinder\DocFinder")
            file_no = list(range(1,1000))
            files_name = data['file_name']
            file_path = data['result']
            file_and_path = zip(file_no,files_name,file_path)
            return render(request,'home.html',{"file_and_path":file_and_path,'keyword':keyword})
            
    else:   
        return render(request,'home.html',{'keyword':keyword})
