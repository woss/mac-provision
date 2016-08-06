import json
import os

# os.environ["PARSE_API_ROOT"] = "http://your_server.com:1337/parse"
#
# # Everything else same as usual
#
# from parse_rest.datatypes import Function, Object, GeoPoint
# from parse_rest.connection import register
# from parse_rest.query import QueryResourceDoesNotExist
# from parse_rest.connection import ParseBatcher
# from parse_rest.core import ResourceRequestBadRequest, ParseError
#
# APPLICATION_ID = '...'
# REST_API_KEY = '...'
# MASTER_KEY = '...'
#
# register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)

node_version = os.popen('node -v').read()
print 'Node version ' + node_version

npms_json_string = os.popen('npm ls --global --depth=0 --json=true').read()
npms = json.loads(npms_json_string)
dependencies = npms['dependencies']

parse_npms = []

for npm in dependencies:

    if npm != 'npm':
        print 'Processing ' + npm
        print 'Processing ' + json.dumps(dependencies[npm])
        _npm = {
            'name': npm,
            'from': dependencies[npm]['from'],
            'resolved': dependencies[npm]['resolved'],
            'version': dependencies[npm]['version'],
            'node_version': node_version,
        }

        parse_npms.append(_npm)
