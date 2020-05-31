import urllib.parse
import http.client
import json

def main():
    host = '106.ihuiyi.com'
    smsSendURI = '/webservice/sms.php?method=Submit'
    params = urllib.parse.urlencode({'account':'wzp', 'password':'123',
                                     'content':'验证码是124885', 'mobile':'13042580978', 'format':'json'})
    print(params)
    # 这个估计是在https协议里面指定了content-type
    headers = {'content-type':'application/x-www-form-urlencoded', 'Accept':'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', smsSendURI, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()

if __name__ == '__main__':
    main()