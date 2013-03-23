from social.strategies.base import BaseStrategy
from pyramid.httpexceptions import HTTPFound

class PyramidStrategy(BaseStrategy):

    def redirect(self, url):
        raise HTTPFound(location=url)

    def get_setting(self, name):
        return getattr(self.settings, name)

    def html(self, content):
        pass

    def render_html(self, tpl=None, html=None, context=None):
        pass

    def request_data(self, merge=True):
        if merge:
            merged = self.request.POST
            merged.update(self.request.GET)
            return merged
        elif self.request.method == 'POST':
            return self.request.POST
        else:
            return self.request.GET

    def request_host(self):
        pass

    def session_get(self, name, default=None):
        pass

    def session_set(self, name, value):
        pass

    def session_pop(self, name):
        pass

    def authenticate(self, *args, **kwargs):
        kwargs['strategy'] = self
        kwargs['storage'] = self.storage
        kwargs['backend'] = self.backend
        import pdb; pdb.set_trace()
        return self.backend.authenticate(*args, **kwargs)

    def build_absolute_uri(self, path=None):
        path = path or ''
        if path.startswith('http://') or path.startswith('https://'):
            return path
        if self.request.host_url.endswith('/') and path.startswith('/'):
            path = path[1:]
        return self.request.host_url + (path or '')

    def is_response(self, value):
        pass
