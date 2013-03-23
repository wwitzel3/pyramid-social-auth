import json
from pyramid.view import view_config
import pyramid_social_auth as psa

@view_config(name='login', renderer='example:templates/login.mako')
def login(request):

    return {
        'providers': request.registry.settings['login_providers'],
    }

@view_config(name='denied', context=psa.AuthenticationDenied, renderer='example:templates/results.mako')
def login_denied(request):
    return {
        'result': 'denied',
    }

@view_config(name='complete', context=psa.AuthenticationComplete, renderer='example:templates/results.mako')
def login_complete(request):
    context = request.context
    results = {
        'profile': context.profile,
        'credentials': context.credentials,
    }
    return {
        'result': json.dumps(results, indent=4),
    }
