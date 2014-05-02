# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # What is Django
# "The web framework for perfectionist with deadlines"
# 
# # What is a Web Framework
# 
# >A web application framework (WAF) is a software framework that is designed to support the development of **dynamic websites, web applications, web services and web resources.** The framework aims to alleviate the overhead associated with common activities performed in web development. For example, many frameworks provide libraries for database access, templating frameworks and session management, and they often promote code reuse. [wikipedia](http://en.wikipedia.org/wiki/Web_application_framework) 
# 
# # History of Django
# * Started as a content management system for  Lawrence Journal-World (Kansas)
# * Development started in 2003
# * Released 2005
# * Named after?
# 
# # Basic Architecture of Django
# * Model-View-Controller
# * Separate
# 	* Data Representation (Model)
# 	* From How Data are Displayed (View)
# 	* From Logic of Program (Controller)
# 	
# # Model
# * An object-relational mapper 
# * Maps a Python Class (object) to a Relational Model
# 	
# # Model: Object
# * models.py
# ~~~~~~~~~~
# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     middle_name = models.CharField(max_length=30,
#                                    blank=True)
#     last_name = models.CharField(max_length=40,
#                                  blank=True)
#     def __unicode__(self):
#         return u'%s %s %s'%(self.first_name,
#                             self.middle_name,
#                             self.last_name)
# ~~~~~~~~~~~
# 
# # Model: Object
# 
# ~~~~~~~~~~
# class Author(models.Model):
# ~~~~~~~~~~~
# **Inherits from Basic Django Model**
# 
# ~~~~~~~~~
#     middle_name = models.CharField(max_length=30,
#                                    blank=True)
#     last_name = models.CharField(max_length=40,
#                                  blank=True)
#     def __unicode__(self):
#         return u'%s %s %s'%(self.first_name,
#                             self.middle_name,
#                             self.last_name)
#                             
# # Model: Object
# 
# ~~~~~~~~~~
# class Author(models.Model):
# 
#     middle_name = models.CharField(max_length=30,
#                                    blank=True)
#     last_name = models.CharField(max_length=40,
#                                  blank=True)
#     def __unicode__(self):
#         return u'%s %s %s'%(self.first_name,
#                             self.middle_name,
#                             self.last_name)
# ~~~~~~~~~~~~~~

# <markdowncell>

