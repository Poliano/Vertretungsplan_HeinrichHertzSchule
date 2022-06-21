# Vertretungsplan für die Heinrich Hertz Schule

Ein einfaches Programm zum auslesen des Heinrich Hertz Vertretungsplanes.

## Versionen
Es gibt bisher 2 Versionen, welche bei der "Branch" Einstellung ausgewählt werden können. Der Master "Branch" enthält die **python** Version auf welcher das Projekt basiert. Der Exe "Branch" enthält eine mit auto-py-to-exe generierte **.exe** Datei für Windows

## Installation

Installation der exe Version 

Datei herunterladen und audführen.


## Nutzung

```
Klasse: 
Klasse: VS
Klasse: 5
Klasse: 5a
Klasse: VSa
Klasse: Settings
Klasse: Einstellungen
Klasse: help
Klasse: hilfe
```
Öffnen Sie Plan.exe und geben Sie die gewünschte Klasse oder den gewünschten Jahrgang ein. Für mehr Informationen geben Sie help oder Hilfe ein. **Groß- und Kleinschreibung ist irrelevant**

## Funktion

Diese Projekt ist ein einfaches Webscraping Projekt von Ben B. und ist möglich geworden da die [WebUntis](https://ikarus.webuntis.com/WebUntis/?school=hh5062#/basic/timetable) Seite auf der [HHS Homepage](https://heinrich-hertz-schule-hamburg.de/) ungesichert ist. Die Angegebene [Vertretungsplan Seite](https://heinrich-hertz-schule-hamburg.de/OnlineVertretungsplan.php) ist zwar von php mit einem Login gesichert, jedoch verweist diese Seite nach dem Login nur auf weitere Seiten der nächsten drei Tage. Diese Seiten lassen sich direkt aufrufen ohne den Login benutzen zu müssen. Da die [url](https://heinrich-hertz-schule-hamburg.de/vertretungsplan/subst_001.htm) der drei Seiten immer gleich bleibt, kann man mit der Hilfe der request Bibliothek in Python die HTML Seite herunterladen und mit bs4 und Pandas analysieren und darstellen.  