from pico_epaper import EPD_2in13_B_V4
from microbmp import MicroBMP

if __name__=='__main__':
    img_obj = MicroBMP().load("qrcode.bmp")
    print(img_obj)
    epd = EPD_2in13_B_V4()
    epd.Clear(0xff, 0xff)
    epd.imageblack.fill(0xff)
    epd.imagered.fill(0xff)
    
    item = 0
    for b in img_obj.parray:
        #print(b)
        #epd.delay_ms(100)
        row = int(item / (img_obj.DIB_h))
        column = img_obj.DIB_w - int(item % (img_obj.DIB_w))
        #print(f"{item} - {row} - {column} - {b}")
        #epd.delay_ms(100)
        epd.imageblack.pixel(row, column, b)
        item = item + 1
            
    img_obj = MicroBMP().load("bitmap.bmp")
    print(img_obj)
    item = 0
    for b in img_obj.parray:
        #print(b)
        #epd.delay_ms(100)
        row = int(item / (img_obj.DIB_h))
        column = img_obj.DIB_w - int(item % (img_obj.DIB_w))
        #print(f"{item} - {row} - {column} - {b}")
        #epd.delay_ms(100)
        epd.imagered.pixel(row, column + 124, b)
        item = item + 1
    
    epd.display()
    
    epd.sleep()