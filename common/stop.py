import requests

# devices1 = ['A007', 'A008', 'A001', 'A002']
def stop_device(devices):
    for i in devices:
        stop_url = R'http://47.93.41.147:9092/api/client/close?deviceId=' + i
        try:
            req = requests.get(url=stop_url, verify=False)
            print(req.status_code)
            print(req.text)
        except Exception as e:
            print(e)
            break

# stop_device(devices1)