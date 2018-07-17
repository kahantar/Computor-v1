#!/usr/bin/python
import simplification
import sys
import re

if len(sys.argv) != 2:
    print("Erreur Parametre")
    sys.exit()
equation = sys.argv[1]
reg = r"^(-\s)?([0-9]*[.]?[0-9]*\s\*\sX\^[0-9]*)(\s[-+]\s[0-9]*[.]?[0-9]*\s\*\sX\^[0-9]*)*\s=\s(-\s)?([0-9]*[.]?[0-9]*\s\*\sX\^[0-9]*)(\s[-+]\s[0-9]*[.]?[0-9]*\s\*\sX\^[0-9]*)*$"
if re.search(reg, equation) is None:
    print("Erreur format")
else:
    resolveur = simplification.Resolveur(equation)
    resolveur.parse()
    resolveur.simplification()
    resolveur.resolution()
