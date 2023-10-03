from Muse_Reader_Assets import Reader

Muse_Device = Reader.Muse()

try:
    while True:
        alpha, beta, theta, delta = Muse_Device.process()
        print(beta)
        
        

       
        
except KeyboardInterrupt:
        print('Closing!')