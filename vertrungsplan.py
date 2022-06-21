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
    days = int(input(f"({days}) Vorausschaunde Tage: "))
    if days > 3 or days < 0 or days == "":
        print("Days Fehler Zahl muss zwischen 0-3 sein")
        days = 3
    dropindex = str(input(f"({dropindex}) Index Neubeginnen: "))
    if dropindex.lower() != "y" and dropindex.lower() != "n":
        print("Falsche Eingabe Entweder Y oder N")
        dropindex = "n"
    
substring = substring.replace(" ", "")

for urllist in range(days): 
    urllist = urllist + 1
    url = f"https://www.heinrich-hertz-schule-hamburg.de/vertretungsplan/subst_00{urllist}.htm"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    date = doc.div.string
    print("--- " + date + " ---")

    dfs = pd.read_html(url, index_col=False)
    df = dfs[1]
    df = df[df['Klasse(n)'].str.contains(substring, case=False, na=False)]

    if dropindex == "y":
        df = df.reset_index(drop=True)

    if "Empty DataFrame" in str(df):
        print("Keine Vertretung")
        print("")
    else:
        print(df)
        print("")