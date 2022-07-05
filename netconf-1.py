import warnings
import xml.dom.minidom

warnings.simplefilter("ignore", DeprecationWarning)

from ncclient import manager

m = manager.connect(host='172.17.8.8',
                    port=830, # 830
                    username='admin',
                    password='123',
                    device_params={'name': 'csr'})

netconf_filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
'''

reply = m.get(netconf_filter)
print(reply)

config = xml.dom.minidom.parseString(reply.xml)
print(config.toprettyxml())

