# Hey lol this was made by Shadow1/shadow1Python

import subprocess, colorama, requests, base64, os

os.system('@title Mydesk 2.0 ^| AnyDesk IP Address Resolver ^| by shadow1')

from colorama import Fore, Style

colorama.init()

anydesk_pids = []
anydesk_address = {}
ip_addr = []
old_port = 0
old_ip = ''

# banner
print(base64.b64decode(b'G1szN20KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZDhiICAgICAgICAgICAgICAgICBkOGIgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA4OFAgICAgICAgICAgICAgICAgID84OCAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZDg4ICAgICAgICAgICAgICAgICAgIDg4YiAgICAgICAgICAKIGQ4ODhiOGIgICAgODhiZDg4YiA/ODggICBkOFAgIGQ4ODg4ODggICBkODg4OGIgLmQ4ODhiLCAgODg4ICBkODgnICAgIApkOFAnID84OCAgICA4OFAnID84YmQ4OCAgIDg4ICBkOFAnID84OCAgZDhiXyxkUCA/OGIsICAgICA4ODhiZDhQJyAgICAgCjg4YiAgLDg4YiAgZDg4ICAgODhQPzgoICBkODggIDg4YiAgLDg4YiA4OGIgICAgICAgYD84YiAgZDg4ODg4YiAgICAgICAKYD84OFAnYDg4YmQ4OCcgICA4OGJgPzg4UCc/OGIgYD84OFAnYDg4YmA/ODg4UCdgPzg4OFAnIGQ4OCcgYD84OGIsICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICApODggICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgLGQ4UCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICBgPzg4OFAnICAgICAgICAgICAgICAgICAgICAgICBNYWRlIGJ5IFNoYWRvdy9zaGFkb3cxIzYyNDQvc2hhZG93MVB5dGhvbgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkOGIgICAgICAgICAgICAgICAgICAgR0lUSFVCOiBodHRwczovL2dpdGh1Yi5jb20vc2hhZG93MVB5dGhvbi9NeURlc2sKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgODhQICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGQ4OCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgODhiZDg4YiBkODg4OGIgLmQ4ODhiLCBkODg4OGIgODg4ICA/ODggICBkOFAgZDg4ODhiICA4OGJkODhiICAgICAgICAKICA4OFAnICBgZDhiXyxkUCA/OGIsICAgZDhQJyA/ODg/ODggIGQ4OCAgZDhQJ2Q4Yl8sZFAgIDg4UCcgIGAgICAgICAgIAogZDg4ICAgICA4OGIgICAgICAgYD84YiA4OGIgIGQ4OCA4OGIgPzhiICw4OCcgODhiICAgICBkODggICAgICAgICAgICAgCmQ4OCcgICAgIGA/ODg4UCdgPzg4OFAnIGA/ODg4OFAnICA4OGJgPzg4OFAnICBgPzg4OFAnZDg4JyAgICAgICAgICAgICAKCg==').decode() + "\nwaiting for connection...", end='')

while 1:
	try:
		if str(subprocess.check_output("tasklist")).count('AnyDesk') <= 3:
			pass
		else:
			for line in str(subprocess.check_output("tasklist")).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n'):
				if 'AnyDesk' in line:
					try:
						anydesk_pids.append(line.split('.exe')[1].split()[0].replace(' ', ''))
						
					except Exception as e:
						pass
			nstats_output_lines = str(subprocess.check_output('netstat -p TCP -n -a -o')).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n')
			for pid in anydesk_pids:
				for line in nstats_output_lines:
					if pid in line and not 'LISTENING' in line:
						try:
							parts = line.split()
							protocol = parts[0]
							local_addr = parts[1]
							remote_addr = parts[2].split(':')[0]
							remote_port = parts[2].split(':')[1]
							anydesk_address[remote_addr] = int(remote_port)
						except Exception as e:
							print(e)
			for ip, port in anydesk_address.items():
				if int(port) > old_port and not '169.254.' in ip:
					old_port = int(port)
					old_ip = ip
			remote_ip = old_ip
			remote_port = old_port
			print(f'{Fore.GREEN} connection established!')
			try:
				json_data = requests.get(f'http://extreme-ip-lookup.com/json/' + remote_ip).json()
				print(Style.BRIGHT + '''
{12}╔════════════════════════════════════════════╗
{12}║ {13}IP{14}:{13} {0}{6} {12}║ 
{12}║ {13}Country{14}:{13} {1}{7} {12}║ 
{12}║ {13}City{14}:{13} {2}{8} {12}║ 
{12}║ {13}ISP{14}:{13} {3}{9} {12}║ 
{12}║ {13}Lat{14}:{13} {4}{10} {12}║ 
{12}║ {13}Lon{14}:{13} {5}{11} {12}║ 
{12}╚════════════════════════════════════════════╝
				'''.format(json_data['query'], json_data['country'], json_data['city'], json_data['isp'], json_data['lat'], json_data['lon'], (' ' * (38 - int(len(json_data['query'])))), (' ' * (33 - int(len(json_data['country'])))), (' ' * (36 - int(len(json_data['city'])))), (' ' * (37 - int(len(json_data['isp'])))), (' ' * (37 - int(len(json_data['lat'])))), (' ' * (37 - int(len(json_data['lon'])))),Fore.RED, Fore.WHITE, Fore.BLACK))
			except:
				print('hum.')
			input('press \'enter\' to continue...')
			exit()
	except KeyboardInterrupt:
		print('ctrl+c'); exit()

input()
