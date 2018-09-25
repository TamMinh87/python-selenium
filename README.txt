PROJECT STRUCTURE
.
|__allure						# Store allure result (json format)
|__api 									 
   |__common.py 					# Common functions like send_request, check_response, check_data_schema
   |__formsite_api.py					# Specific implementation for formsite api like get_result, get_result_count
|__config
   |__behave.ini 					# Behave is BDD library, this file stores some environment configs 
   							  which can override by command param (e.g os, browser, etc...)
   |__config_api.ini 					# Store config for api (e.g. api-key, end-point)
   |__config_ui.ini 					# Store config for ui (e.g. username, password, url)
   |__config_parser.ini
|__data							# Store the test-data
|__features
   |__steps 						# "steps" folder is must under "features" folder
      |__common_steps.py 				# Define "step" which can re-use in many places
      |__utils.py 					# Define common functions like read_test_data, compare_value, etc... 
      |__lead_capture_steps.py 				# Specific steps for Lead Capture feature
      |__...
   |__environment.py 					# This is the entry point  
   							  and the place to define code to run before 
							  and after certain events during your testing
   							  (before_all, after_all, before_feature, after_feature, etc...)
   |__capture-lead.feature 				# Store all scenarios for Lead Capture Feature
   |__...
|__pages
   |__base_page.py 					# Define some basic functions to interacte with web page 
   							  (e.g. get html element, load website, click action, etc...)
   |__lead_capture_form.py 				# Define all HTML elements and function for Lead Capture form
   							  (e.g. submit form, submit empty form, verify input data, etc...)
   |__login_form.py 					# Same as above but for Login form
   |__thank_you_pape.py 				# Same as above but for Thank You page
   |__...
|__screenshots 						# Store screenshot of failed step

Workflow of the test
1. Go to "environment.py" to do init the browser
2. Go to *.feature file to read the scenario
3. Perform action for each step
4. Back to "environment.py" to take picture for each step if test failed
5. Loop #2, #3, #4 for all steps, all scenarios
6. Back to "environment.py" and quit browser

How to debug
1. Run test by IDE: add wip.feature file and debug as normal (wip = work in progress)
2. Run test by command: 
	- pip install ipdb
	- Now in you test import ipdb and the step you want to start the debugging insert ipdb.set_trace()
	- more details in http://automationtipsntricks.blogspot.com/2017/08/pip-install-ipdb-debugging-python.html


SETUP PROJECT (MacOS, Linux)
1. Install python 3.6.6, chromedriver, geckodriver on target machine

2. Put latest source code to target machine (pull from repository or unzip, etc...)

3. Use terminal to go to that folder (e.g. cd workspace/python-selenium)

4. Create virtual environment
    - python3 -m venv venv (command on MacOS)
 		- first venv is the command
 		- second venv is the folder name
 	- https://docs.python.org/3/library/venv.html

5. Use virtual environment
 	- source venv/bin/activate
 	- type "deactivate" when you want to exit virtual environment

6. Install dependencies to virtual environment
 	- pip install - r requirements.txt

7. Run test
	- behave -f allure_behave.formatter:AllureFormatter -o allure/ ./features -D browser=chrome
	    - ./features: run all features
	    - can specify the feature to run by pointing directly to that file/folder (e.g. features/capture-lead.feature)
        - able to run test by tags: --tags=wip --tags=p1 --tags=smoke --tags=negative
	- browser=chrome: change browser by replacing browser=chrome by browser=firefox (can add more browsers depend on your need)

8. Generate report
	- allure serve ./allure/


QUESTION
If we wanted to run this test as part of CI or nightly build process how could we host the test and alert us as to the results or failure of the test?

We have 3 items in above question
1. run this test as part of CI or nightly build process ?
We can run UI tests as part of CI if we make sure they're fast otherwise I prefer nightly build process, why?
 - "Keep the build fast" is one of practice for Continuous Integration, development-team should not wait 10 minutes (or more) for each commit
 - UI tests always take time to run (than unit-test, integration-test, api-test)
 - UI tests may need an deployment to be able to run

2. how could we host the test ?
 - please see SETUP PROJECT part in README file
 	- put the project to nightly build machine or CI machine
 	- use command to trigger the test

3. alert us as to the results or failure of the test ?
 - we can send Email or send notification to Slack (Jenkins supports both)
