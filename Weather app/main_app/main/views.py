from django.shortcuts import render
import urllib.request,json
# Create your views here.
def index(request): 
    if request.method == 'POST': 
        
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
        # source contain JSON data from API 
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bd5e7f47e5a8bcfcc06f74d69b6f1d61').read() 
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        # data for variable list_of_data 
        data = { 
            "city": str(list_of_data['name']),  # Add city name
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon'])+' '+ str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp'])+'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={} 
    return render(request, "index.html", context= data) 