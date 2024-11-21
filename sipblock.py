import json
from subprocess import Popen, PIPE, STDOUT
from log import Logger



logger = Logger.getLogger('DialogSipBlock', 'logs/DialogSipBlock')


class Sipblock:
    def sipBlockDialog(data, ref):
        logger.info("sipBlockDialog : %s" % ref + " - " + str(data['num_list']))    
        
        for num in data['num_list']:
        
            p = Popen(['java', '-jar', 'jars/Ebanline.jar', 'TrunkNumberBlocking', 'HQ-IBCF','3004',num,'ADD'], stdout=PIPE, stderr=STDOUT)
            for line in p.stdout:
                print(line)
            
            #subprocess.call(['java', '-jar', 'jars/Ebanline.jar', 'TrunkNumberBlocking', 'HQ-IBCF','3004',num,'ADD'])
            #subprocess.call(['java', '-jar', 'jars/Ebanline.jar', 'TrunkNumberBlocking', 'WEL_IBCF','3004',num,'ADD'])
            print(num)
        return 0    
        
