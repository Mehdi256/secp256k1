'''
Made by Mizogg Look for HASH160 Compressed and Uncompressed Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting HASH160randomCPU.py Version 1 scan randomly  in Range with CPU Speed Improvments

https://mizogg.co.uk

'''
import secp256k1 as ice
import time, multiprocessing, random
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
from time import sleep

def hunt(start, stop, h160, cores='all'):

    try:
        available_cores = cpu_count()
    
        if cores == 'all':
            cores = available_cores
        elif 0 < int(cores) <= available_cores:
            cores = int(cores)
        else:
            cores = 1
    
        counter = Value('L')
        match = Event()
        queue = Queue()
    
        workers = []
        for r in range(cores):
            p = Process(target=main, args=(counter, start, stop, h160))
            workers.append(p)
            p.start()
    
        for worker in workers:
            worker.join()
    
    except(KeyboardInterrupt, SystemExit):
        exit('\nCTRL-C detected. Exiting gracefully. Thank you and Happy Hunting')


def main(counter, start, stop, h160):
    count = 0
    st = time.time()
    sleep(0.00001)
    while True:
        with counter.get_lock():
            counter.value += 1
        speed = round(counter.value/(time.time() - st))
        count += 1
        ran=random.randrange(start,stop)
        HEX = "%064x" % ran        
        hash160 = ice.privatekey_to_h160(0, True, ran).hex()
        hash160u = ice.privatekey_to_h160(0, False, ran).hex()

        if hash160 in h160 or hash160u in h160:
            print('\nMatch Found ', '\nHASH160 compressed : ', hash160, '\nHASH160 Uncompressed : ', hash160u, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(ran))
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nMatching HASH160 Compressed Found   : ' + hash160)
            f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u)
            f.close()
        else:
            print(hash160, ' : Keys/s : ', str(speed), end='\r')
            #print('\nHASH160 Uncompressed : ', hash160u, '\nHASH160 Compressed : ', hash160, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX)


if __name__ == '__main__':
    print('[+] Starting.........Please Wait.....HASH160 List Loading.....')
    filename ='h160.txt'
    with open(filename) as f:
        line_count = 0
        for line in f:
            line != "\n"
            line_count += 1
    with open(filename) as file:
        h160 = file.read().split()
    h160 = set(h160)
    print('Total HASH160 Loaded and Checking : ',str (line_count))
    howmany=int(input("Number of Cores CPU -> "))   
    start=1
    stop= 10000000000
    print("Starting search... Please Wait min range: " + str(start))
    print("Max range: " + str(stop))
    print("==========================================================")
    print('Total HASH160 Loaded and Checking : ',str (line_count))
    hunt(start, stop, h160, cores = howmany)
