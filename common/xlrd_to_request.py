from common import xlrd_handle
import requests
import time
import datetime
import random



def start_all_device(devices):
        # 开启表格所有硬件设备
    for i in devices:
        start_url = R'http://47.93.41.147:9092/api/client/start?deviceId='+i
        try:
            req = requests.get(url=start_url, verify=False)
            print(req.status_code)
            print(req.text)
        except Exception as e:
            print(e)
            break


def set_device_data(devices_data):
    for i in range(len(devices_data[0]["data"])):
        for j in devices_data:
            try:
                set_url = R'http://47.93.41.147:9092/api/client/setData?deviceId='+str(j["deviceId"])+\
                          '&TVOC='+str(j["data"][i][0])+'&PM25='+str(j["data"][i][1])+'&CO2='+str(j["data"][i][2])+\
                          '&formaldehyde='+str(j["data"][i][3])+'&temperature='+str(j["data"][i][4])+'&humidity='+str(j["data"][i][5])
                req = requests.get(url=set_url, verify=False)
                print(req.status_code)
                print(req.text)
            except Exception as e:
                print(e)
                break

        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(60)

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

if __name__ == '__main__':
    file_path = R'C:\Users\Administrator\Desktop\3.0\device-duanxin.xlsx'
    device_list = xlrd_handle.workbook_sheet(file_path)
    all_data = xlrd_handle.workbook_data(file_path)
    start_all_device(device_list)
    print('----------------------------------------------')
    # time.sleep(3)
    set_device_data(all_data)
