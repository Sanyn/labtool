A LatexTablazat(fejlec,adatok,tizedesjegy,igazitas) működése:

Mit tud?
Ha már pythonban kezeled az adataidat jegyzőkönyvíráshoz, akkor azokat csak bedobod ebbe a funkcióba,
és visszaad neked egy szöveget amit ha bemásolsz LaTeX-ba akkor kapsz egy táblázatot az adatokból.

Az jó... de miért?
Nem tudom én nagyon utálok adatokat átirogatni kooplexból a latex fileba, úgyhogy
akkor már automatizáljuk.

Hogyan tudod használni?
Ha k8plexen dolgozol, akkor másold be az egész kódot egy cellába, és futtasd le a cellát.
Ha külön dolgozol pythonba, akkor másold be a python fileod mellé a labtool.py file-t,
és be tudod importálni azzal hogy:
from labtool.py import *
Ekkor már csak meg kell hívd a LatexTablazat() funkciót a megfelelő, lentebb magyarázott argumentumokkal.

fejlec argumentum:
Az első argumentumként egy listát tartalmaz, ami annyi stringet tartalmaz ahány oszlopot szeretnél csinálni.
Ezek lesznek a táblázat első sorában fejlécként bent. Obviously ne legyen üres tömb, mert akkor nem lesz egy oszlopod se.
Nyugodtan használhatsz Latex kifejezéseket is.
Ehhez egy annyi tipp, hogy mindenhol ahol \-t használnál latexba, oda \\-t tegyél
Mivel a pythonban a \ egy speciális karakter (pl \n az egy sortörés, ezért a \nu-t úgy érti a python, hogy:
u)

adatok argumentum:
Ide a funkció egy listát tartalmaz, ami tartalmazza az adatlistákat. Kicsit értelmesebben megfogalmazva,
Ha van két adatlistád, pl: M=[1,2,3] és x=[5,10,15], és ezeket szeretnéd te a táblázatba látni, akkor
ide a [M,x] lista kell. Mindenképpen annyi adatlistát kell tartalmaznia, ahány oszlop fejléced van.
Minden adatlistának ugyan olyan hosszúnak kell lennie.
Nincs megcsinálva hogy számnak kell lennie az adatlistában levő adatoknak, de erősen hagyatkozik erre a formázó
funkció. Ha mindenképpen szeretnél nem számot használni, akkor arra az oszlopra a tizedesjegy mindneképp -1 legyen
(lásd lejjebb)

tizedesjegy argumentum:
Ez vagy egy számot, vagy egy listát vár.
Alapból az értéke -1. Ekkor csak stringé alakítja a számokat, és nem foglalkozik semmi mással. Ha ezt akarod, akkor
nem kell megadj semmit.
Ha egy számot kap, akkor minden számot annyi tizedesjegyig fog kiírni, amennyi meg van adva a tizedesjegy-ben.
Kezeli a python álltal normál alakban írt számokat is, kiírja latexban értelmesen. Ha 10 a pozitívadikon van,
akkor tizedesjegy menyiségű tizedesjegyet fog kiírni a pont után. Azonban ha 10 a negatívonadikon van, akkor
úgy adja meg a számot, hogy tizedesjegy pontosságú legyen. (Azaz ha 1.765354e-2 -t iratod 4 tizedesjegy pontosan,
akkor $1.76\times10^{-2}$-vé alakítja). Negatív számokra errort fog dobni. tizedesjegy=0 esetén figyel
arra hogy ne rakjon felesleges pontot
Ha listát adsz meg, akkor oszloponként külön tudod kezelni, hogy hány tizedesjegyre kerekítsen. Ekkor fontos,
hogy a listának olyan hosszúnak kell lennie, amilyen sok sorod van. A lista tartalmazhat -1-et, akkor ugyanúgy mint
sima -1-re az adott sort nem fogja formázni

igazitas argumentum:
Ez vagy egy stringet, vagy egy listát vár
Ha stringet adsz meg, akkor a latex lista létrehozásakor, amikor meg kell adni hogy hova igazítson, ezt fogja bemásolni.
Alapértéke c, ha középre akarsz mindent igazítani, nem kell megadj semmit.
A latex csak az "r" (aka right), a "c" (aka center) és a "l" (aka left) értékeket érti meg (tudtommal),
de nem állítalak meg hogy beírd a saját dolgodat. Csak legyen string.
Ha listát adsz meg, akkor ugyan ez, csak minden oszlopot tudsz egyenként befolyásolni.
Ekkor fontos hogy annyi adat legyen a listában, ahány oszlop lesz.

Ha véletlen észlelsz bármi hibát a programban, akkor szólj és megjavítom.
Onnan ismered meg, hogy nem kezelt hibáról van szó, hogy angol error szövegezt kapsz, és nem magyart.
Ha van bármi ötleted, hogy ezt hogyan lehetne továbbfejleszteni, vagy hogy milyen más labtoolok lennének jók,
akkor is írj nyugodtan.

Legyen szép napod:)
CP

