The Per View Cachings

it is a more granular way to use the Cachings framework is by
Caching the outputof individual views.
django.views.decorators.cache defines a cache_page decorator
that will automatically cache views response. if multiple urls poiny
at same view, each url will be cached seprately.    

In  this poc open course template and runserver. once you hit home page, 
immidetly delete last 2 courses and withing 30 second refresh the page you will notice
that you get still previous page content, because it comming from cache, but after 30 second
when you again hit home page you get new content from template you have edited.

this will work for only at those view on which you mention decorater. and you can see in db 
cache_key, value,expiry if you open in any ide.

you can use per view cache in urls as well as in views.py
for better understanding there are 2 url, once you hit '' url after that edit in template
now refresh that url, you got previews thing but when you hit home url you get updated data.

in this poc cache save in db.