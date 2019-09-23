from django.shortcuts import render
from django.http import HttpResponse
from . import data as d


search_tag="shubham"

def request_page(request):
	if(request.GET.get('search')):
		search_tag=request.GET.get('search_box')
	return render(request,'products/search.html')

def home(request):
	var={
		'search':search_tag
	}
	return render(request,'products/search.html',var)

def product_page(request):
	context={
		'title': d.title,
		'image' :d.image,
		'review':d.review,
		'rating':d.rating,

	}
	return render(request,'products/Product_page.html',context)



