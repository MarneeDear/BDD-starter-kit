# BDD Starter Kit
Getting started with BDD and automated UI testing.

This project has examples of using both [splinter](https://github.com/cobrateam/splinter) and [behaving](https://github.com/ggozad/behaving). 

**To get started:**

1. Install Python. Either v 2.7 or 3+ will work
2. Install Python pip (Google to find instructions for your environment). You might already have it installed. On the command line try ```pip```. You should see the help.
3. Install [virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)
  
    a. ```pip install virtualenv```
4. Clone this repo
5. Create a virtual environment. Follow the link above if you don't know how to do that. I like to put my virtual environment folders in the same folder as my project. So you might like to go into the folder where you clone this repo and do it there.
6. Activate your virtualenv
8. pip install all of the requirements (this will install them in your activated virtual environment only)

    a. ```pip install -r requirements.txt```

You now have a virtual environment that you can use to run the sample tests, but you will also need the browser drivers. The default is the gecko driver for Firefox so you will need to install that and make sure it is in your path. 

**On Windows:**

1. Go [here](https://github.com/mozilla/geckodriver/releases) and download the latest geckdriver for you system, probably something like this ``geckodriver-vx.xx.0-win64.zip``
2. Extact the executable (geckdriver.exe) in the zip.
3. Put the executable somewhere convenient. I put mine in c:\seleniumdrivers\geckodriver.exe
4. Add this path to your Path environment variable. Probably best to use the User variables, but system is good too. If you don't know how to do this go [here](http://windowsitpro.com/systems-management/how-can-i-add-new-folder-my-system-path). BE VERY CAREFUL!

**Other systems:**

Please ask Google because I am not sure. I will try this on the Ubuntu sub-system at some point and fill in these instructions.

**Run the behaving tests:**

These commands assume you are using bash. If you are on Windows you can install and use git-bash, which comes with the git Windows install.

1. Close your Firefox or this will not go so good.
2. Using the command line go to where you cloned the repo
3. Activate your virutal environment
4. Change directories into behaving_example
5. Do this command in bash. 
  1. ```./bin/behave ./features```

**Run the splinter/behave tests:**

1. Close your Firefox or this will not go so good.
2. Using the command line go to where you cloned the repo
3. Activate your virutal environment
4. Change directories into splinter_example
5. Do this command in bash. 
  1. ```./bin/behave ./features```
