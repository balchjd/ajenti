from ajenti.api import *
from ajenti.com import *


class DebianNetworkCfg(Plugin):
    implements(IConfigurable)
    name = 'Network'
    id = 'network'
    platform = ['Debian', 'Ubuntu', 'gnu/kfreebsd']
    
    def list_files(self):
        dir = '/etc/network/'
        return [dir+'*', dir+'*/*', dir+'*/*/*']
    
