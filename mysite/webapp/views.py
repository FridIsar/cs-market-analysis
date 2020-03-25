from django.shortcuts import render
from django.http import JsonResponse
from time import sleep
import urllib.request, json
def index(request):

	url = "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Shattered%20Web%20Case"

	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	print(data)

	context = {}
	return render(request, 'index.html', context)

def getPrice(request):
	#send notification if is under xxx
	url = "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Shattered%20Web%20Case"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	print(data)

	context = {'price':data}
	return JsonResponse(context)
