import aes

key = aes.hexToBytes('140b41b22a29beb4061bda66b6747e14')
IV = aes.hexToBytes('4ca00ff4c898d61e1edbf1800618fb28')

if __name__ == '__main__':

    print("AES encryption/decryption !!!")
    print("Input buffer from file \"input.txt\"")
    print("Output buffer to file \"output.txt\"")

    mode = input("Encrypt or Decrypt? (e/d): ")
    operation = input('CBC or CRT? (c/r): ')

    input = open('input.txt', 'rb')
    buffer = input.read()
    input.close()

    if not buffer:
        print('No input file found')
        exit(1)
 
    if mode == 'e' and operation== 'c':
        buffer = aes.encryptCBC(key, buffer, IV)
    elif mode == 'd' and operation == 'c':
        buffer = aes.decryptCBC(key, buffer, IV)
    elif mode == 'e' and operation == 'r':
        buffer = aes.encryptCTR(key, buffer, IV)
    elif mode == 'd' and operation == 'r':
        buffer = aes.decryptCTR(key, buffer, IV)
    else:
        print('Invalid input')
        exit(1)

    output = open('output.txt', 'wb')
    output.write(buffer)
    output.close()
