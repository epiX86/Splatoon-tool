import gc
import board
import digitalio
import time
import busio

#up down left right
bt_up = digitalio.DigitalInOut(board.D5)
bt_up.direction = digitalio.Direction.OUTPUT
bt_down = digitalio.DigitalInOut(board.D6)
bt_down.direction = digitalio.Direction.OUTPUT
bt_left = digitalio.DigitalInOut(board.D7)
bt_left.direction = digitalio.Direction.OUTPUT
bt_right = digitalio.DigitalInOut(board.D8)
bt_right.direction = digitalio.Direction.OUTPUT
#key A
bt_a = digitalio.DigitalInOut(board.D9)
bt_a.direction = digitalio.Direction.OUTPUT

bt_up.value = True
bt_down.value = True
bt_left.value = True
bt_right.value = True
bt_a.value = True

buttonrun = digitalio.DigitalInOut(board.D16)
buttonrun.switch_to_input(pull=digitalio.Pull.UP)


print("loadding logo . bmp")
fr = open('logo.bmp', 'rb')
#print(fr.read())
bmpfile=list(fr.read())
fr.close()
print("Free RAM ="+str(gc.mem_free()))

head2byte=bmpfile[0:2]
print("head2byte ="+str(head2byte))
bmpsize=(bmpfile[5]<<24)|(bmpfile[4]<<16)|(bmpfile[3]<<8)|bmpfile[2]
print("bmp size ="+str(bmpsize))

witgh_pix=(bmpfile[21]<<24)|(bmpfile[20]<<16)|(bmpfile[19]<<8)|bmpfile[18]
hight_pix=(bmpfile[25]<<24)|(bmpfile[24]<<16)|(bmpfile[23]<<8)|bmpfile[22]
print("bmp  HxW pix is =  "+str(witgh_pix)+"x"+str(hight_pix))

print("first byte is  =  "+('%#x'%(bmpfile[62])))

time.sleep(1)
all_pix_number=320*120
byte_number=all_pix_number/8
y=0
x=0
offset=62

#wait the run key
counter_wait=0
while True:

    if buttonrun.value:
        counter_wait=counter_wait+1
    else:
        time.sleep(0.1)
        if buttonrun.value==False :
            break
    time.sleep(0.1)
    if counter_wait>20 :
        counter_wait=0
        print("waiting for run kesy.......")
print(".......")
print("run ")
print(".......21")



###############################################################go
for y in range(120):
    if (y%2)==0:
        #
        print_data=bmpfile[offset:(offset+40)]
        for x in range(40):
            for z in range (8):
                if ((print_data[x] & 0x80 ) ==00 ):
                    bt_a.value=False
                    time.sleep(0.1)
                    bt_a.value=True
                    time.sleep(0.1)
                    bt_right.value=False
                    time.sleep(0.1)
                    bt_right.value=True
                    time.sleep(0.1)
                #pass A
                #delay
                #pass right
                else :
                    #pass right
                    bt_right.value=False
                    time.sleep(0.1)
                    bt_right.value=True
                    time.sleep(0.1)
                print_data[x]=print_data[x]<<1
        offset=offset+40

    else:
        print_data=bmpfile[offset:(offset+40)]
        print_data.reverse()
        for x in range(40):
            for z in range (8):
                if ((print_data[x] & 0x01 ) ==0 ):
                    bt_a.value=False
                    time.sleep(0.1)
                    bt_a.value=True
                    time.sleep(0.1)
                    bt_left.value=False
                    time.sleep(0.1)
                    bt_left.value=True
                    time.sleep(0.1)
                #pass A
                #delay
                #pass right
                else :
                    #pass right
                    bt_left.value=False
                    time.sleep(0.1)
                    bt_left.value=True
                    time.sleep(0.1)
                print_data[x]=print_data[x]>>1
        offset=offset+40


    time.sleep(0.15)
    print("one line  done .....")
    bt_up.value = False
    time.sleep(0.15)
    bt_up.value = True
    time.sleep(0.15)
    #向上走一行.













while True:


    bt_a.value = True
    time.sleep(0.08)
    bt_a.value = False
    time.sleep(0.1)

    bt_left.value = True
    time.sleep(0.08)
    bt_left.value = False
    time.sleep(0.1)




