# -- encoding: utf-8 --

# Copyright 2014 Applied Informatics Inc.
# @author  Nickolas Whiting  <nickolas@trialx.com>

TEST_AUTH_TOKEN = 'ashf087qwb3874ch3q123d'

# Django
from django.http import HttpResponse

class FHIRResponseHeader:
    """FHIRResponseHeader publishes the type of response into the header.
    """
    def process_response(self, request, response):
        """Injects the "Content-Type" header into the response.
        """
        response['Content-Type'] = 'application/json'
        return response

class FHIRRequestAuthorizationToken:
    """FHIRRequestAuthorizationToken parses an access token and validates the 
    authorization of the request.

    Currently this validates strictly aganist the 
    """ 
    def process_request(self, request):
        """Validates the authorization of the request.
        """
        unauthorized = HttpResponse("""<h1>401 Unauthorized</h1>""",status=401)
        meta = getattr(request, 'META')
        if 'HTTP_AUTHORIZATION' not in meta:
            return unauthorized
        try:
            bearer, token = meta['HTTP_AUTHORIZATION'].split('Bearer', 2)
        except:
            return unauthorized
        if token.strip() != TEST_AUTH_TOKEN:
            return unauthorized