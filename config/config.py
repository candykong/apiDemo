import  enum

class URLconf(enum.Enum):

    url_mapping={
        'dev':'http://10.4.190.31:8081/'
    }

    login_uri=r'/fins-console-sso/user/login'