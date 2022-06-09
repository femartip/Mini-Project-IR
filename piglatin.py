#!/usr/bin/env python
#! -*- encoding: utf8 -*-


from itertools import count
import sys
import re
import string 

class Translator():

    def __init__(self, punt=None):
        """
        Constructor de la clase Translator

        :param punt(opcional): una cadena con los signos de puntuación
                                que se deben respetar
        :return: el objeto de tipo Translator
        """
        if punt is None:
            punt = ".,;?!"
        self.re = re.compile(r"(\w+)([" + punt + r"]*)")

    def translate_word(self, word):
        """
        Recibe una palabra en inglés y la traduce a Pig Latin

        :param word: la palabra que se debe pasar a Pig Latin
        :return: la palabra traducida
        """
        final_de_linea = False
        if word[-1] == '\n': 
            word = word.replace('\n','') 
            final_de_linea = True
        signos= {'.',',',';','?','!'}
        contiene_signo = False
        for w in word:
            if w in signos:
                #pos = word.index(w)
                signo=w
                word = word.replace(w,'')
                contiene_signo = True
        primera_mayuscula = False
        en_mayusculas = False
        if word.isupper():en_mayusculas = True
        if word[0] in string.ascii_uppercase: primera_mayuscula = True
        vocal = {'a','e','i','o','u','y','A','E','I','O','U','Y'}
        nv = ''
        cont = 0
        if word[0] not in string.ascii_letters:
            new_word = word
        else:
            for w in word:
                if w not in string.ascii_letters:
                    return word
            if word[0] not in vocal:
                for w in word:
                    if w not in vocal:
                        nv = nv + w
                        cont += 1
                    else: 
                        break
                new_word = word[cont:] + nv + 'ay'
            else:
                new_word = word + 'yay'                    
        if primera_mayuscula: new_word = new_word.capitalize()
        if en_mayusculas: new_word = new_word.upper()
        if contiene_signo: new_word = new_word + signo 
        if final_de_linea: new_word = new_word + '\n'
        return new_word
    def translate_sentence(self, sentence):
        """
        Recibe una frase en inglés y la traduce a Pig Latin

        :param sentence: la frase que se debe pasar a Pig Latin
        :return: la frase traducida
        """
        array = sentence.split(' ')
        pl = []
        for a in array:
            pl.append(self.translate_word(a))
        return ' '.join(pl)


    def translate_file(self, filename):
        """
        Recibe un fichero y crea otro con su tradución a Pig Latin

        :param filename: el nombre del fichero que se debe traducir
        :return: True / False 
        """
        f = open(filename,'r', encoding="utf8")
        pl = open(filename[:-4] + '_piglatin.txt', 'w')
        for l in f:
            pl.write(self.translate_sentence(l))
        return True

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f'Syntax: python {sys.argv[0]} [filename]')
        exit()
    t = Translator()
    if len(sys.argv) == 2:
        t.translate_file(sys.argv[1])
    else:
        sentence = input("ENGLISH: ")
        while len(sentence) > 1:
            print("PIG LATIN:", t.translate_sentence(sentence))
            sentence = input("ENGLISH: ")

   