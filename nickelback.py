songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

no_nickelback = {song for song in songs if song[0] != "Nickelback"}
print(no_nickelback)
