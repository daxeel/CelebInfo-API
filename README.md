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
<h3>Search By Birthday</h3>
API Request syntax : <br>
https://birthdays-daxeel.rhcloud.com/api/date/{DATE}/{MONTH_IN_WORDS}
<br>where,<br>
DATE and MONTH_IN_WORDS is a day and API will give you the data of all celebrities having birthday on this specified date and month.<br>
For example : <br><a href="https://birthdays-daxeel.rhcloud.com/api/date/28/september">https://birthdays-daxeel.rhcloud.com/api/date/28/september</a>
<br><br>
<h3>Custom Search</h3>
API Request syntax : <br>
http://birthdays-daxeel.rhcloud.com/api/custom/{SEARCH_TYPE}
<br>where,<br>
SEARCH_TYPE can be <br><br>
