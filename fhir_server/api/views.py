# -- encoding: utf-8 --

# Copyright 2014 Applied Informatics Inc.
# @author  Nickolas Whiting  <nickolas@trialx.com>


# Django
from django.http import HttpResponse
from django.views.generic import View

# Python
import json

from .tmp import TMP_USER

class PatientView(View):
    """Fetches a Patient resource from the given id.

    Currently this really does nothing and returns the same info with the given 
    id.
    """
    def get(self, request, id):
        return HttpResponse(json.dumps(TMP_USER))

class PatientSearch(View):
    """Fetches a Patient using search.

    Currently this really does nothing and returns the same info with the given 
    id.
    """
    def get(self, request):

        allowed = {
            'name': TMP_USER['name'][0]['text'], 
            'family': TMP_USER['name'][0]['family'], 
            'given': TMP_USER['name'][0]['given'], 
            'identifier': TMP_USER['id'], 
            'gender': TMP_USER['gender'], 
            'birthdate': TMP_USER['birthDate']
        }
        results = []
        for term, value in request.GET.iteritems():
            if term in allowed and value == allowed[term]:
                results.append(TMP_USER)
                break
        return HttpResponse(json.dumps({
            'resourceType': 'Bundle',
            'type': 'searchset',
            'total': len(results),
            'entry': results,
            'link': [{
                'relation': 'self',
                'url': request.build_absolute_uri(),
            }]
        }))