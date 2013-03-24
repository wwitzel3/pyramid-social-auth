from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

import pyramid_social_auth as psa
from social.backends import (
    google,
    facebook,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    psa.register_provider(settings, google.GoogleOAuth2)
    psa.register_provider(settings, facebook.FacebookOAuth2)
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('login', '/login')
    config.include(psa, route_prefix='/social')

    config.scan()
    return config.make_wsgi_app()