# * Pre-defined data types
# 
# ~~~~~~~~~~~
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.IntegerField(blank=True)
#     def __unicode__(self):
#         return u'%s %s'%(self.title,self.authors)
# ~~~~~~~~~~~~~~~
# 
# * ForeignKeys
# 
# # Views
# * HTML code to define how Models are presented to user
# 
# # Views
# 
# ~~~~~~~~~~~~~~
# {% extends "quotebook.html" %}
# {% block qb %}
# <h2> Create New Author </h2>
# <p></p>
# <table border="0">
#     <tbody>
#         <tr><form action="." method="POST"> 
#             <td>
#                 {{author.as_table}}
#             </td>
#             <td>
#                 <input name="submit" value="Save" 
#                             stype="submit">
#             </td>
#         </tr>
#     </tbody>
# </table>
# {% endblock %}
# ~~~~~~~~~~~~~~~~~~~~~~
# 
# # Views: Code Reuse
# 
# ~~~~~~~~~
# {% extends "cf5Base.html" %}
# {% load markup %}
# {% block content %}
# <p><a href="../addpublisher">Add Publisher</a>, 
# <a href="../addauthor">Add Author</a>, 
# <a href="../addbook">Add Book</a>, 
# <a href="../addquote">Add Quote</a></p>
# <p><a href="../viewquotes">View Quotes</a></p>
# {% block qb %}
# 
# {% endblock qb %}
# 
# {% endblock content %}
# ~~~~~~~~~~~~~~~~~
# * **extends**
# 
# 
# # Model
# ![Author View](./authorView.png)
# 
# # Model
# ![Book View](./bookView.png)
# 
# # Controls
# 
# ~~~~~~~~~~~~
# @login_required
# def createBook(request):
#     try:
#         user = request.user
#         #print request.method
#         if( request.method == 'POST' ):
#             submittype = request.POST['submit']
#             b = BookForm(request.POST)
#             newB = b.save(commit=False)
#             newB.user = request.user
#             newB.save()
#             b.save_m2m()
#             return render_to_response("quotebook.html",
#                               { "usrname":user.username,
#                               "href":'/accounts/logout/',
#                                "hrefWrite":"/write",
#                                "hrefBrowse":"/browse"})
# 
# ~~~~~~~~~~~~~~~~~~
# 
# # Views (continue)
# 
# ~~~~~~~~~~~~~~
#         b = BookForm()
#         return render_to_response('book.html',{"book":b,
#                             "usrname":user.username,
#                             "logout":'/accounts/logout/',
#                             "listing":'/select'})
#     except Exception, error:
#         pass #print "error",error
# ~~~~~~~~~~~~~~~~~
# 
# # URL Mapping
# 
# ~~~~~~~~~
#     (r'^select/$','family.views.selectProgram'),
#     (r'^browse/$','family.journal.views.browser'),
#     (r'^recordweather/$',
#        'family.weather.views.createEntry'),
#     (r'^viewweather/$',
#        'family.weather.views.browser'),
#     (r'^addauthor/$',
#        'family.quotebook.views.createAuthor'),
#     (r'^addbook/$',
#        'family.quotebook.views.createBook'),
#     (r'^addpublisher/$',
#        'family.quotebook.views.createPublisher'),
# ~~~~~~~~~~~~
# 
# # Settings
# * Define database
# * Operating environment
# * Registered Apps
# 
# # Settings: Database
# 
# ~~~~~~~~
# LOGIN_URL = '/delphi/accounts/login/'
# LOGIN_REDIRECT_URL = '/delphi/select/'
# LOGOUT_REDIRECT_URL = '/delphi/accounts/logout/'
# MANAGERS = ADMINS
# 
# DATABASE_ENGINE = 'sqlite3'         
# DATABASE_NAME = '/Users/brian/family.db'  
# #  path to database file if using sqlite3.
# DATABASE_USER = ''             # Not used with sqlite3.
# DATABASE_PASSWORD = ''         # Not used with sqlite3.
# DATABASE_HOST = ''             # Set to empty string for localhost. 
# 							   # Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. 
# 							   # Not used with sqlite3.
# ~~~~~~~~~~~
# 
# # Settings: Registered Apps
# 
# ~~~~~~~~~
# INSTALLED_APPS = (
#     'django.contrib.auth',
#     'django.contrib.admin',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'family.journal',
#     'family.weather',
# 	'family.quotebook',
#     'django.contrib.markup',
# )
# ~~~~~~~~~~~~~~~~~~
# 
# # Creating a Django Site
# * pip install django
# 	* installs django in the Python distribution site-packages
# 	* installs the executable script django-admin.py
# 	* django-admin.py is used to create projects (top-level collection of apps)
#     

# <codecell>

!pip install django

# <codecell>

!django-admin.py startproject cbc

# <markdowncell>

# * django-admin.py startproject delphi
# 
# # Creating a Django App
# * Use a third party package (install with pip)
# * Create your own
# 	* python manage.py startapp APPNAME
#     * This creates an empty package (notice the \_\_init\_\_.py file)
#         * admin.py
#         * models.py 
#         * tests.py
#         * views.py
#         

# <codecell>

!python manage.py startapp quotebook

# <markdowncell>

# 		
# >What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular Web site. A project can contain multiple apps. An app can be in multiple projects. [Django Tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/)

# <markdowncell>

# ## Having created an app, we need to register it

# <codecell>

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quotebook',
)

# <markdowncell>

# ## Edit delphi/models.py

# <codecell>

from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30,blank=True)
    country = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s %s %s'%(self.name,self.city, self.country)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    def __unicode__(self):
        return u'%s %s %s'%(self.first_name,self.middle_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.IntegerField(blank=True)
    def __unicode__(self):
        return u'%s %s'%(self.title,self.authors)

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author)
    source = models.ForeignKey(Book)
    page = models.CharField(max_length=4,blank=True)
    chapter = models.CharField(max_length=100,blank=True)
    def __unicode__(self):
        return u'%s \n%s \n%s'%(self.text,self.author,self.source)

# <markdowncell>

# ## Having modified models.py
# * Sync the database
#     * syncdb

# <codecell>

!python manage.py syncdb

# <markdowncell>

# ## Django has a powerful admin interface
# * This is largely why Django gained popularity
# * we can register our Models so that they can be viewed/modified in the admin interface.
# * modify admin.py

# <codecell>

from django.contrib import admin
from quotebook.models import Book, Quote, Author, Publisher

admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(Publisher)

# <markdowncell>

# ## Edit Views
# * create views.py file

# <codecell>

from django.shortcuts import render
from django.http import HttpResponse

from forms import * 

