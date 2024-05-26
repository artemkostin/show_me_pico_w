from e_ink import EPD_2in13_B_V4

if __name__=='__main__':
    epd = EPD_2in13_B_V4()
    epd.Clear(0xff, 0xff)
    
    epd.imageblack.fill(0xff)
    epd.imagered.fill(0xff)
    
    epd.sleep()