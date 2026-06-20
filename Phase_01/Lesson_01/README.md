# Lesson_01: Print, Kommentare und Variablen

## Lernziele
- Die Verwendung von `print()` lernen
- Kommentare in Python verstehen
- Variablen deklarieren und verwenden
- Einfache Berechnungen mit Variablen durchführen
- Variablenwerte ändern und überschreiben

## Wichtige Konzepte

### 1. `print()` Funktion
- Text und Werte in der Konsole ausgeben
- Variablenwerte direkt in print() verwenden
- Mehrere print()-Aufrufe für verschiedene Ausgaben

### 2. Kommentare
- **Einzeilige Kommentare**: `# Das ist ein Kommentar`
- Erklären, was jede Zeile Code tut
- Helfen anderen und dir selbst, Code zu verstehen

### 3. Variablen
- Variablen speichern Informationen im Speicher
- Datentypen: `str` (Text), `int` (Ganzzahl)
- Aussagekräftige Variablennamen verwenden
- Variablenwerte können berechnet werden (z.B. `alter = aktuellesJahr - geburtsJahr`)
- Variablen können überschrieben werden (z.B. `alter = 20`)

## Beispiele aus main.py

```python
# Variablen erstellen
name = "Trần Nguyễn Ngọc"
geburtsJahr = 2007
aktuellesJahr = 2026

# Berechnung mit Variablen
alter = aktuellesJahr - geburtsJahr

# Variablen ausgeben
print(name)
print(alter)

# Variablenwert ändern
alter = 20
print(alter)  # Jetzt 20 ausgeben