###@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the quotebook index.")
def createAuthor(request):
    try:
        user = request.user
        if( request.method == 'POST' ):
            submittype = request.POST['submit']
            a = AuthorForm(request.POST)
            newA = a.save(commit=False)
            newA.user = request.user
            newA.save()
            a.save_m2m()
            return render(request,"quotebook.html",
                              { "usrname":user.username,
                              "href":'/accounts/logout/',
                               "hrefWrite":"/write",
                               "hrefBrowse":"/browse"})
        a = AuthorForm()
        return render(request,'author.html',{"author":a,"usrname":user.username,"logout":'/accounts/logout/',
                              "listing":'/select'})
    except Exception, error:
        pass #print "error",error

#@login_required
def createBook(request):
    try:
        user = request.user
        #print request.method
        if( request.method == 'POST' ):
            submittype = request.POST['submit']
            b = BookForm(request.POST)
            newB = b.save(commit=False)
            newB.user = request.user
            newB.save()
            b.save_m2m()
            return render(request,"quotebook.html",
                              { "usrname":user.username,
                              "href":'/accounts/logout/',
                               "hrefWrite":"/write",
                               "hrefBrowse":"/browse"})
        b = BookForm()
        return render(request,'book.html',{"book":b,"usrname":user.username,"logout":'/accounts/logout/',
                              "listing":'/select'})
    except Exception, error:
        pass #print "error",error
   
#@login_required
def createPublisher(request):
    try:
        user = request.user
        #print request.method
        if( request.method == 'POST' ):
            submittype = request.POST['submit']
            p = PublisherForm(request.POST)
            newP = p.save(commit=False)
            newP.user = request.user
            newP.save()
            p.save_m2m()
            return render(request,"quotebook.html",
                              { "usrname":user.username,
                              "href":'/accounts/logout/',
                               "hrefWrite":"/write",
                               "hrefBrowse":"/browse"})
        pp = PublisherForm()
        return render(request,'publisher.html',{"pp":pp,"usrname":user.username,"logout":'/accounts/logout/',
                              "listing":'/select'})
    except Exception, error:
        pass #print "error",error
   
#@login_required
def createQuote(request):
    try:
        user = request.user
        if( request.method == 'POST' ):
            submittype = request.POST['submit']
            q = QuoteForm(request.POST)
            newQ = q.save(commit=False)
            newQ.user = request.user
            newQ.save()
            q.save_m2m()
            return render(request,"quotebook.html",
                              { "usrname":user.username,
                              "href":'/accounts/logout/',
                               "hrefWrite":"/write",
                               "hrefBrowse":"/browse"})
        q = QuoteForm()
        return render_to_response('quote.html',{"quote":q,"usrname":user.username,"logout":'/accounts/logout/',
                              "listing":'/select'})
    except Exception, error:
        pass
        #print "error",error

def searchQuotes(request):
    try:
        all_quotes = Quote.objects.all().order_by("author")
        return render(request,"viewquotes.html",{'rslts':all_quotes})
    except Exception, error:
        pass #print "failed in searchQuotes", error


#@login_required
def displayMainQB(request):
    
    user=request.user
    username=request.user.username
    return render(request,"quotebook.html",
                              { "usrname":username,
                              "href":'/accounts/logout/',
                               "hrefWrite":"/write",
                               "hrefBrowse":"/browse"})

# <markdowncell>

# ## Edit URLS
# * modify site url.py to point to app url.py
# * add urls to url.py
# * url takes four arguments
#     * regex to catch webaddress (required)
#     * view to invoke (required)
#     * kwargs (optional keyword arguments)
#     * name (optional name for url)

# <codecell>

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'delphi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^quotebook/',include('quotebook.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# <codecell>

from django.conf.urls import patterns, url
from quotebook import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^addauthor/$',views.createAuthor,name='add_author'),
    url(r'^addbook/$',views.createBook,name='add_book'),
    url(r'^addpublisher/$',views.createPublisher,name='add_publisher'),
    url(r'^addquote/$',views.createQuote,name='add_quote'),
    url(r'^quotebook/$',views.displayMainQB,name='view_quotebook'),
    url(r'^searchquotes/$',views.searchQuotes,name='search_quotebook')
)


# <markdowncell>

# # Finding Third Party Apps
# * [Django Packages](https://www.djangopackages.com)
# 
# # [Django Calendaring Apps](https://www.djangopackages.com/grids/g/calendar/)
# * [django-schedule](https://www.djangopackages.com/packages/p/django-schedule/)
# 	* Stable (~5-years-old)
# * [[django-scheduler](https://www.djangopackages.com/packages/p/django-scheduler/)
# 	* Newer project, seems to be same developers as django-schedule
# 	

# <codecell>


