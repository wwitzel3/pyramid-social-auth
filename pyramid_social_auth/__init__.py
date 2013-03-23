from social.apps.actions import do_auth
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
    providers = settings.get('providers',dict())
    providers[provider.name] = provider
    settings['login_providers'] = providers

def login(request):
    provider_name = request.matchdict['provider']
    providers = request.registry.settings.get('login_providers')
    provider = providers[provider_name]

    settings = request.registry.settings
    consumer_key = settings.get('psa.{0}.consumer_key'.format(provider_name))
    consumer_secret = settings.get('psa.{0}.consumer_secret'.format(provider_name))
    scope = settings.get('psa.{0}.scope'.format(provider_name), [])

    strategy_settings = dict(
        KEY=consumer_key,
        SECRET=consumer_secret,
        SCOPE=scope,
    )

    strategy = PyramidStrategy(backend=provider, request=request)
    strategy.settings = strategy_settings

    do_auth(strategy)

def includeme(config):
    config.add_route('psa.login', '/{provider}')
    config.add_view(view=login, route_name='psa.login')

