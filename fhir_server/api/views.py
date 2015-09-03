# -- encoding: utf-8 --

# Copyright 2014 Applied Informatics Inc.
# @author  Nickolas Whiting  <nickolas@trialx.com>


# Django
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import View
from django.core.urlresolvers import reverse

# OAuth
from oauth2_provider.views.generic import ReadWriteScopedResourceView

# Python
import json

from .tmp import TMP_USER

class FHIRScopedView(ReadWriteScopedResourceView):
    """Overwites the 403 Response with a 401 when unauthorized."""
    def dispatch(self, request, *args, **kwargs):
        p = super(FHIRScopedView, self).dispatch(request, *args, **kwargs)
        if isinstance(p, HttpResponseForbidden):
            return HttpResponse(status=401)
        return p

class PatientView(FHIRScopedView):

    required_scopes = ['user/*.read']

    """Fetches a Patient resource from the given id.

    Currently this really does nothing and returns the same info with the given 
    id.
    """
    def get(self, request, id, extension=None):
        return HttpResponse(json.dumps(TMP_USER))

class PatientSearch(FHIRScopedView):

    required_scopes = ['user/*.read']

    """Fetches a Patient using search.

    Currently this really does nothing and returns the same info with the given 
    id.
    """
    def get(self, request, extension=None):

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

class SMARTOAuthMetaData(View):
    """Respondes to the EHR Conformance statement.

    Right now this only returns information pertaining to the security.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps({
            "resourceType": "Conformance",
            "rest": [{
                "security": {
                    "extension": [{
                        "url": "http://fhir-registry.smarthealthit.org/StructureDefinition/oauth-uris",
                        "extension": [
                        {
                            "url": "token",
                            "valueUri": request.build_absolute_uri(reverse("oauth2_provider:token"))
                        },
                        {
                            "url": "authorize",
                            "valueUri": request.build_absolute_uri(reverse("oauth2_provider:authorize"))
                        }]
                    }],
                }
            }]
        }))
