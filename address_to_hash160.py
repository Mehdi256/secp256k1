#cat alladdress.txt | python3 address_to_hash160.py > alladdress160.txt
import sys
from bit.base58 import b58decode_check
from bit.utils import bytes_to_hex

def address_to_hash160(address):
    address_bytes = b58decode_check(address)
    address_hash160 = bytes_to_hex(address_bytes)[2:]

    return address_hash160

for line in sys.stdin:
    print (address_to_hash160(line.rstrip()))