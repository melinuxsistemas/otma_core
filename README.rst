=====
Otma Core
=====

Core for company projects django.
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "otma_core" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'otma_core',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('core/', include('otma_core.urls')),

3. Run `python manage.py migrate` to create the core models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to verify core models (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/core/ to participate in the poll.