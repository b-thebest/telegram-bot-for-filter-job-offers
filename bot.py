from telethon import TelegramClient, events, sync
from time import sleep
from collections import defaultdict

api_id = 1657894
api_hash = '3bd1e08efa3683d490bfeb8ba512d5ba'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

#print(client.get_me().stringify())
group_array = ['frcp_deals', 'stealsales']
filter_array = ['Amazon fire', 'Cinthol', 'Cooler', 'Extension', 'Keyboard', 
			    'LED', 'Loot', 'Lux', 'Mask', 'Mouse', 'N95', 'Pad', 'RO', 'Sanitizer', 
                            'Steal', 'cooler', 'loot', 'lux', 'mask', 'n95', 'pad', 'sanitizer', 'vivobook']
last_message = {}

for g in group_array:
	last_message[g] = 0

while True:
	for group in group_array:
		messages = client.iter_messages(group)
		for message in messages:
			#print(message.id)
			#print(message.text)
			text = message.text
			if text and message.id != last_message[group]:
				last_message[group] = message.id
				for elem in filter_array:
					if elem in text:
						client.send_message('filterdeal', group + '\n\n' + text)
			break
		#print(group)

