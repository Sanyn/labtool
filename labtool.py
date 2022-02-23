def formatFloat(number,decimals):
    mString=str(number)
    rString="$"
    if mString.find("e")!=-1:
        rString+=mString[:mString.find(".")]
        eNum=int(mString[mString.find("e")+1:])
        if decimals>0:
            if(eNum>0):
                rString+=mString[mString.find("."):mString.find(".")+1+decimals]
            else:
                if(decimals+eNum>0):
                    rString+=mString[mString.find("."):mString.find(".")+1+(decimals+eNum)]
        rString+="\\times 10^{"+str(eNum)+"}"
    elif mString.find(".")!=-1:
        mString+="000000000000000000000000000000000000000000000000000"
        rString+=mString[:mString.find(".")+1+decimals]
    else:
        rString+=mString
    rString+="$"
    return(rString)

def LatexTablazat(fejlec,adatok,tizedesjegy=-1,igazitas="c"):
    fixDecimals=False
    listDecimals=False
    listAlignment=False
    if type(fejlec)!=list:
        raise Exception("Fejlécnek nem egy listát adtál meg, hanem egy "+str(type(fejlec))+"-t!")
    if type(adatok)!=list:
        raise Exception("Adatoknak nem egy listát adtál meg, hanem egy "+str(type(adatok))+"-t!")
    columns=len(fejlec)
    if(columns==0):
        raise Exception("Nincs egy fejléc se megadva!")
    if type(tizedesjegy)==int:
        if(tizedesjegy!=-1):
            if(tizedesjegy>=0):
                fixDecimals=True
            else:
                raise Exception("A negatív tizedesjegy mennyiség nincs implementálva, és valószínüleg nem is lesz mert túl sok szenvedés")
    elif type(tizedesjegy)==list:
        fixDecimals=True
        listDecimals=True
        if len(tizedesjegy)!=columns:
            raise Exception("Nem ugyanannyi oszlop van mint tizedesjegy adat a listában. "+str(columns)+" oszlop van, és "+str(len(tizedesjegy))+" tizedesjegy érték")
        for i in range(len(tizedesjegy)):
            if(type(tizedesjegy[i])!=int):
                raise Exception("Az "+str(i)+". eleme a tizedesjegyeknek nem szám, hanem"+str(type(tizedesjegy[i])))
            elif(tizedesjegy[i]<0):
                raise Exception("A negatív tizedesjegy mennyiség nincs implementálva, és valószínüleg nem is lesz mert túl sok szenvedés")
    else:
        raise Exception("A tizedesjegyek nem egy int vagy egy list, hanem"+str(type(tizedesjegy)))
    if type(igazitas)==list:
        listAlignment=True
        if len(igazitas)!=columns:
            raise Exception("Nem ugyanannyi oszlop van mint igazítás adat a listában. "+str(columns)+" oszlop van, és "+str(len(igazitas))+" igazítás adat")
        for i in range(len(igazitas)):
            if(type(igazitas[i])!=str):
                raise Exception("Az "+str(i)+". eleme az igazítás listának nem string, hanem"+str(type(igazitas[i])))
    elif type(igazitas)!=str:
        raise Exception("Az igazítás nem egy str vagy egy list, hanem"+str(type(igazitas))) 
    if(columns!=len(adatok)):
            raise Exception("Nem ugyanannyi fejléc van mint adatsor."+str(columns)+"  fejléc ban, és "+str(len(adatok))+" adatoszlop")
    try:
        rows=len(adatok[0])
    except TypeError:
        raise Exception("Az első adatsorod nem egy lista, hanem egy "+str(type(adatok[0])))
    for i in range(columns):
        try:
            if len(adatok[i])!=rows:
                raise Exception("Nem mindegyik adatsor ugyan olyan hosszú")
        except TypeError:
            raise Exception("A "+str(i)+". adatsorod nem egy list, hanem egy"+str(type(adatok[i])))

    returnString="\\begin{center}\r\n\\begin{tabular}{|"
    if listAlignment:
        for i in range(columns):
            returnString+=igazitas[i]+"|"
    else:
        for i in range(columns):
            returnString+=igazitas+"|"
    returnString+="}\r\n\\hline\r\n"
    for i in range(columns):
        if type(fejlec[i])!=str:
            raise Exception("A fejléc "+str[i]+". eleme nem string, hanem "+str(type(fejlec[i])))
        returnString+=fejlec[i]
        if i<columns-1:
            returnString+="&"
    returnString+="\\\\\r\n\\hline\r\n"
    for i in range(rows):
        for j in range(columns):
            if fixDecimals:
                if listDecimals:
                    if tizedesjegy[j]!=-1:
                        returnString+=formatFloat(adatok[j][i],tizedesjegy[j])
                    else:
                        returnString+="$"+str(adatok[j][i])+"$"
                else:
                    returnString+=formatFloat(adatok[j][i],tizedesjegy)
            else:
                returnString+="$"+str(adatok[j][i])+"$"
            if j<columns-1:
                returnString+="&"
        returnString+="\\\\\r\n\\hline\r\n"
    returnString+="\end{tabular}\r\n\end{center}"
    return returnString

print(LatexTablazat(["aa"],[[]]))