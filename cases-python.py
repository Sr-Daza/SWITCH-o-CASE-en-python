#! /usr/bin/env python

import pexpect
import time

def teleg():
    try:
        global esp
        global tele
        tele = pexpect.spawn('telegram-cli -W -C')
        time.sleep(2)

        tele.sendline('contact_list')
        time.sleep(2)

        print("Prueba")
        esp = tele.expect_exact(["<mensaje>", '<foto>', '<comando>', '<musica>', pexpect.EOF], timeout=10)
        print(esp)
       
        if 0 <= esp < 4:
            return esp

        else:
            tele.sendline('quit')
            print("Sin solicitud de Telegram")
            exit(0)

    except pexpect.TIMEOUT:
        tele.sendline('quit')
        print("Saliendo por TIMEOUT")
        exit(0)


def mensaje():
    return "Mensaje"


def foto():
    return "Fotos"

def comando():
    return "Comando"

def musica():
    return "Musica"

switcher = {
    0: mensaje,
    1: foto,
    2: comando,
    3: musica
}

def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "n")

    return func()


if __name__ == "__main__":
    teleg()
    tele.sendline('quit')

    b = numbers_to_strings(esp)
    print(str(b))
    exit(0)
