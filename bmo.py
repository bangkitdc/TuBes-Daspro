def interface():
	print(
'''⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡤⠶⠶⠶⠶⠒⠒⠒⠒⠚⠛⠛⠛⠛⠛⠓⠒⠒⠒⠒⠲⠶⠶⠶⠤⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡇⠄⠄⠄⠄⠄⠄⢠⡔⠛⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⠛⠛⢦⡀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⠄⠄⠄⠄⠄⠄⢀⡏⠄⠄⣀⠤⠖⠒⠒⠒⠚⠛⠛⠛⠛⠛⠛⠛⠒⠒⠒⠒⠶⢄⡀⠈⣇⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⡏⠄⠘⠁⠄⠆⠄⢸⡇⠄⠄⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⡇⠄⣿⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢀⡇⠈⠁⠠⠄⠠⡆⢸⡇⠄⢸⡇⠄⠄⠄⠜⠛⠇⠄⠄⠄⠄⠄⠄⠄⠄⠞⠛⠄⠄⢸⡇⠄⣿⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢸⡇⠄⠶⠄⠄⠄⠄⢸⡇⠄⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠙⠛⠛⠁⠄⠄⠄⠄⠄⠄⢸⡇⠄⣧⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⠄⠄⢸⡇⠄⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⡇⠄⣿⠄⠄⠄⠄⠄⠄⠄
⢠⣤⣀⠄⠄⠄⠄⠄⢸⡇⢠⣤⣀⠄⠄⠄⢸⡇⠄⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⡇⠄⡏⠄⠄⠄⠄⠄⠄⠄
⢿⠿⢿⠄⠄⠄⠄⠄⢸⡇⢸⣿⣿⢿⡇⠄⢸⠃⠄⠸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⠇⠄⡇⠄⠄⠄⠄⠄⠄⠄
⢸⡄⠈⣆⠄⠄⠄⠄⢸⡇⢘⡿⠿⣿⡇⠄⢸⠄⠄⠄⠙⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠖⠁⠄⠄⡇⠄⠄⠄⠄⠄⠄⠄
⠈⢇⠄⠻⡀⠄⠄⠄⢸⡇⠸⣿⣷⣶⡆⠄⢸⠄⠄⠄⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠄⠄⠄⠄⢠⠂⣦⠄⠄⠄⠄⡇⠄⠄⠄⠄⠄⠄⠄
⠄⠘⣦⠄⠙⣤⠄⠄⢸⡇⢸⣿⣿⣿⡀⠄⢸⠄⠄⠄⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠄⠄⠄⠄⠄⠉⠁⠄⠄⠄⢀⡇⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠈⠷⣀⠈⠳⢆⣸⡇⢀⣉⣉⠛⠃⠄⢸⠄⠄⠄⠄⠄⠄⢀⣀⡀⠄⠄⠄⠄⠄⠄⠄⢀⡀⠄⠄⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠉⠲⢄⡀⠉⠙⠛⠿⢿⣷⡀⠄⢸⠄⠄⠄⠄⠄⠄⣚⡋⣓⡆⠄⠄⠄⠄⠄⢰⡿⠹⡆⠄⠄⠄⠄⠄⢸⡧⢄⣀⡀⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠈⠛⡶⢦⣤⣾⣿⠁⠄⢸⠄⠄⠄⠄⠄⠄⠘⠛⠃⠄⠄⠄⠄⠄⠄⠉⢉⡉⠉⠄⣿⠉⡇⠄⢸⣧⣤⠄⠙⠳⣄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢧⠄⠉⠉⠄⠄⠄⢸⠄⠄⠄⠄⣀⣀⣀⡀⢀⣀⣀⠄⠄⠄⠄⣼⡟⠁⠙⣆⠙⠛⠁⠄⢸⡇⠄⠙⠦⣀⠈⢧⡀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢦⣀⠄⠄⠄⠄⢸⠄⠄⠄⠄⠻⠶⠾⠃⠱⠶⠶⠃⠄⠄⠄⠱⠵⠤⠴⠁⠄⠄⠄⠄⢸⡇⠄⠄⠄⠹⣄⢈⣇
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠓⠲⣤⣀⢸⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⠄⠄⠄⠄⠄⠹⡿⠟
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⠳⢤⣤⣤⣤⣤⣤⠤⠤⠤⠤⠤⠤⠤⠤⡤⠴⢶⡖⠒⠒⠒⠚⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣇⠄⠛⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⢧⠄⠘⠳⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠶⢤⣀⠗⠄⠄⠄⠄⠄⠄⠄⠄⠈⠑⠶⠶⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
''')
	return
