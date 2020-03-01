#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def main():

    opciones = dict()

    opciones['p'] = "Piedra"
    opciones['a'] = "Papel"
    opciones['t'] = "Tijera"

    opcion = None
    while (not is_valid_option(opcion)):
        if opcion is not None:
            print("Opcion no válida, introduce [p] piedra , [a] papel)  o [t]"
                  "tijera , o bien [q] para terminar")
        opcion = input("Piedra [p], papel[a] o tijera [t]?")
        if opcion == 'q':
            print("Bye!")
            return True
    machine_option = get_machine_option()
    winner = get_winner(machine_option, opcion)

    print("Tu: {}".format(opciones[opcion]))
    print("Ordenador: {}".format(opciones[machine_option]))

    if winner == "human":
        print("Has ganado!!")
    elif winner == "machine":
        print("Has perdido")
    else:
        print("Habeis empatado")


def get_winner(human, machine):

    human_winner = [('p', 't'),
                    ('a', 'p'),
                    ('t', 'a')]

    if human == machine:
        return None
    elif (human, machine) in human_winner:
        return "human"
    return "machine"


def get_machine_option():
    options = ['p', 'a', 't']
    return random.choice(options)


def is_valid_option(opcion):
    if opcion not in ['p', 'a', 't', 'q']:
        return False
    return True


if __name__ == '__main__':
    while exit is not True:
        exit = main()
