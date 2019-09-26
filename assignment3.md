# 1. Wallets

## source code
```
def inputValues():
    walletList = []
    for i in range(5):
        value = float(input('Enter the amount of money: '))
        walletList.append(value)        
    return walletList
        
def printSummary(walletList):
    maxValue = max(walletList)
    minValue = min(walletList)
    sumValues = sum(walletList)
    totalDimes = sumValues*10
    print("The fattest wallet has $"+str(maxValue)+" in it.")
    print("The skinniest wallet has $"+str(minValue)+" in it.")
    print("All together, these wallets have $"+str(sumValues)+" in them.")
    print("All together, the total value of these wallets is worth $"+ str(totalDimes) +" dimes")


walletList = inputValues()
printSummary(walletList)
```

# 2. Periodic Table

## dictionary of elements
elements = {"H":{"row":1,"column":1,"atomic number":1,"name":"Hydrogen"},
"He":{"row":1,"column":18,"atomic number":2,"name":"Helium"},
"Li":{"row":2,"column":1,"atomic number":3,"name":"Lithium"},
"Be":{"row":2,"column":2,"atomic number":4,"name":"Beryllium"},
"B":{"row":2,"column":13,"atomic number":5,"name":"Boron"},
"C":{"row":2,"column":14,"atomic number":6,"name":"Carbon"},
"N":{"row":2,"column":15,"atomic number":7,"name":"Nitrogen"},
"O":{"row":2,"column":16,"atomic number":8,"name":"Oxygen"},
"F":{"row":2,"column":17,"atomic number":9,"name":"Fluorine"},
"Ne":{"row":2,"column":18,"atomic number":10,"name":"Neon"},
"Na":{"row":3,"column":1,"atomic number":11,"name":"Sodium"},
"Mg":{"row":3,"column":2,"atomic number":12,"name":"Magnesium"},
"Al":{"row":3,"column":13,"atomic number":13,"name":"Aluminum"},
"Si":{"row":3,"column":14,"atomic number":14,"name":"Silicon"},
"P":{"row":3,"column":15,"atomic number":15,"name":"Phosphorus"},
"S":{"row":3,"column":16,"atomic number":16,"name":"Sulfur"},
"Cl":{"row":3,"column":17,"atomic number":17,"name":"Chlorine"},
"Ar":{"row":3,"column":18,"atomic number":18,"name":"Argon"},
"K":{"row":4,"column":1,"atomic number":19,"name":"Potassium"},
"Ca":{"row":4,"column":2,"atomic number":20,"name":"Calcium"},
"Sc":{"row":4,"column":3,"atomic number":21,"name":"Scandium"},
"Ti":{"row":4,"column":4,"atomic number":22,"name":"Titanium"},
"V":{"row":4,"column":5,"atomic number":23,"name":"Vanadium"},
"Cr":{"row":4,"column":6,"atomic number":24,"name":"Chromium"},
"Mn":{"row":4,"column":7,"atomic number":25,"name":"Manganese"},
"Fe":{"row":4,"column":8,"atomic number":26,"name":"Iron"},
"Co":{"row":4,"column":9,"atomic number":27,"name":"Cobalt"},
"Ni":{"row":4,"column":10,"atomic number":28,"name":"Nickel"},
"Cu":{"row":4,"column":11,"atomic number":29,"name":"Copper"},
"Zn":{"row":4,"column":12,"atomic number":30,"name":"Zinc"},
"Ga":{"row":4,"column":13,"atomic number":31,"name":"Gallium"},
"Ge":{"row":4,"column":14,"atomic number":32,"name":"Germanium"},
"As":{"row":4,"column":15,"atomic number":33,"name":"Arsenic"},
"Se":{"row":4,"column":16,"atomic number":34,"name":"Selenium"},
"Br":{"row":4,"column":17,"atomic number":35,"name":"Bromine"},
"Kr":{"row":4,"column":18,"atomic number":36,"name":"Krypton"},
"Rb":{"row":5,"column":1,"atomic number":37,"name":"Rubidium"},
"Sr":{"row":5,"column":2,"atomic number":38,"name":"Strontium"},
"Y":{"row":5,"column":3,"atomic number":39,"name":"Yttrium"},
"Zr":{"row":5,"column":4,"atomic number":40,"name":"Zirconium"},
"Nb":{"row":5,"column":5,"atomic number":41,"name":"Niobium"},
"Mo":{"row":5,"column":6,"atomic number":42,"name":"Molybdenum"},
"Tc":{"row":5,"column":7,"atomic number":43,"name":"Technetium"},
"Ru":{"row":5,"column":8,"atomic number":44,"name":"Ruthenium"},
"Rh":{"row":5,"column":9,"atomic number":45,"name":"Rhodium"},
"Pd":{"row":5,"column":10,"atomic number":46,"name":"Palladium"},
"Ag":{"row":5,"column":11,"atomic number":47,"name":"Silver"},
"Cd":{"row":5,"column":12,"atomic number":48,"name":"Cadmium"},
"In":{"row":5,"column":13,"atomic number":49,"name":"Indium"},
"Sn":{"row":5,"column":14,"atomic number":50,"name":"Tin"},
"Sb":{"row":5,"column":15,"atomic number":51,"name":"Antimony"},
"Te":{"row":5,"column":16,"atomic number":52,"name":"Tellurium"},
"I":{"row":5,"column":17,"atomic number":53,"name":"Iodine"},
"Xe":{"row":5,"column":18,"atomic number":54,"name":"Xenon"},
"Cs":{"row":6,"column":1,"atomic number":55,"name":"Cesium"},
"Ba":{"row":6,"column":2,"atomic number":56,"name":"Barium"},
"La":{"row":8,"column":3,"atomic number":57,"name":"Lanthanum"},
"Ce":{"row":8,"column":4,"atomic number":58,"name":"Cerium"},
"Pr":{"row":8,"column":5,"atomic number":59,"name":"Praseodymium"},
"Nd":{"row":8,"column":6,"atomic number":60,"name":"Neodymium"},
"Pm":{"row":8,"column":7,"atomic number":61,"name":"Promethium"},
"Sm":{"row":8,"column":8,"atomic number":62,"name":"Samarium"},
"Eu":{"row":8,"column":9,"atomic number":63,"name":"Europium"},
"Gd":{"row":8,"column":10,"atomic number":64,"name":"Gadolinium"},
"Tb":{"row":8,"column":11,"atomic number":65,"name":"Terbium"},
"Dy":{"row":8,"column":12,"atomic number":66,"name":"Dysprosium"},
"Ho":{"row":8,"column":13,"atomic number":67,"name":"Holmium"},
"Er":{"row":8,"column":14,"atomic number":68,"name":"Erbium"},
"Tm":{"row":8,"column":15,"atomic number":69,"name":"Thulium"},
"Yb":{"row":8,"column":16,"atomic number":70,"name":"Ytterbium"},
"Lu":{"row":8,"column":17,"atomic number":71,"name":"Lutetium"},
"Hf":{"row":6,"column":4,"atomic number":72,"name":"Hafnium"},
"Ta":{"row":6,"column":5,"atomic number":73,"name":"Tantalum"},
"W":{"row":6,"column":6,"atomic number":74,"name":"Wolfram"},
"Re":{"row":6,"column":7,"atomic number":75,"name":"Rhenium"},
"Os":{"row":6,"column":8,"atomic number":76,"name":"Osmium"},
"Ir":{"row":6,"column":9,"atomic number":77,"name":"Iridium"},
"Pt":{"row":6,"column":10,"atomic number":78,"name":"Platinum"},
"Au":{"row":6,"column":11,"atomic number":79,"name":"Gold"},
"Hg":{"row":6,"column":12,"atomic number":80,"name":"Mercury"},
"Tl":{"row":6,"column":13,"atomic number":81,"name":"Thallium"},
"Pb":{"row":6,"column":14,"atomic number":82,"name":"Lead"},
"Bi":{"row":6,"column":15,"atomic number":83,"name":"Bismuth"},
"Po":{"row":6,"column":16,"atomic number":84,"name":"Polonium"},
"At":{"row":6,"column":17,"atomic number":85,"name":"Astatine"},
"Rn":{"row":6,"column":18,"atomic number":86,"name":"Radon"},
"Fr":{"row":7,"column":1,"atomic number":87,"name":"Francium"},
"Ra":{"row":7,"column":2,"atomic number":88,"name":"Radium"},
"Ac":{"row":9,"column":3,"atomic number":89,"name":"Actinium"},
"Th":{"row":9,"column":4,"atomic number":90,"name":"Thorium"},
"Pa":{"row":9,"column":5,"atomic number":91,"name":"Protactinium"},
"U":{"row":9,"column":6,"atomic number":92,"name":"Uranium"},
"Np":{"row":9,"column":7,"atomic number":93,"name":"Neptunium"},
"Pu":{"row":9,"column":8,"atomic number":94,"name":"Plutonium"},
"Am":{"row":9,"column":9,"atomic number":95,"name":"Americium"},
"Cm":{"row":9,"column":10,"atomic number":96,"name":"Curium"},
"Bk":{"row":9,"column":11,"atomic number":97,"name":"Berkelium"},
"Cf":{"row":9,"column":12,"atomic number":98,"name":"Californium"},
"Es":{"row":9,"column":13,"atomic number":99,"name":"Einsteinium"},
"Fm":{"row":9,"column":14,"atomic number":100,"name":"Fermium"},
"Md":{"row":9,"column":15,"atomic number":101,"name":"Mendelevium"},
"No":{"row":9,"column":16,"atomic number":102,"name":"Nobelium"},
"Lr":{"row":9,"column":17,"atomic number":103,"name":"Lawrencium"},
"Rf":{"row":7,"column":4,"atomic number":104,"name":"Rutherfordium"},
"Db":{"row":7,"column":5,"atomic number":105,"name":"Dubnium"},
"Sg":{"row":7,"column":6,"atomic number":106,"name":"Seaborgium"},
"Bh":{"row":7,"column":7,"atomic number":107,"name":"Bohrium"},
"Hs":{"row":7,"column":8,"atomic number":108,"name":"Hassium"},
"Mt":{"row":7,"column":9,"atomic number":109,"name":"Meitnerium"},
"Ds""":{"row":7,"column":10,"atomic number":110,"name":"Darmstadtium"},
"Rg""":{"row":7,"column":11,"atomic number":111,"name":"Roentgenium"},
"Cn""":{"row":7,"column":12,"atomic number":112,"name":"Copernicium"},
"Uut""":{"row":7,"column":13,"atomic number":113,"name":"Ununtrium"},
"Uuq""":{"row":7,"column":14,"atomic number":114,"name":"Ununquadium"},
"Uup""":{"row":7,"column":15,"atomic number":115,"name":"Ununpentium"},
"Uuh""":{"row":7,"column":16,"atomic number":116,"name":"Ununhexium"},
"Uus""":{"row":7,"column":17,"atomic number":117,"name":"Ununseptium"},
"Uuo""":{"row":7,"column":18,"atomic number":118,"name":"Ununoctium"}}

