# Solve The Mystery
Pelissä on 3 tasoa jotka voi pelata. Kun on suorittanut pelin kerran kokonaan, voi yrittää aiempia tasoja uudelleen.

Tasot itsessään sisältävät erilaisia vaihtoehtoja, joihin oikeat vastaukset johtavat pelaajaa ansaitsemaan todistusaineistoja. Todistusaineiden määrä vaikuttaa pelin loppuun. Pelissä on mahdollista saada 3 esinettä. 0 - 1: huono loppu, 2: ihan ok loppu, 3: paras loppu pelille. Pelin voi myös hävitä viimeisen tason aikana, jos teet liikaa virheitä. Häviäminen tulostaa huonoimman lopetuksen pelille ja sulkee tiedoston

mainpeli.py itsessään sisältää vain pelin valikon, muutaman funktion tarkistamaan tallenteiden tila. Käyttäjälle voi kirjautua oikean tallenteen numeron kanssa + käyttäjän ikä vaaditaan avaamaan tallenne. Voit myös aloittaa pelin, tarkistaa saamasi esineet, tallentaa tai lopettaa pelin. lopettaessa peli kysyy, jos käyttäjä tahtoo tallentaa pelinsä.

Paketissa on seuraavat moduulit
- esineet.py: Sisältää luokan esineille, joita luon pelin aikana
- hahmo.py: Sisältää käyttäjän Pelaaja luokan, jolla on funktio kerätä esineitä
- ohjeet.txt: Tulostetaan, jos valikossa valitaan "ohjeet" vaihtoehto. Sisältää pienen tekstin pelin aiheesta
- tallenna.py: Sisältää ominaisuuden tallentaa pelin ja luoda uuden käyttäjän
- tasot.py: pääohjelma kutsuu funktioita tasot.py moduulista, jossa pelin kaikki tasot ovat kirjoitettuna. Sisältää myös funktion, joka tarkistaa pelaajan nykyisen taso-arvon ja laittaa hänet oikeaan tasoon. Kun kaikki on suoritettu, voi pelata aiempia tasoja uudelleen¨

Kestävä kehitys on otettu pelissä huomioon ensimmäisessä tasossa ja pelin tarinan päämysteerissä, vesistöjen suojelu
