# Questão 2 (Tradutor de Linguagem)

# Abrir o arquivo para leitura | Arquivo de entrada
arq = open("verb_in.txt", "r")

#Lendo o arquivo
palavras = (arq.read().lower()).split('\n')

# Declarando uma tupla
vogal = ('a','e', 'i', 'o', 'u')

# A função recebe uma palavra
# A função retorna -> palavra - verbo - sufixo
def verbos(p):
  cont = 0

  #lendo cada letra da palavra de trás para frente 
  for i in range(len(p[::-1])):

    #Se encontrar uma vogal
    if p[::-1][i] in vogal:
      cont += 1

    #Se encontrar uma consoante 
    else :
      # começou com vogal  
      if cont == 1:
        chave = p[::-1][:i]
        verbo = p[::-1].replace(p[::-1][:i], 'ne')
        lista = [p, verbo[::-1], chave[::-1] ]
        return lista

      # começou com consoante 
      if cont == 0 :
        cont+=2

      # encontrou consoante
      else:
        chave = p[::-1][:i]
        verbo = p[::-1].replace(p[::-1][:i], 'ne')
        lista = [p, verbo[::-1], chave[::-1] ]
        return lista
       
#chamando a função verbos
lista_verbos = list(map(verbos, palavras))

lista = [{'os': 'casen'}, {'e': 'porren'}, {'aem': 'carren'}]
present = {'o':'1st', 'os':'2nd', 'a':'3rd', 'om':'4th', 'ons':'5th', 'am':'6th'}
past = {'ei':'1st', 'es':'2nd', 'e':'3rd', 'em':'4th', 'est':'5th', 'im':'6th'}
future = {'ai':'1st', 'ais':'2nd', 'i':'3rd', 'aem':'4th', 'aist':'5th', 'aim':'6th'}

def tense_person(lista):  
  palavra = lista[0]
  verbo = lista[1]

  #tense and person
  if lista[2] in present:
    tense =  'present'
    person = present[lista[2]]
  elif lista[2] in past:
    tense =  'past'
    person = past[lista[2]]

  elif lista[2] in future:
    tense =  'future'
    person = future[lista[2]] 

  else :
    return f'{palavra} - not a verb case\n'

  return f'{palavra} - verb {verbo}, {tense} tense, {person} person\n'

#Abrindo o arquivo para gravação 
arq_out = open("verb_out.txt", "w")

for i in lista_verbos:
  arq_out.write(tense_person(i))