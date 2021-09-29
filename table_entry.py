import PySimpleGUI as sg
import pandas as pd

# výber farby formulára:
sg.theme('DarkTeal9')

# vytvoriť tabuľku v Exceli tak, aby názvy stĺpcov boli pomenované presne ako keys v tomto programe
# vloženie tabuľky do premennej EXCEL_FILE
EXCEL_FILE = 'Table.xlsx'
df = pd.read_excel(EXCEL_FILE)

# rozloženie formulára:
layout = [
	[sg.Text('Vyplňte prosím nasledujúce polia: ')],
	[sg.Text('Meno', size=(15,1)), sg.InputText(key='meno')],
	[sg.Text('Obľúbená farba', size=(15,1)), sg.Combo(['zelená','modrá','červená'], key='farba')],
	[sg.Text('Ovládam', size=(15,1)),
	                        sg.Checkbox('nemčinu', key='nemčina'),
							sg.Checkbox('angličtinu', key='angličtina'),
							sg.Checkbox('španielčinu', key='španielčina')],
	[sg.Text('Počet detí', size=(15,1)), sg.Spin([i for i in range (0,16)],
	                                             initial_value=0, key='deti')],

	[sg.Submit('Uložiť'), sg.Button('Vyčistiť'), sg.Exit('Ukončiť')]
]

# vytvorenie okna, v ktorom sa to bude zobrazovať:
okno = sg.Window('Jednoduchý formulár pre vkladanie údajov', layout)

# tlačidlo Clear - vyčistenie obsahu
def clear_input():
	for key in values:
		okno[key]('')
	return None


# zatvorenie okna ak niekto stlačí Exit - 'Ukončiť'
# vloženie údajov do Excelu a vypísanie správy o vložení údajov
# vyčistenie tabuľky, tlačidlo clear - Vyčistiť
while True:
	event, values = okno.read()
	if event == sg.WIN_CLOSED or event == 'Ukončiť':
		break
	if event == 'Vyčistiť':
		clear_input()
	if event == 'Uložiť':
		df = df.append(values, ignore_index=True)
		df.to_excel(EXCEL_FILE, index=False)  # vkladá do excelu, iba ak je excel súbor zavretý
		sg.popup('Údaje vložené!')
		clear_input()
		print(event, values)  # toto vypisuje práve vložené hodnoty aj v IntelliJ
okno.close()
