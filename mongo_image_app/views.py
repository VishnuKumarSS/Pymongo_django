import pdb
from django.shortcuts import render
from .mongo_models import *
import base64

def image_upload_view(request):
    """Process images uploaded by users"""
    context = {}
    datas = {}
    if request.method == 'POST':
        img = request.FILES['img_name']
        img_title = request.POST['title_name']

        # read
        img_binary = fs.put(img.read(), filename=img_title)

        # insert in table
        datas['img_binary_id'] = img_binary
        datas['title'] = img_title

        obj = my_collection.insert_one(datas)

        img_source = fs.get(img_binary).read()
        uploaded = fs.get(img_binary).upload_date

        img_url = base64.b64encode(img_source).decode()
        pdb.set_trace()

        context['img']  = img_url
        context['uploaded'] = uploaded
        context['img_title'] = img_title
        return render(request, 'upload.html', context)
    else:
        return render(request, 'upload.html')

