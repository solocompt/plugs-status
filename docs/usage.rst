=====
Usage
=====

To use Plugs Status in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'plugs_status.apps.PlugsStatusConfig',
        ...
    )

Add Plugs Status's URL patterns:

.. code-block:: python

    from plugs_status import urls as plugs_status_urls


    urlpatterns = [
        ...
        url(r'^', include(plugs_status_urls)),
        ...
    ]
