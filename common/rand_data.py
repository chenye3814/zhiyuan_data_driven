from common import xlrd_handle
import requests
import time
import datetime
import random
from common.xlrd_to_request import start_all_device
from common.stop import stop_device



def rand_set_data(devices,num):
    """循环为设备新增数据"""
    for i in range(0, num):
        for j in devices:
            try:
                set_url = R'http://47.93.41.147:9092/api/client/setData?deviceId=' + str(j) + \
                          '&TVOC=' + str(round(random.uniform(0.001, 1), 3)) + '&PM25=' + str(round(random.uniform(0.001, 100), 3)) + \
                          '&CO2=' + str(round(random.uniform(0.01, 1500), 3)) + '&formaldehyde=' + str(round(random.uniform(0.001, 0.3), 3)) + \
                          '&temperature=' + str(round(random.uniform(-50, 50), 1)) + '&humidity=' + str(round(random.randint(0, 100)))
                req = requests.get(url=set_url, verify=False)
                print(req.status_code)
                print(req.text)
            except Exception as e:
                print(e)
                break
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print('===================================')
        time.sleep(60)

if __name__ == '__main__':
    file_path = R'C:\Users\Administrator\Desktop\3.0\device-D.xlsx'
    device_list = xlrd_handle.workbook_sheet(file_path)
    stop_device(device_list)
    print('----------------------------------------------')
    # start_all_device(device_list)
    print('----------------------------------------------')

    # rand_set_data(device_list, 1000)