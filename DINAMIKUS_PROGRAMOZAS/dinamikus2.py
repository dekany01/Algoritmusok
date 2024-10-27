def legoBlocks (n,m):

    MOD = 10**9 + 7  # modulo 10^9+7 -ben kell majd megadnunk az értékeket, ezért létrehozzuk ezt a változót, hogy később egyszerűbben lehessen rá hivatkozni

    base = [0] * (m + 1) # létrehozunk egy m + 1 nagyságú listát, amiben eltároljuk az 1 magasságú (és 0-tól 'm'-ig szélességű) Lego falakat 
  
    # Alapesetek:
    #   Az 1 magasságú falaknál (="alapfalaknál") megnézzük, hány féle képpen lehet falat építeni.
    #   Mivel 4 féle Lego elemünk van, ezért 4 db alapesetet különböztetünk meg.

    base[1] = 1 # 1 szélességű alapfalat 1 féleképpen lehet építeni

    if m > 1: #1-is lehet 'm' értéke, ezért feltételhez szabjuk a 2. alapesetet, nehogy túlindexeljük a listát, ugyanezt megtesszük a többi fennmaradó alapesetnél

        base[2] = 2 # 2 szélességű alapfalat 2 féleképpen lehet építeni ( 1+1 / 2 )

    if m > 2:

        base[3] = 4 # 3 szélességű alapfalat 4 féleképpen lehet építeni ( 1+1+1 / 1+2 / 2+1 / 3 )
    if m > 3:

        base[4] = 8 # 4 szélességű alapfalat 8 féleképpen lehet építeni ( 1+1+1+1 / 1+1+2 / 1+2+1/ 2+1+1 / 1+3 / 3+1 / 2+2 / 4 )

    # Ha az alapfal 4-nél nagyobb szélességű:
    
    if m > 4:
        for i in range(5, m+1): # 5.indexű elemtől az '(m + 1)'-dik indexig (m szélességig) végig iteráljuk, hogy mennyi  féleképpen lehet megépíteni az adott index szélességű falat
          
            base[i] = (base[i-1] + base [i-2] + base[i-3] + base [i-4]) % MOD # A megadott modulo 10^9+7 szerinti értéket adjuk meg

    # A végén kapunk egy 'm+1' elemű 'base' listát, aminek adott indexű eleme megadja, hogy az adott index szélességű és 1 magasságú falat hány féleképpen lehet megépíteni

  
    if n == 1: # Ha csak 1 magasságú a fal, akkor a függvény visszadja a base tömb adott elemét és kész is vagyunk 
        return base[m] 

    # Ha 1-nél nagyobb a magasság, akkor létrehozunk egy 'total' listát, ami eltárolja, hogy az 'n' magasságú és adott index szélességű falat hányféleképpen lehet megépíteni kötöttségek nélkül:
    # Miután a későbbiekben ezeket az értékeket többször felhasználjuk, ezért tároljuk el egy külön listában.
  
    total = [0] * (m + 1) # Létrehoz egy ugyanakkora listát
    for i in range(m + 1): # Majd feltölti a tömböt az alábbiak szerint

        total[i] = ((base[i]**n) % MOD)  # Az adott tömbelem mindig akkora, mint az adott szélességű alapfalnak az 'n.' hatványa 
      
        # (pl. 2 magasságú 3 szélességű falnál az összes eset = 4^2 , mert 1 magasságú 3 szélességű falat '4' féleképpen lehet építeni, 2 magasságúnál ezt az értéket még egyszer önmagával szorozva kapjuk az összes lehetőséget (4*4))
    
  
    # A végén kapunk egy 'm+1' elemű 'total' listát, aminek adott indexű eleme megadja, hogy az adott index szélességű és 'n' magasságú falat hány féleképpen lehet megépíteni.


    # Ezek után megnézzük, hogy mennyi a jó esetek száma az 'n' magasságú (0-tól m-ig szélességű) falaknál (összes eset - rossz esetek száma):

    solid = [0] * (m + 1) # Létrehozunk még egy ugyanakkora listát
                          # Ez tartalmazza majd, hogy az adott szélességű falat rögzített 'n' esetén hány féleképpen lehet építeni úgy, hogy az "solid" vagy tömör legyen, vagyis ne tartalmazzon egybefüggő vertikális vonalat (ne lehessen további "solid" falakra bontani)
    
    solid[1] = 1 # 1 szélességű falat legyen az akármilyen magas, továbbra is csak 1 féleképpen lehet építeni (nem bontható további falakra)

    for i in range(2, m + 1): # Kettő vagy annál szélesebb falaknak nézzük meg az összesrossz esetet.

        bad_cases = 0    # Változó, ami az összes rossz esetet eltárolja adott szélességnél
                         # Rossz eset = ha a fal legalább egy köztes függőleges vonalat tartalmaz
      
        for j in range (1,i): # Adott szélességű fal balról nézve mindig további 'adott szélesség - 1' db falakra bontható.
                              # Pl. 4 szélességű fal 1, 2 és 3 szélességű falakat tartalmaz

            bad_cases += (solid[j]*total[i-j]) % MOD  # Rossz eseteket úgy számolja ki, hogy veszi az adott szélességű falnál (1-nél nagyobb vagy egyenlő) kisebb számot (a fenti példa szerint mondjuk először az 1 szélességűt),
                                                      # majd beszorozza a fennmaradó terület összes építési lehetőségével (a fenti példa szerint a total[3]-mal, vagyis a 3 szélességű fal összes építési lehetőségével)
                                                      # Így megadja, hogy ha van 1 függőleges vonal az adott szélességnél, akkor mennyi abban az esetben az összes rossz eset (ha már adott szélességnél van 1 függőleges vonal, akkor már mindegy, hány további függőleges vonal van a teljes falban)
                                                      # Az adott szélességnél kapott rossz esetek számát hozzáadja a 'bad_cases' változóban tárolt értékhez.
      
        solid[i] = (total[i] - bad_cases) % MOD 
      
    # A végén kapunk egy 'm+1' elemű 'solid' listát, aminek adott indexű eleme megadja, hogy az adott index szélességű és 'n' magasságú falat hány féleképpen lehet jól ("tömören") megépíteni.
  
    return solid[m] # Ha tehát 'n' nagyobb, mint 1, akkor a függvény visszaadja a fentiek szerint meghatározott 'solid' lista 'm'.indexű elemét
