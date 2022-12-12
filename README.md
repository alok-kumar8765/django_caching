# django_caching
In this Repository there are types of caching mentioned as django provided. There are basically 3 type of caching, template, per view and per site caching technique, and we save our cached data in file, data base and local memory. all types of caching practical have in this repository. 

## Requirements :
pip install django

## What is Django cache?
>    Django comes with its own caching system that lets you save your dynamic pages, to avoid calculating them again when needed. The good point in Django Cache framework is that you can cache −

       - The output of a specific view.
       - A part of a template.
       - Your entire site.

    To use cache in Django, first thing to do is to set up where the cache will stay. The cache framework offers different possibilities - cache can be saved in database, on file system or directly in memory.

## How does caching work ??
    ** Local Memory Cache **
>    Unless we explicitly specify another caching method in our settings file, Django defaults to local memory caching. As its name implies, this method stores cached data in RAM on the machine where Django is running. Local memory caching is fast, responsive, and thread-safe. 

    To set up local memory caching, the CACHES section of our Django settings file should look like this (swap out the cache location for yours):

        CACHES = {

        'default': {

            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',

            'LOCATION': 'your-memory-location-will-go-here-see-docs-for-more',

        }

    ** Filesystem Cache **
>    A filesystem cache uses significantly less memory than in-memory caching. However, it comes at the cost of being considerably slower than an in-memory cache. Aside from those two factors, its trade-offs are similar to those of local memory caching.

    The CACHES section of your Django settings file should look something like this:

        CACHES = {

        'default': {

            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',

            'LOCATION': 'filesystem directory where Django will save cache files',

        }

    ** Memcached **
>    Memcached is an efficient cache implementation. It’s the fastest caching method that Django works with out of the box. You may be surprised to hear that many high-traffic sites rely on Memcached to reduce database queries, including Facebook and Wikipedia.
        One such configuration (running on localhost) looks like this:

        CACHES = {

        'default': {

            'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',

            'LOCATION': '127.0.0.1:11211',

        }

        }

    ** Database Caching **
>    Django is also capable of leveraging our existing database for caching. Setup is straightforward: we just need to provide the name of the database table to store cache data. A database-backed cache doesn’t perform as well as in-memory caching.

    To use database caching, we place the following code in the CACHES section of the settings file:

        CACHES = {

            'default': {

                'BACKEND': 'django.core.cache.backends.db.DatabaseCache',

                'LOCATION': 'the_table_name_for_the_cache',

            }

        }

    ** Custom Cache Implementation **
>    If we don’t like any of Django’s default caching options, we can add our own. We just need to create a class that extends BaseCache. As a starting point, we can look at Django’s dummy cache implementation. Our custom cache provider class should implement the same methods as the dummy cache class, replacing the code in each method with code that interacts with our preferred cache storage backend. 

    We can configure a custom cache implementation by providing only the path of our provider class.

    To use a custom implementation, the CACHES section in our settings file should look like this, with the appropriate path swapped in:

        CACHES = {

        'default': {

            'BACKEND': 'path.to.backend',

        }

        }

### Google Doc Viewr Mode : 

> Base url: <a href="https://docs.google.com/document/d/19OJlPNzKIgjb1_CR3LEcnqeH8fomxG7j8or1L2H8P2s/edit?usp=sharing" target="_blank">[Google Doc]</a>

> [Google Doc](doc:https://docs.google.com/document/d/19OJlPNzKIgjb1_CR3LEcnqeH8fomxG7j8or1L2H8P2s/edit?usp=sharing)

> Full URL of the document: [Google Doc](doc:https://docs.google.com/document/d/19OJlPNzKIgjb1_CR3LEcnqeH8fomxG7j8or1L2H8P2s/edit?usp=sharing.pdf#anchor-links)

> {google_docs}(doc:https://docs.google.com/document/d/19OJlPNzKIgjb1_CR3LEcnqeH8fomxG7j8or1L2H8P2s/edit?usp=sharing.pdf{/google_docs}$anchor-links)