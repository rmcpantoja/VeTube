from sound import playsound
ps = playsound()

device_names = ps.devicenames
print("Dispositivos disponibles:")
for i, name in enumerate(device_names):
	print(f"{i+1}. {name}")
	ps.setdevice(i+1)
	print(f"Dispositivo establecido: {device_names[i-1]}")
	file_to_play = "sounds/abrirchat.wav"
	ps.playsound(file_to_play, True)