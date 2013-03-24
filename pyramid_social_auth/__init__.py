from social.exceptions import (
    AuthFailed,
    AuthCanceled,
    )

from social.apps.actions import (
    do_auth,
    do_complete,
    )

from strategy import PyramidStrategy

class AuthenticationComplete(object):
    """An AuthenticationComplete context object"""
    def __init__(self, *args, **kwargs):
        pass


class AuthenticationDenied(object):
    """An AuthenticationDenied context object"""
    def __init__(self, *args, **kwargs):
        pass


def register_provider(settings, provider):
    providers = settings.get('login_providers',dict())
    providers[provider.name] = provider
    settings['login_providers'] = providers

def locate_provider(request):
    provider_name = request.matchdict['provider']
    providers = request.registry.settings.get('login_providers')
    return (provider_name, providers[provider_name])

def strategy_settings(request, name):
    settings = request.registry.settings
    consumer_key = settings.get('psa.{0}.consumer_key'.format(name))
    consumer_secret = settings.get('psa.{0}.consumer_secret'.format(name))
    scope = settings.get('psa.{0}.scope'.format(name), [])
    if scope:
        scope = [s.strip() for s in scope.split(',')]

    redirect_uri = request.route_url('psa.callback', provider=name)
    strategy_settings = dict(
        KEY=consumer_key,
        SECRET=consumer_secret,
        SCOPE=scope,
        REDIRECT_URI=redirect_uri,
    )
    return strategy_settings

def login(request):
    name, provider = locate_provider(request)
    settings = strategy_settings(request, name)
    strategy = PyramidStrategy(backend=provider, request=request,
                               storage=None,
                               redirect_uri=settings.get('REDIRECT_URI'))
    strategy.settings = settings
    do_auth(strategy)

def callback(request):
    name, provider = locate_provider(request)
    settings = strategy_settings(request, name)
    strategy = PyramidStrategy(backend=provider, request=request,
                               storage=None,
                               redirect_uri=settings.get('REDIRECT_URI'))
    strategy.settings = settings
    try:
        do_complete(strategy, login=request.session.get('user_id'))
    except (AuthFailed, AuthCanceled):
        return AuthenticationDenied(provider_name=name)

def includeme(config):
    config.add_route('psa.callback', '/{provider}/callback')
    config.add_route('psa.login', '/{provider}')

    config.add_view(view=login, route_name='psa.login')
    config.add_view(view=callback, route_name='psa.callback')

