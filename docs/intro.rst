Intalling and Usage
=========================

Install
=======

To install just run pip install pyramid-social-Auth

Usage
=====

import pyramid_social_auth as psa

login_url = psa.login_url
providers = request.registry.settings['login_providers']

context =  psa.AuthenticationComplete
           psa.AuthenticationDenied

providers = settings.items('psa.providers')

[psa.providers]
psa.google = True
psa.facebook = False
psa.twitter = True

[psa.google]
consumer_key = 
consumer_secret =

config.add_providers(providers)

