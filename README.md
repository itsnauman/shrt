#Chota
Chota is an awesome url shortener written in `Flask`, it is simple yet powerful. Fork this repo and play around with it, don't forget to make pull requests. This app is running on Heroku, http://chota-tk.herokuapp.com/ :)

<a href="http://imgur.com/KEIT77n"><img src="http://i.imgur.com/KEIT77n.png" title="Hosted by imgur.com" /></a>

###Installation:
 - Clone this repo ```git clone https://github.com/itsnauman/chota.git```
 - Install the requirements, only Flask is required though ```pip install -r requirements.txt```

###Usage:
Edit `__init__.py` and provide your db path instead of `os.environ['DATABASE_URL']`, also add `db.create_all()` in the `runserver.py` file to create the db. That's all, Run the `runserver.py` file and boom, you are up and running :)

###Contributing:
 - Improve loading speed
 - Make the website pretty
 - Improve the api

###License:
Chota is distributed under MIT license, see license for more details
