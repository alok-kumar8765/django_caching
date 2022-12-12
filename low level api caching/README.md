The Template Fregment Cachings

the cache will stored in db as mentioned in settings

in template cache, first we load cache,
then we add data in jija template. eg :-
    <h1>Course 1</h1>
        <h1>Course 2</h1>
        {%cache 30 course %}
        <h1>Course 3</h1>
        <h1>Course 4</h1>
        {%endcache course%}

as you see if i changed in couser 1 and 2 it immiditey reflact, but
course 3 and 4 data comes from cache after 30 sec it will give current change.