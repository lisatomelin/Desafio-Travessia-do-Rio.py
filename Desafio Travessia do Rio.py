#Criem listas e variáveis para testar suas condicionais
margemA=['pai','filho1','filho2', 'mae', 'filha1','filha2','guarda', 'prisioneira']
margemB=[]
jangada=[]
qtPA = len(margemA)
qtPB = len(margemB)
qtPJ = len(jangada)

# condicional para avaliar situação na jangada. Está pronta!!!
if (qtPJ == 1 or qtPJ == 2) and ('pai' in jangada or 'mae' in jangada or 'guarda' in jangada) and not('prisioneira' in jangada and 'guarda' not in jangada) and not('mae' in jangada and ('filho1' in jangada or 'filho2' in jangada)) and not('pai' in jangada and ('filha1' in jangada or 'filha2' in jangada)):
  print('Jangada OK')
else:
  print('Problema na jangada')

# condicional para avaliar situação da margem A (quanto aos personagens na margem A)
if not ('mae' in margemA and ('filho1' in margemA or 'filho2' in margemA)) and not ('pai' in margemA and ('filha1' in margemA or 'filha2' in margemA)) and not ('prisioneira' in margemA and 'guarda' not in margemA):
  print("Margem A OK")
else:
  print("Problema na Margem A")
# condicional para avaliar situação da margem B (quanto aos personagens na margem B)
if not ('mae' in margemB and ('filho1' in margemB or 'filho2' in margemB)) and not ('pai' in margemB and ('filha1' in margemB or 'filha2' in margemB)) and not ('prisioneira' in margemB and 'guarda' not in margemB):
    print('Margem B OK')
else:
  print('Problema na Margem B')

# condicional para avaliar situação ao chegar na margem B (quanto ao fim do jogo)
if ('prisioneira' and 'guarda' and 'mae' and 'filho1' and 'filho2' and 'pai' and 'filha1' and 'filha2' in margemB):
  print("Fim do Jogo")
else:
  print("Tente novamente")
