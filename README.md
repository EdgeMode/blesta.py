blesta.py
=========

A python wrapper for the Blesta (www.blesta.com) billing system HTTP API.

Its primary benefit is that it converts a standard python dictionary of parameters, into (Blesta-friendly) JSON.

It also includes a couple of convenience methods for converting the dates and currency values returned by the API
into something more usable.


Usage
-----

After adding your API server, username and key, you can call the api using HTTP verb, blesta class and method.

For example, to queue an invoice for delivery via email:

``` python
import blesta

api = blesta.api()
response = api.call(verb='get', classname='invoices', method='addDelivery',
                    value_dict={
                        'invoice_id': '127',
                        'client_id': '42',
                        'vars': {
                            'method': 'email'
                        }
                    })
```

Consult http://source-docs.blesta.com/package-blesta.app.models.html for a full list of API classes and methods.
