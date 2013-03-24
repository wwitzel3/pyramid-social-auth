<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Auth Page</title>
</head>
<body>

<%def name="form(name, title, **kw)">
% if name in providers:
<form id="${name}" action="${request.route_url('psa.login', provider=name)}" method="post">
    % for k, v in kw.items():
    <input type="hidden" name="${k}" value="${v}" />
    % endfor
    <input type="submit" value="${title}" />
</form>
% else:
<form id="${name}" method="post">
    <input type="submit" value="${title}" disabled="disabled" />
</form>
% endif
</%def>

${form('facebook', 'Login with Facebook')}
${form('github', 'Login with Github')}
${form('twitter', 'Login with Twitter')}
${form('bitbucket', 'Login with Bitbucket')}
${form('google-oauth2', 'Login with Google',
       use_popup='false',
       openid_identifier='google.com')}
${form('yahoo', 'Login with Yahoo',
       oauth='true',
       openid_identifier='yahoo.com')}
${form('live', 'Login with Windows Live')}

</body>
</html>
