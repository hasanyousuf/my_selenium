**Table of Contents**

# Tools
- Python
- pytest
- Selenium 
- Webdriver Manager

# Prons
- Test framework built using python and virtual environments can be run on different operating systems.e.g., Windows, Linux, MacOS
- Selenium is open source tools so it is free
- Selenium support variour popular browsers. ie. IE, Chrome, Firefox
- Easily integrated with many CI tools., Bamboo, Jenkins, Teamcity
- Using Allure reporting tool, nice test reports can be generated
- Pytest has plenty of plugins which can be used to enhance the capability of testing tool in short time
- Allure support Jenkins, Bamboo

# Con
- Selenium does not support desktop application
- It is difficult to mangage dynamic properties using Selenium 

#How this may be used in a wider team (think about different life cycles(Kanban/Scrum))?

#Scum
- During sprint, corresponding test cases can be added 
- Using nightly build, features added can be tested using CI tools
- At the end of each sprint, tests can be executed on staging envirnoment as a regression suite

# Kanban
- Kanban also uses PULL, test cases can be added as features are added
- At the same it, automated test can be integrated in build pipline for verification. So features can be verified and delivered to customer as soon as features are completed

# What would be required to adopt in a Product Engineering team?
- Reports play import role, Product Engineering team should keep eye on report so they can immediate feedback that features are completed successfully
- Based on report, they proritize features/bugs tickets to be fixed/developed for future delopement


###End
