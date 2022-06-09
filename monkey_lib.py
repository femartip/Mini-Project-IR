#!/usr/bin/env python
#! -*- encoding: utf8 -*-
# 3.- Mono Library

import pickle
import random
import re
import sys
import collections


def sort_index(d):
    for k in d:
        l = sorted(((y, x) for x, y in d[k][1].items()), reverse=True)
        d[k] = (sum(x for x, _ in l), l)
        
    


class Monkey():

    def __init__(self):
        self.r1 = re.compile('[.;?!]')
        self.r2 = re.compile('\W+')


    def index_sentence(self, sentence, tri):
        sentence = '$ ' + sentence + ' $'     
        bigrams = [b for b in zip(sentence.split(" ")[:-1], sentence.split(" ")[1:])]  #Obtienes bigramas palabras       
        return dict(collections.Counter(bigrams))


    def compute_index(self, filename, tri):
        self.index = {'name': filename, "bi": {}}
        if tri:
            self.index["tri"] = {}
        fh = open(filename, 'r')
        lines_split = fh.read().splitlines()        #Dividir fichero  en lineas 
        for l in lines_split:                       #Para cada linea
            sentences = re.split(self.r1, l)            #Divides las lineas en las frases que contiene
            sentences = list(filter(lambda a: a != '', sentences))      #Eliminas de la lista de frases la cadena vacia
            for s in sentences:                 #Para cada frase
                s = re.sub(self.r2, ' ', s)         #Eliminas elemnetos no alfanumericos
                bigrams = self.index_sentence(s.lower(), tri)       #Obtienes los bigramas
                for b in bigrams:               #Para cada bigrama
                    if b[0] not in self.index['bi']:        #Si la palabra no ha salido ya 
                        self.index['bi'][b[0]] = (1, {b[1] : 1})    #Se añade la palabra, con su bigrama correspondiente
                    else:
                        ctr = self.index['bi'].get(b[0])        #Si la palabra ya ha salido, nos guardamos el valor de su coorespondiente llave
                        counter = list(ctr)                     #Hacemos un cast del valor para poder interactuar con el, ya que si no sera una tupla
                        if b[1] not in counter[1]:          #Si el bigrama de la palabra que estamos mirando no aparece en su diccionario 
                            counter[0] = counter[0] + 1     #Aumentamos contador de nº de bigramas  
                            self.index['bi'][b[0]] = (counter[0], counter[1] | {b[1] : 1} )     #Añadimos al diccionario de palabras el bigrama
                        else:
                            counter[0] = counter[0] + 1         #Aumentamos contador de nº de bigramas
                            counter[1][b[1]] = counter[1].get(b[1]) + 1         #Ya que el bigrama ya aparecia en el diccionario de bigramas asociado a la palabra, solo habra que incrementar el contador
                            self.index['bi'][b[0]] = (counter[0], counter[1])       #Actualizamos con las modificaciones hechas
        
        sort_index(self.index['bi'])
        if tri:
            sort_index(self.index['tri'])
        

    def load_index(self, filename):
        with open(filename, "rb") as fh:
            self.index = pickle.load(fh)


    def save_index(self, filename):
        with open(filename, "wb") as fh:
            pickle.dump(self.index, fh)


    def save_info(self, filename):
        with open(filename, "w") as fh:
            print("#" * 20, file=fh)
            print("#" + "INFO".center(18) + "#", file=fh)
            print("#" * 20, file=fh)
            print("filename: '%s'\n" % self.index['name'], file=fh)
            print("#" * 20, file=fh)
            print("#" + "BIGRAMS".center(18) + "#", file=fh)
            print("#" * 20, file=fh)
            for word in sorted(self.index['bi'].keys()):
                wl = self.index['bi'][word]
                print("%s\t=>\t%d\t=>\t%s" % (word, wl[0], ' '.join(["%s:%s" % (x[1], x[0]) for x in wl[1]])), file=fh)
            if 'tri' in self.index:
                print(file=fh)
                print("#" * 20, file=fh)
                print("#" + "TRIGRAMS".center(18) + "#", file=fh)
                print("#" * 20, file=fh)
                for word in sorted(self.index['tri'].keys()):
                    wl = self.index['tri'][word]
                    print("%s\t=>\t%d\t=>\t%s" % (word, wl[0], ' '.join(["%s:%s" % (x[1], x[0]) for x in wl[1]])), file=fh)


    def generate_sentences(self, n=10):
        frases_random = ''
        for i in range(0,n):        #Para cada frase que se quiere generar
            rand_num = random.randint(2, 25)    #Instanciamos un numero aleatorio de palabras
            frase = [''] * rand_num         #Creamos una lista de cadena vacia de longitud el numero de palabras 
            frase[0] = '$'              #Primer elemento de la frase
            for j in range(1,rand_num):         #Para cada palabra de la frase
                w = (self.index['bi'][frase[j-1]][1])       #Obtenemos lista de tuplas asociadas a esa palabra
                length = len(w)         #Longitud de la tupla
                nums = []               #Variable para guardar los pesos de cada palabra asociada
                words = []              #Variable para guardar las palabra asociada
                for k in range(0,length): nums.append(w[k][0]); words.append(w[k][1])       #Bucle que recorre las tuplas y guarda pesos/palabras 
                rc = random.choices(words, weights=nums,k=1)        #Obtiene una palabra aleatoria ponderada segun la frequencia con la que sale(peso)
                frase[j] = rc[0]                #Añades la palabra aleatoria a la frase
                if frase[j] == '$': frase = frase[:j];break         #Si la palabra aleatoria es un fin de frase, esta se acaba
            frases_random += ' '.join(map(str,frase[1:])) + '\n'        #Unes la frase a la lista de frases
        return frases_random
        



if __name__ == "__main__":
    print("Este fichero es una librería, no se puede ejecutar directamente")


