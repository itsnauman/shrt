#Chota
Chota is an awesome url shortener written in `Flask`, it is simple yet powerful. Fork this repo and play around with it, don't forget to make pull requests. See the app in [action](http://chota-tk.herokuapp.com/) :)

<a href="http://imgur.com/KEIT77n"><img src="http://i.imgur.com/KEIT77n.png" title="Hosted by imgur.com" /></a>

###Installation:
 - Clone this repo ```git clone https://github.com/itsnauman/chota.git```
 - Install the requirements, only Flask is required though ```pip install -r requirements.txt```

###Usage:
Edit `__init__.py` and provide your db path instead of `os.environ['DATABASE_URL']`, also add `db.create_all()` in the `runserver.py` file to create the db. That's all, Run the `runserver.py` file and boom, you are up and running :)

###Api:
The api is very basic at the moment but gets the job done, in order to shorten  url, send a GET request to chota-tk.herokuapp.com/api with long url.
Request: 
```
curl http://chota-tk.herokuapp.com/api/google.com
```
Response:
```
{
  "short_url": "http://chota-tk.herokuapp.com/czidce", 
  "success": true
}
```
###Contributing:
 - Improve loading speed
 - Unittests will be appreciated 

###License:
Chota is distributed under MIT license, see license for more details
