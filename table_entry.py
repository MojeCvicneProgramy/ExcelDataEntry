import PySimpleGUI as sg

# výber farby formulára:
sg.theme('DarkTeal9')

# rozloženie formulára:
layout = [
	[sg.Text('Vyplňte prosím nasledujúce polia: ')],
	[sg.Text('Meno', size=(15,1)), sg.InputText(key='Meno')],
	[sg.Submit('Uložiť'), sg.Exit('Ukončiť')]
]

# vytvorenie okna, v ktorom sa to bude zobrazovať:
okno = sg.Window('Jednoduchý formulár pre vkladanie údajov', layout)

#
while True:
	event, values = okno.read()
	if event == sg.WIN.CLOSED or event == 'Exit':
		break
	if event == 'Submit':
		print(event, values)
okno.close()

