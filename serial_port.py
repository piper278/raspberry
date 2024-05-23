import serial
import time

# 串口初始化
ser = serial.Serial('/dev/ttyUSB', 9600)  # 串口设备文件和波特率//S0(引脚)改为USB

try:   
    while True:
        # 接收信息
        if ser.in_waiting > 0:  # 如果串口接收缓冲区有数据
            received_data = ser.readline().decode('utf-8').strip()  # 读取数据并解码为字符串
            print("Received:", received_data)
        # 发送信息
        message = "Hello from Raspberry Pi!"  # 要发送的信息
        ser.write(message.encode('utf-8'))  # 将字符串编码为字节并发送
        print("Sent:", message)
        time.sleep(1)  

except KeyboardInterrupt:
    print("Exiting...")
ser.close()  
