
import os
import requests


class SettingsClient(object):

    def get_key(self):
        return os.environ.get('SETTINGS_CLOUD_KEY', '')

    def set_key(self, key):
        os.environ['SETTINGS_CLOUD_KEY'] = key

    def get_host(self):
        return os.environ.get('SETTINGS_CLOUD_HOST', 'http://settings.tslow.cn')

    def set_host(self, host):
        if 'http' not in host:
            host = 'http://' + host
        host = host.strip().strip('/')
        os.environ['SETTINGS_CLOUD_HOST'] = host

    def get_script(self, name, key='', host=''):
        key = key or self.get_key()
        host = host or self.get_host()
        url = '%s/settings/?name=%s&key=%s' % (host, name, key)
        try:
            script = requests.get(url).text
            return script
        except Exception as e:
            print('get script from settings cloud failed!')
            print(e)
            return ''

    def set_script(self, name, content, language='', key='', host=''):
        key = key or self.get_key()
        host = host or self.get_host()

        url = '%s/settings/' % host
        data = {
            'name': name,
            'content': content,
            'language': language,
            'key': key,
        }
        r = requests.post(url, data)
        return r.text


if __name__ == '__main__':

    s = SettingsClient()
    s.set_host('http://127.0.0.1:6004/')
    s.set_key('testkey')

    s.set_script('test', 'a=1\nprint(a)', 'python', 'testkey')

    script = s.get_script('test')
    assert 'a=1' in script, script
    exec(script)










