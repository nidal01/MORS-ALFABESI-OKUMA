import machine
import utime

# Pico'nun pinleri
ldr_pin = machine.Pin(27, machine.Pin.IN)  # LDR bağlantısının yapıldığı pin

# Morse alfabesini tanımlama
morse_code = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '/': ' '
}

# Işık seviyesi eşik değeri
light_threshold = 500  # Bu değeri ortam ışığına göre ayarlayabilirsiniz

# Morse kodunu okuma işlevi
def read_morse():
    morse = ''
    while True:
        ldr_value = ldr_pin.value()
        if ldr_value < light_threshold:  # Işık seviyesi eşik değerinden düşükse
            utime.sleep_ms(50)  # Bir boşluk algılandı, bekleme süresi
            ldr_value = ldr_pin.value()
            if ldr_value < light_threshold:  # Hala düşük ışık seviyesi algılandıysa (uzun süre ışıksızlık)
                morse += '-'
            else:
                morse += '.'
        else:  # Işık algılandıysa
            break
    return morse

# Morse kodunu metne çevirme işlevi
def morse_to_text(morse):
    words = morse.split(' ')
    decoded_message = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in morse_code:
                decoded_message += morse_code[letter]
        decoded_message += ' '
    return decoded_message

# Ana döngü
while True:
    morse = read_morse()
    if morse:  # Eğer bir morse kodu algılandıysa
        decoded_text = morse_to_text(morse)
        print("Algılanan Morse Kodu:", morse)
        print("Çevrilen Metin:", decoded_text)
    utime.sleep(1)
