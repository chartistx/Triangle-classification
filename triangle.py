# Funkcijas apraksts

# Funkcija - Trīsstūra veda noteikšana (TVN)

# Funkcija tiek izmantota lietotnē, kura var tikt izmantota zinātniskiem nolūkiem, lai noteiktu trīsstūra veidu.
# Tātad aprēķiniem ir jāspēj strādāt ar decimālskaitļiem un izvadei ir jābūt precīzai arī, kad tiek padotas decimāli 
# ļoti mazas vērtības. 

# Formula pēc kuras nosaka vai trīsstūris ir iespējams 
# a+b>c
# a+c>b
# b+c>a , kur a,b,c ir trīsstūra malu garumi

# Kritēriji, kas nosaka, ka trīsstūris irvienādmalu - visu malu garumi ir vienādi
# Kritēriji, kas nosaka, ka trīsstūris ir vienādsānu - divas malas ir vienāda garuma
# Kritēriji, kas nosaka, ka trīsstūris ir dažādsānu - malas ir dažāda garuma

# Ievade

# a,b,c - trīsstūra malu garumi
# pieņēmums - dati saņemti string formātā

# Izvade

# Gadījumā, kad trīsstūris nav iespējams tiek izvadīts paziņojums "Trīsstūris nav iespējams"
# Gadījumā, kad trīsstūris ir vienādmalu tiek izvadīts paziņojums "Trīsstūris ir vienādmalu"
# Gadījumā, kad trīsstūris ir vienādsānu tiek izvadīts paziņojums "Trīsstūris ir vienādsānu"
# Gadījumā, kad trīsstūris ir dažādsānu tiek izvadīts paziņojums "Trīsstūris ir dažādsānu"



# Funkcijas kods

def triangleType(a,b,c):
    #pārbaude vai trīsstūris ir iespējams
    if (a+b<=c) or (a+c<=b) or (b+c<=a):
        return "Trīsstūris nav iespējams"
    #pārbaude vai trīsstūris ir vienādmalu
    elif a==b and b == c:
        return "Trīsstūris ir vienādmalu"
    #pārbaude vai trīsstūris ir vienādsānu
    elif a==b or a==c or b==c:
        return "Trīsstūris ir vienādsānu"
    else:
        return "Trīsstūris ir dažādmalu"

# funkcija kas nosaka trīsstūra veidu	
def classifyTriangle(a,b,c): # a,b,c ir trīsstūra malu garumi
    try:
        #ievades pārbaude
        #transformācija uz float un pārbaude vai iedadītie dati ir skaitļi
        a=float(a)
        b=float(b) 
        c=float(c)
        #pārbaude vai ievadītie dati ir <=0
        if a <= 0 or b <= 0 or c <= 0:
            return "Trīsstūris nav iespējams"
    except ValueError as error:
        #print(error)
        return "Trīsstūris nav iespējams"
    
    return triangleType(a,b,c)

    


