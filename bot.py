from telethon import TelegramClient, events, sync
from time import sleep
#from requests import get
import csv

api_id = 1424461
api_hash = '0defeef68470555247ae26206bebf895'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

#print(client.get_me().stringify())
#group_array = ['frcp_deals', 'stealsales']
#filter_array = ['Amazon fire', 'Cinthol', 'Cooler', 'Extension', 'Keyboard', 
#                           'LED', 'Loot', 'Lux', 'Mask', 'Mouse', 'N95', 'Pad', 'RO', 'Sanitizer', 
#                            'Steal', 'cooler', 'loot', 'lux', 'mask', 'n95', 'pad', 'sanitizer', 'vivobook']

group_array = list(csv.reader(open('groups.csv')))[0]
filter_array = list(csv.reader(open('filters.csv')))[0]
prev_config = 0
last_message = {}

for g in group_array:
        last_message[g] = 0
while True:
        #client.send_message('juspay', 'group' + '\n\n' + 'text')
        config_messages = client.iter_messages('juspay')
        for msg in config_messages:
                text = msg.text
                if text and msg.id != prev_config:
                        prev_config = msg.id
                        if '/filter' in text:
                                text = text.replace('/filter ', '')
                                if text not in filter_array:
                                        filter_array.append(text)
                                        csv.writer(open('filters.csv', 'w')).writerow(filter_array)
                                        client.send_message('juspay', text + ' added to filters')
                        elif '/join' in text:
                                text = text.replace('/join ', '')
				last_message[text] = 0
                                if text not in group_array:
                                        group_array.append(text)
                                        csv.writer(open('groups.csv', 'w')).writerow(group_array)
                                        client.send_message('juspay', text + ' added to groups')
                        elif '/notfilter' in text:
                                text = text.replace('/notfilter ', '')
                                if text in filter_array:
                                        filter_array.remove(text)
                                        csv.writer(open('filters.csv', 'w')).writerow(filter_array)
                                        client.send_message('juspay', text + ' removed from filters')
                        elif '/exit' in text:
                                text = text.replace('/exit ', '')
                                if text in group_array:
                                        group_array.remove(text)
                                        csv.writer(open('groups.csv', 'w')).writerow(group_array)
                                        client.send_message('juspay', text + ' removed from groups')
                        elif '/print' in text:
                                client.send_message('juspay', '\n'.join(group_array) + '\n\n' + '\n'.join(filter_array))

                        #else:
                        #        client.send_message('juspay', 'invalid format')
                break

        #print(group_array)
        #print(filter_array)
        sleep(5)
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
                                                client.send_message('juspay', group + '\n\n' + text)
                        break
                #print(group)

