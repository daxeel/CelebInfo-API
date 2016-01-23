<a href="https://market.mashape.com/daxeel/celebinfo"><img src="http://i1.wp.com/blog.mashape.com/wp-content/uploads/2013/02/Screen_Shot_2013-02-12_at_6.53.42_PM.png"</a>

# CelebInfo-API
Unofficial API of famousbirthdays.com

# About
CelebInfo is a simple API which will give you access to the information like birthdays etc. With this API you will get these data of celebrities.
<ul>
	 <li>Name</li>
	 <li>Age</li>
	 <li>Birthday</li>
	 <li>Birth Year</li>
	 <li>Birth Place</li>
	 <li>Birth Sign</li>
	 <li>Occupation</li>
	 <li>Photo</li>
</ul>

# Documentation
API documentation here is for python language. To use this in python you need to install unirest module.
```sh
sudo pip install unirest
```
###Search By Birthday
API Request syntax : <br>
```py
response = unirest.get("https://daxeel-celebinfo-v1.p.mashape.com/date/{DATE}/{MONTH_IN_WORDS}",
  headers={
    "X-Mashape-Key": "V96M0xptxxxxxx",
    "Accept": "text/plain"
  }
)
```
where,<br>
DATE and MONTH_IN_WORDS is a day and API will give you the data of all celebrities having birthday on this specified date and month.<br>
For example,
```py
response = unirest.get("https://daxeel-celebinfo-v1.p.mashape.com/date/28/september",
  headers={
    "X-Mashape-Key": "V96M0xptxxxxxx",
    "Accept": "text/plain"
  }
)
```
Response will be like this,
```json
{
	"data": [{
		"age": "18",
		"birth_place": "Harij, Gujarat, India",
		"birth_sign": "Pisces",
		"birth_year": "1996",
		"birthday": "September 28",
		"name": "Daxeel Soni",
		"occupation": "Developer of this API. More: www.daxeelsoni.in",
		"photo_url": "http://daxeelsoni.in/images/me.jpg"
	}, {
		"age": 28,
		"birth_place": "Houston",
		"birth_sign": "Libra",
		"birth_year": "1987",
		"birthday": "September 28",
		"name": "Hilary Duff",
		"occupation": "TV Actress",
		"photo_url": "http://www.famousbirthdays.com/thumbnails/duff-hilary-medium.jpg"
	}, {
		"age": 38,
		"birth_place": "Columbia",
		"birth_sign": "Libra",
		"birth_year": "1977",
		"birthday": "September 28",
		"name": "Young Jeezy",
		"occupation": "Rapper",
		"photo_url": "http://www.famousbirthdays.com/thumbnails/jeezy-young-medium.jpg"
	}, {
		"age": 48,
		"birth_place": "Roanoke",
		"birth_sign": "Libra",
		"birth_year": "1967",
		"birthday": "September 28",
		"name": "Challen Cates",
		"occupation": "TV Actress",
		"photo_url": "http://www.famousbirthdays.com/thumbnails/cates-challen-medium.jpg"
	}]
}
```
<br><br>


<h3>Custom Search</h3>
API Request syntax : <br>
```py
response = unirest.get("https://daxeel-celebinfo-v1.p.mashape.com/custom/{SEARCH_TYPE}",
  headers={
    "X-Mashape-Key": "V96M0xptxxxxxx"
  }
)
```
<br>where,<br>
SEARCH_TYPE can be <br><br>
<table style="border:1px solid #FE7B09;padding:20px;">
	<tr>
		<td><b>yesterday</b></td>
		<td>Returns info of celebrities having birthdays yesterday</td>
	</tr>
	<tr>
		<td><b>today</b></td>
		<td>Returns info of celebrities having birthdays today</td>
	</tr>
	<tr>
		<td><b>tomorrow</b></td>
		<td>Returns info of celebrities having birthdays to tomorrow</td>
	</tr>
	<tr>
		<td><b>tdat</b></td>
		<td>Returns info of celebrities having birthdays the after tomorrow</td>
	</tr>
</table>
<br>
For example,
```py
response = unirest.get("https://daxeel-celebinfo-v1.p.mashape.com/custom/today",
  headers={
    "X-Mashape-Key": "V96M0xptxxxxxx"
  }
)
```
Response will be like this,
```json
{
	"data": [{
		"age": 20,
		"birth_place": "Houston",
		"birth_sign": "Aquarius",
		"birth_year": "1996",
		"birthday": "January 23",
		"name": "Chachi Gonzales",
		"occupation": "Dancer",
		"photo_url": "http://www.famousbirthdays.com/thumbnails/gonzales-chachi-medium.jpg"
	}, {
		"age": 32,
		"birth_place": "Netherlands",
		"birth_sign": "Aquarius",
		"birth_year": "1984",
		"birthday": "January 23",
		"name": "Arjen Robben",
		"occupation": "Soccer Player",
		"photo_url": "http://www.famousbirthdays.com/thumbnails/robben-arjen-medium.jpg"
	}, {
		"age": 31,
		"birth_place": "Pennsylvania",
		"birth_sign": "Aquarius",
		"birth_year": "1985",
		"birthday": "January 23",
		"name": "Draya Michele",
		"occupation": "Reality Star",
		"photo_url": "http://www.famousbirthdays.com/thumbnails/michele-draya-medium.jpg"
	}, {
		"age": 24,
		"birth_place": "New Jersey",
		"birth_sign": "Aquarius",
		"birth_year": "1992",
		"birthday": "January 23",
		"name": "Louis Giordano",
		"occupation": "Vine Star",
		"photo_url": "http://www.famousbirthdays.com/thumbnails/giordano-louis-medium.jpg"
	}]
}
```
