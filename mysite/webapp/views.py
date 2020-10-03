from django.shortcuts import render
from django.http import JsonResponse
from time import sleep
import urllib.request, json
def index(request):
	url = "https://steamcommunity.com/market/search/render?q=&category_730_ItemSet[]=any&category_730_ProPlayer[]=any&category_730_StickerCapsule[]=any&category_730_TournamentTeam[]=any&category_730_Weapon[]=tag_weapon_tec9&appid=730&norender=1&count=500"
	#url = "https://steamcommunity.com/market/search/render/?query=&start=0&count=1000&norender=1&appid=730&currency=3"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	print(data['results'][0]['name'])
	context = {'items':data['results']}
	return render(request, 'index.html', context)

def getPrice(request):
	#send notification if is under xxx
	url = "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Shattered%20Web%20Case"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	print(data)

	context = {'price':data}
	return JsonResponse(context)

def toDelete(request):
	return render(request, 'todelete.html')
