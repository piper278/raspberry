from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
from PIL import ImageFont

__version__ = 1.0
serial = i2c(port=1, address=0x3C)# 初始化端口
device = ssd1306(serial)
print("当前版本：", __version__)
font = ImageFont.truetype('./msyh.ttc', 12)
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((20, 10), "23401180202,", fill="white")
    draw.text((20, 25), "董琰喜欢树莓派！", fill="white", font=font)

sleep(10)