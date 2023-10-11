def main():
    print('=' * 25)
    print('Operasi Matematika')
    print('1. Jumlah \t [+]')
    print('2. Kurang \t [-]')
    print('3. Kali \t [*]')
    print('4. Bagi \t [/]')
    print('=' * 25)
    hitung()

def hitung(operasi, a, b):
    if operasi == '1':
        hasil = a + b
        return f'Hasil operasi dari {a} + {b} = {hasil}'
    elif operasi == '2':
        hasil = a - b
        return f'Hasil operasi dari {a} - {b} = {hasil}'
    elif operasi == '3':
        hasil = a * b
        return f'Hasil operasi dari {a} * {b} = {hasil}'
    elif operasi == '4':
        hasil = a / b
        return f'Hasil operasi dari {a} / {b} = {hasil}'
    else:
        return 'Tidak Valid'

if __name__ == '__main__':
    main()