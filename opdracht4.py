getal=25
running=True

while running:
  raden=int(raw_input('Vul een getal in:'))
  if raden==getal:
    print'Mooi, je hebt het geraden'
    running=False
  elif raden <getal:
    print'Nee, iets hoger dan dat.'
  else:
    print'Nee, iets lager dan dat.'
else:
  print'Zo werkt dus de WHILE lus.'
print'Klaar'