#Textile Fabric Consultants Inc.
This is the in-development website for Textile Fabric Consultants Inc. Built with the Django framework, there are several applications that make up the site:
1. blog
2. companion
3. webstore

##How to load the project
###Components neeeded
####Python
####Django
#####Plugins
####Elastic Search
####PHP / Apache
####Bootstrap
####jquery
###Running

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
