from PIL import Image, ImageDraw, ImageFont
import board, busio
from adafruit_ssd1306 import SSD1306_I2C

# Initiera OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

# Canvas
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Ladda din egen font med valfri storlek
font = ImageFont.truetype("/home/magopti/fonts/Westminster.ttf", 30)

# Rita text
draw.text((0, 10), "The AI Rev.", font=font, fill=255)
draw.text((0, 40), "v.3.14", font=font, fill=255)
oled.image(image)
oled.show()
