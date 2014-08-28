#Textile Fabric Consultants Inc.
This is the code for the in-development website for Textile Fabric Consultants Inc. Built with the Django framework, there are several applications that make up the site:
1. Blog
2. Textile Companion app
3. Webstore
4. Main page (home page, about us)

##How to load the project
###Components neeeded
####Python
This Django project uses Python 2.7.6 or 2.7.7. It should be compatible with 2.6 as well, and there is Django for Python 3, but this code is written for Python 2.
So, install Python if not already installed and verify that it is working properly.
####Django
https://docs.djangoproject.com/en/1.6/
Using version 1.6, the current version when the project was started. It may be worth considering moving to version 1.7 because it includes some helpful database migration tools. 

Instalation instructions:
https://docs.djangoproject.com/en/1.6/topics/install/#installing-official-release
As discussed in the docs, you can install everything inside of a python virtualenv. I didn't, but I think that would be a good idea. That would make the project much more portable. Actually, you could build a virtualenv with everything installed, then just have that on git so that everyone has the same environment.

Before installing Django, you'll need to have pip installed.
http://www.pip-installer.org/en/latest/installing.html#using-the-installer
If you are using Windows, this may be easier:
https://sites.google.com/site/pydatalog/python/pip-for-windows

Install django with `pip install Django`. If on a unix system, you may need to put `sudo` before pip commands.
#####Plugins
The usefulness of Django really comes from all of its plugins. Or maybe all of its plugins just provide basic functionality that you need to make a website work. Regardless, there's a bunch to install and this may not be a complete list. When you try to run the server, you'll get a sort-of-meaningful error message if you are missing a plugin. Some of these aren't used currently but might be useful. To install each of these, do `pip install` and then the name of the plugin. Most of these will have their documentation at readthedocs https://readthedocs.org/
- django-bootstrap-toolkit
	- Bootstrap is the frontend framework for this site, which works in with Django templates through this plugin.
- django-admin-bootstraped
	- Makes the admin pages look really nice!
- south
	- Database migration tool. Not used anymore after we did some structural changes to the db and had to manually rebuild it.
- django-endless-pagination
	- Really great tool for splitting content up over multiple pages or use lazy loading and infinite scrolling. Not sure if anything on the site is using it right now, but it is worth looking into since it makes a typically tricky task very simple.
- Pillow
	- A derivation of PIL, the python imaging library. There's a whole bunch of versions out there, but this one should work.
	- http://pillow.readthedocs.org/en/latest/installation.html
- django-imagekit
	- provides the images resizing and cropping for dynamically adding companion app items and store items.
	- http://django-imagekit.readthedocs.org/en/latest/index.html
- haystack
	- special installation: `pip install -e git+https://github.com/toastdriven/django-haystack.git@master#egg=django-haystack`
	- Find a needle in a haystack. Provides search for Elasticsearch
- pyelasticsearch
	- install the plugin, but there are other steps involved. See the next section.
- django-crispy-forms
	- Used for the forms for login / account info.
	- http://django-crispy-forms.readthedocs.org/en/latest/genindex.html
- django-embed-video
	- Not used. The idea was for embeding videos for the companion app, but youtube works best for that.
- django-annoying
	- Cleans up some "annoying" things in the django framework. https://github.com/skorokithakis/django-annoying
- django-jsonview
	- Basically lets django work with json objects similarly to javascript.
	- https://github.com/jsocol/django-jsonview
- pytz
	- Time zones. Date and times are magically localized.
- requests
	- It fixes the problems with python's built in HTTP
	- http://docs.python-requests.org/en/latest/


####Elastic Search
Check out http://www.elasticsearch.org/
This provides the search functionality on different parts of the site. It's really powerful, and could be used for more (blog searching, description searching on the companion app). Gerenally for search, you would just make database queries (I actually think that would be simpler for the webstore). Elasticsearch however makes it possible to search large amounts of text.
In addition to the django plugin, you also need to have a standalone program installed on your computer, or the server when it is deployed. This program powers the search, so if you are running the site and want to use the search features, you will also need to run the elasticsearch program. Also, in order for image upload from the admin pages to work, elasticsearch *must* be running.
Download the client for your system at http://www.elasticsearch.org/overview/elkdownloads/

On Mac / Linux, navigate to its directory and run it with `./elasticsearch -f`
On Windows, `.\bin\elasticsearch`

####PHP / Apache
This is a Django application, so what's this about PHP??
In order to calculate shipping for the webstore, you have to get the prices from the shipping companies' api, which is PHP for UPS. FedEx and USPS also have PHP api's, but there are some other options as well. This piece of the project is not fully implemented, but see the UPS_Calculator section for more information.
- Install an Apache server and set up PHP. Lots of different ways to do this!
- MAMP is simple for Mac, WampServer is simple for Windows

####Bootstrap
Bootstrap is the magical front-end framework that makes the site look pretty, format correctly on all browsers, and respond to different browser sizes so the site works great on mobile, tablet, and desktop. No additional setup is needed; it's all in the project already.
Learn *everything* here:
http://getbootstrap.com/

####Stripe
Payments are (or would be) handled by Stripe https://stripe.com/
It's not very tightly integrated at this point, but we made this choice mainly for security and ease of use reasons.

####jquery / AJAX
###Running the site

##Layout of source code
###.idea
###UPS_Calculator
###avatars
The images that are uploaded and processed for the webstore and companion app are stored here.
###blog
###companion
###frontend
###mysite
###src
###static
###store_images
###templates
###webstore

##Database
###Background
###Schema
###Migrations

##Current development
###Incomplete features
###Known issues

-----
Current Development version of the Tektiles App for Textile Fabric Inc


1. Inorder for the package to work you must have python and django installed.

2. unpack the archive to your home directory
	$tar xf filename 

3. in your home directory issue:

	$python manage.py runserver
	
   3.1 
	This will start a local webserver at the loopback address on port 8000
	**alternative: you can specify the address and port by appending it to the end of the cmd 
	e.g. 
		$python manage.py runserver 10.0.1.25:8080

		note: The port you choose may be protected by the os and you may have to run as super user.

   3.2
	Once the server is running, test by opening your web browser and enter 127.0.0.1:8000/ this will 		show the boot page for the django app
