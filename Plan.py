#A Project by Ben Ber 2022

#!/usr/bin/env python3
print("--- Stundenplan Abfrage HHS ---")    #just to cover up the loading time (psst)
print("")
from bs4 import BeautifulSoup	#just used to get the date very inefficient
import requests
import pandas as pd
#defaults
days = 3
dropindex = "n"
loop = "y"

while loop  == "y":
	substring = input("Klasse: ")
	print("")
	if str(substring).lower() == "hilfe" or str(substring).lower() == "help":
		print(
		'''Einfach den Namen der Klasse Eingeben oder sie Stufen Bezeichnung:
		VS für Vorstufe oder 5 für alle Klassen aus dem Jahrgang 5
		5a oder Med1 für die Klasse 5a oder das Medien Profil 1
		Wenn du ohne eingabe Enter drückst bekommst du alle Klasse
		Gebe Einstellungen oder Settings ein um in die Einstellungen zu kommen
		''')
	elif substring == "einstellungen" or str(substring).lower() == "settings":

		dayspre = days
		days = input(f"({days}) Vorausschaunde Tage: ")    #number of listed future tables
		if days == "":
			days = dayspre
		days = int(days)
		if int(days) > 3 or int(days) < 1 or int(days) == "":  #max 3 days in to the future
			print("Days Fehler Zahl muss zwischen 0-3 sein")
			days = dayspre

		dropindexpre = dropindex	#saves sate before question
		dropindex = input(f"({dropindex}) Index Neubeginnen: ")    #reset index or use existing
		if dropindex == "":
			dropindex = dropindexpre
		if dropindex.lower() != "y" and dropindex.lower() != "n":
			print("Falsche Eingabe Entweder Y oder N")
			dropindex = dropindexpre
		if dropindex != dropindexpre:
			if dropindex.lower() == "y":
				print(f"Index Neubeginnen geändert zu: ({loop})")
				dropindex = "y"
			if dropindex.lower()== "n":
				print(f"Index Neubeginnen geändert zu: ({loop})")
				dropindex = "n"

		looppre = loop	#saves sate before question
		loop = input(f"({loop}) Programm Schleife: ")  #loop request
		if loop == "":
			loop = "y"
		if loop.lower() != "y" and loop.lower() != "n":
			print("Falsche Eingabe Entweder Y oder N")
			loop = looppre
		if loop != looppre:
			if loop.lower() == "y":
				print(f"Programm Schleife geändert zu: ({loop})")
				loop = "y"
			if loop.lower()== "n":
				print(f"Programm Schleife geändert zu: ({loop})")
				loop = "n"
		
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