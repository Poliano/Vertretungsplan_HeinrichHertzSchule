from bs4 import BeautifulSoup
import requests
import pandas as pd
days = 3
dropindex = "n"

substring = input("Klasse: ")
if str(substring).lower() == "hilfe" or str(substring).lower() == "help":
    print(
    '''Einfach den Namen der Klasse Eingeben oder sie Stufen Bezeichnung:
    VS für Vorstufe oder 5 für alle Klassen aus dem Jahrgang 5
    5a oder Med1 für die Klasse 5a oder das Medien Profil 1
    Wenn du ohne eingabe Enter drückst bekommst du alle Klasse
    Gebe Einstellungen oder Settings ein um in die Einstellungen zu kommen
    ''')
elif substring == "einstellungen" or str(substring).lower() == "settings":
    days = int(input(f"({days}) Vorausschaunde Tage: "))    #number of listed future tables
    if days > 3 or days < 0 or days == "":  #max 3 days in to the future
        print("Days Fehler Zahl muss zwischen 0-3 sein")
        days = 3
    dropindex = str(input(f"({dropindex}) Index Neubeginnen: "))    #reset index or use existing
    if dropindex.lower() != "y" and dropindex.lower() != "n":
        print("Falsche Eingabe Entweder Y oder N")
        dropindex = "n"
    
substring = substring.replace(" ", "")  #removing spaces from request

for urllist in range(days): 
    urllist = urllist + 1
    url = f"https://www.heinrich-hertz-schule-hamburg.de/vertretungsplan/subst_00{urllist}.htm" #url of the time table
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser") #using bs4 for the html header to get date bs4 and requests libarys are just to get the date an slow the program a lot down but there is no way th get the date with pandas :(

    date = doc.div.string   #get date from html header
    print("--- " + date + " ---")   #cosmetic for the date

    dfs = pd.read_html(url, index_col=False)
    df = dfs[1] #get second table (first is adress of school)
    df = df[df['Klasse(n)'].str.contains(substring, case=False, na=False)]  #search in column Klasse(n) for the request

    if dropindex == "y":
        df = df.reset_index(drop=True)

    if "Empty DataFrame" in str(df):
        print("Keine Vertretung")
        print("")
    else:
        print(df)   #final table
        print("")