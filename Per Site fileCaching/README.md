The Per Site  Cachings

for this type of caching you need to add middleware just above common middleware in settings.
and one caching middleware just below common middleware.

And to save that cache in file add cache in end of settings.py. 


it is a more granular way to use the Cachings framework is by
Caching the outputof individual views.
django.views.decorators.cache defines a cache_page decorator
that will automatically cache views response. if multiple urls poiny
at same view, each url will be cached seprately.    

In  this poc open course template and runserver. once you hit home page, 
immidetly delete last 2 courses and withing 30 second refresh the page you will notice
that you get still previous page content, because it comming from cache, but after 30 second
when you again hit home page you get new content from template you have edited.

this will work  at whole site. and you can see in db 
cache_key, value,expiry if you open in any ide.

