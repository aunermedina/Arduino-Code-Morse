import serial
from django.shortcuts import render


def index(request):
    return render(request, 'base.html', {})


def encode(request):
    if request.method == 'POST':
        msg_to_encode = request.POST.get('msg', '')

        try:
            serial_connection = serial.Serial("COM3", baudrate=9600, timeout=1)
            print(serial_connection.is_open)
            CODE = {
                # English alphabet
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..',
                # Numbers
                '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                '8': '---..', '9': '----.',
                # Extended
                ' ': '/', '.': '.-.-.-', ',': '--..--', ':': '---...',
                '?': '..--..', "'": '.----.', '-': '-....-', '/': '-..-.',
                '@': '.--.-.', '=': '-...-', '(': '-.--.', ')': '-.--.-',
                '+': '.-.-.'
            }
            encode_msg = ' '.join(CODE.get(char.upper()) for char in msg_to_encode)
            # serial_connection.write(encode_msg.encode())
            serial_connection.write(".-.--.-.-".encode('utf-8'))
            # serial_connection.write('.-.-.-')
            serial_connection.close()
            serial_error = False
        except serial.SerialException:
            serial_error = True
    return render(request, 'base.html', {'serial_error': serial_error})
