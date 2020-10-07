import ifdh
import os

ih = None

def get_creds(args={}):
    """ get credentials -- Note this does not currently push to
        myproxy, nor does it yet deal with tokens, but those should
        be done here as needed.
    """
    global ih
    if not ih:
        ih = ifdh.ifdh()
    p = ih.getProxy()
    #t = ih.getToken()
    t = None
    os.environ['X509_USER_PROXY'] = p
    return p,t
