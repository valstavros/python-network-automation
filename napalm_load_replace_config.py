from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'}
ios = driver('192.168.1.10', 'stavros', 'cisco', optional_args=optional_args)
ios.open()
print('Connection established ...')
# start your code here ...
ios.load_replace_candidate(filename='IOU1_config.txt')

diff = ios.compare_config()
# print(diff)
if len(diff) > 0:
    print('Differences found:')
    print(diff)
    print('Committing the changes ...')
    ios.commit_config()
    print('Changes committed ...')
else:
    print('No differences found ...')
    print('Discarding the changes ...')
    ios.discard_config()
    print('Changes discarded ...')
# end your code here ...
ios.close()
print('Connection closed ...')