## source code
```
toContinue = True

while toContinue == True:

    option = input('\n\nTo see all the information for an element, enter 1. \n'
        'To see one property for every element in the table, enter 2 \n'
        'To enter a new element, enter 3. \n'
        'to change the attribues of an element, enter 4. \n'
        'to exit the program, enter 5. \n')
        
    if option == "1":
        element = input("Type the element's symbol: ")
        info = elements[element]
        print("\n\nName: " + str(info["name"]))
        print("Atomic number: " + str(info["atomic number"]))
        print("Row: " + str(info["row"]))
        print("Column: " + str(info["column"]))
        
    elif option == "2":
        attribute = input('Input the property that you want to see the value for: '+
            '\n[name]'+
            '\n[atomic number]'+
            '\n[row]'+
            '\n[column]')
        for element in elements:    
            print("The " + str(attribute) + " of " + str(element) + " is " + str(elements[element][attribute]))
        
    elif option == "3":
        newSymbol = input("Type the new element's symbol name: ")
        newName = input("Type the new element's name: ")
        newNumber = input("Type the new element's atomic number: ")
        newRow = input("Type the new element's row number: ")
        newColumn = input("Type the new element's column number: ")
        elements[newSymbol] = {"name": newName, "atomic number": newNumber, "row": newRow, "column": newColumn}
        
    elif option == "4":
        symbol = input('Enter the symbol of the element to change: ')
        attribute = input('Enter the name of the attribute to change: ')
        value = input('Enter the new value for ' + attribute + ": ")
        elements[symbol][attribute] = value
        
    elif option == "5":
        toContinue = False
 
```
