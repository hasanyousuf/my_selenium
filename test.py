# Requirements
##	Sumit checkout request
## Valid for each field
## All combinations must function
## Hearing any other requirement

#####
# Looking in HTML of code, it is using HTML5 required feature
# As this does not change in DOM, it should be handled in custom 
# error handling class 
# How to Solve (Approach)
###### Open browser
###### Without filling any field press submit button, it should not display confirmation page 
###### Check field is displayed
###### Check field is enabled
###### Check if there is "required" attribute for the field
###### Fill the field
###### Repeat these step until the last field where required attribute is present
#####  Finally submit the page and verify from the confiramtion message 


Enter the valid data in first field

class TestMust:
	pass