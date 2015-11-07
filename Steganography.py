def encrypt(msg,key):
    txt = []
    for i in range(len(msg)):
        txt.append(ord(msg[i])^ord(key[i%len(key)]))
    return txt
def getmessage(filename):
    f = open(filename, 'rb')
    return f.read()
def buildfile(message, filename):
    f = open(filename, 'wb')
    f.write(message)
    f.flush()
def encode(msg, f):
    k = len(f[0,0])
    pos = 0
    for i in msg:
        for j in xrange(7,-1,-1):
            color = pos%k
            x = (pos/k)%img.size[0]
            y = (pos/k)/img.size[0]
            if not ((i >> j) & 1):
                value = []
                for h in range(k):
                    if h == color:
                        value.append((f[x,y][color])& ~1)
                    else:
                        value.append((f[x,y][h]))
                f[(x,y)] = tuple(value)
            else:
                value = []
                for h in range(k):
                    if h == color:
                        value.append((f[x,y][color])|1)
                    else:
                        value.append((f[x,y][h]))
                f[(x,y)] = tuple(value)
            pos += 1
    filename = raw_input('Enter file name to save in:')
    img.save(filename)
def decode(byte, f):
    k = len(f[0,0])
    pos = 0
    currentbyte = ""
    msg = ""
    while (pos < byte*8):
            color = pos%k
            x = (pos/k)%img.size[0]
            y = (pos/k)/img.size[0]
            if not ((f[x,y][color])%2):
                currentbyte += '0'
            else:
                currentbyte += '1'
            pos += 1
            if not (pos%8):
                msg += chr(int(currentbyte, 2))
                currentbyte = ""
    return msg
    
import Image
key = raw_input('Enter Password:')
image = raw_input('Enter image file name:')
img = Image.open(image)
handle = img.load()
while True:
    print "Choose one of the following:\n1.Create Steganographic Data\n2.Read Steganographic Data\n3.Exit\n"
    x = raw_input('Your Choice:')
    if (x == '1'):
        i = raw_input("1. Read from a file\n2. Enter text manually\nYour Choice:")
        if (i == '2'):
            message = raw_input('Enter Message:')
        elif (i == '1'):
            filename = raw_input('Enter data file name:')
            message = getmessage(filename)
        message = encrypt(message, key)
        encode(message, handle)
        print "The size of the message was " + str(len(message)) + " bytes"
    elif (x == '2'):
        pix = int(raw_input('Enter the number of bytes you want to retrieve:'))
        msg = decode(pix, handle)
        result = ""
        for i in encrypt(msg, key):
            result += chr(i)
        msg = result
        del result
        i = raw_input("1. Write to a file\n2. Display on Console\nYour Choice:")
        if (i == '2'):
            print msg
        elif (i == '1'):
            filename = raw_input('Enter file name to write in:')
            buildfile(msg, filename)
    elif (x == '3'):
        break
    else:
        print
        pass
raw_input()
