import codecs
from collections import namedtuple

codec = namedtuple('codec', ('content_type', 'content_encoding', 'encoder'))

class SerializerNotInstalled(Exception):
    pass


class SerializerRegistry(object):
    def __init__(self):
        self._encoders = {}
        self._decoders = {}
        self._default_encode = None
        self._default_content_type = None
        self._default_content_encoding = None

    def register(self, name, encoder, decoder, content_type,
                 content_encoding='utf-8'):
        if encoder:
            self._encoders[name] = codec(
                content_type, content_encoding, encoder,
            )
        if decoder:
            self._decoders[content_type] = decoder

    def _set_default_serializer(self, name):
        try:
            (self._default_content_type, self._default_content_encoding,
             self._default_encode) = self._encoders[name]
        except KeyError:
            raise SerializerNotInstalled(
                'No encoder installed for {0}'.format(name))

    def dumps(self, data, serializer=None):
        if serializer and not self._encoders.get(serializer):
            raise SerializerNotInstalled(
                'No encoder installed for {0}'.format(serializer))

        if not serializer and isinstance(data, unicode):
            payload = data.encode('utf-8')
            return 'text/plain', 'utf-8', payload

        if serializer:
            content_type, content_encoding, encoder = \
                self._encoders[serializer]
        else:
            encoder = self._default_encode
            content_type = self._default_content_type
            content_encoding = self._default_content_encoding

        payload = encoder(data)
        return content_type, content_encoding, payload

    def loads(self, data, content_type, content_encoding):
        content_type = (content_type if content_type
                        else 'application/data')
        content_encoding = (content_encoding or 'utf-8').lower()

        if data:
            decode = self._decoders.get(content_type)
            if decode:
                return decode(data)
        return data


registry = SerializerRegistry()
dumps = registry.dumps
loads = registry.loads
register = registry.register


def register_yaml():
    try:
        import yaml
        registry.register('yaml', yaml.safe_dump, yaml.safe_load,
                          content_type='application/x-yaml',
                          content_encoding='utf-8')
    except ImportError:

        def not_available(*args, **kwargs):
            """Raise SerializerNotInstalled.
            Used in case a client receives a yaml message, but yaml
            isn't installed.
            """
            raise SerializerNotInstalled(
                'No decoder installed for YAML. Install the PyYAML library')
        registry.register('yaml', None, not_available, 'application/x-yaml')


register_yaml()
registry._set_default_serializer('yaml')

yaml_data = """\
float: 3.1415926500000002
int: 10
list: [george, jerry, elaine, cosmo]
string: The quick brown fox jumps over the lazy dog
unicode: "Th\\xE9 quick brown fox jumps over th\\xE9 lazy dog"
"""

content_type, content_encoding, payload = dumps(yaml_data, serializer='yaml')
print content_type, content_encoding

assert loads(payload, content_type=content_type, content_encoding=content_encoding) == yaml_data
