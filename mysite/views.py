from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import Product
import random
from mysite.models import Product

# Create your views here.


def about(request):
    html = '''
<!DOCTYPE html>
<html>
<head><title>About Myself</title></head>
<body>
<h2>Chi-Chao Chang</h2>
<hr>
<p>
Hi, I am Chi-Chao Chang. Nice to meet you!
</p>
</body>
</html>
'''
    return HttpResponse(html)


def listing(request):
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>中古機列表</title>
</head>
<body>
<h2>以下是目前本店中的二手機列表</h2>
<hr>
<table width=400 border=1 bgcolor='#ccffcc'>
{}
</table>
</body>
</html>
'''
    products = Product.objects.all()
    tags = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.qty)

    return HttpResponse(html.format(tags))
