from pyramid.config import Configurator

import pyramid_social_auth as psa
from social.backends import (
    google,
    facebook,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    psa.register_provider(settings, google.GoogleOpenId)
    psa.register_provider(settings, facebook.FacebookOAuth2)

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include(psa, route_prefix='/social')

    config.scan()
    return config.make_wsgi_app()
