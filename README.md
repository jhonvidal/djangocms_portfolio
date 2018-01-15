=====
djangocms_portfolio
=====


Quick start
-----------

Install & settings
-------------------

1. Install the app
    ```
    pip install git+https://github.com/jhonvidal/djangocms_portfolio.git@master
    ```


2. Add "portfolio" to your INSTALLED_APPS setting like this
   
    ```python
    
    INSTALLED_APPS = [
        ...
        'portfolio',
    ]
    ```
3. Add in project URLS

    ```python
    
    url(r'^portfolio/', include('portfolio.urls')),
    
    ```
4. Settings Add in settings.py
    ```python
    
    WORK_PAGINATION = 5
    WORK_LIST_TRUNCWORDS_COUNT = 10
    
    ```

5. Migrate

  ```python
    
   ./manage.py migrate
   ```

6. Run Test Server

    ```python
    
    ./manage.py runserver
    
    ```
   
Requirements
------------

```
DjangoCMS http://www.django-cms.org/en/
django-filer & (dependencies) https://github.com/divio/django-filer
django-taggit https://github.com/alex/django-taggit
```
   

URLS
------------

```python

    url(r'^$', PortfolioWorkListView.as_view(), name='portfolio_list'),
    url(r'^tag/(?P<tag>[-\w]+)/$', WorkTagListView.as_view(), name='work_tag'),
    url(r'^category/(?P<category>[-\w]+)/$', WorkCategoryListView.as_view(), name='work_category'),
    url(r'^(?P<slug>[-\w]+)/$', PortfolioWorkDetailView.as_view(), name='work_detail'),

```


Example usage
--------------

Work Models
-----------

Fields

<ul>
    <li>title [CharField]</li>
    <li>pub_date [DateTime]</li>
    <li>Description [HTMLField]</li>
    <li>Category [FK(CategoryWork)]</li>
    <li>Tags [TaggableManager()]</li>
    <li>client [CharField]</li>
    <li>location [CharField]</li>
    <li>Head Picture [FilerImageField]</li>
    <li>folder [FilerFolderField]</li>
</ul>


Work List
----------

Browse List

```Jinja
    {% for work in work_list %}
    ...
    {{work.title}}
    {% endfor %}

```

Work Detail
------------

Get Next Or Previous
<ul>
    <li>For get Next Work (Navigation) `work.get_next_work` => return (URL)</li>
    <li>For get Previous Work (Navigation) `work.get_previous_work` => return (URL)</li>
</ul>

For Get previous work
----------------------

{{work.get_previous_work}}


For Get next work
-----------------

{{work.get_next_work}}


Render work
-----------

<ul>
    <li>Title : {{work.title}}</li>
    <li>Publish at : {{worl.pub_date}}</li>
    <li>Description : {{work.description}}</li>
    <li>Category : {{work.category}}</li>
    <li>Tags : {% for tag in work.tags.all %}{{tag}}{% endfor %}</li>
    <li>client:  {{work.client}}</li>
    <li>location : {{work.location}}</li>
    <li>Head picture : {{work.head_picture}}</li>
    <li>Gallery : {% for picture in work.folder.files %}{{picture.url}}{% endfor %}</li>
</ul>


