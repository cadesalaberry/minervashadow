#!/usr/bin/env python
"""
Usage:
	minerva login
	minerva register <class_crns>...
	minerva drop <class_crn>
	minerva transcript
	minerva check <class_crn>
	minerva search <class_name> | <class_crn>
	minerva list [all]
	minerva -h | --help
	minerva -v | --version

Examples:
	minerva register 6969
	minerva transcript
	minerva check 321
	minerva search ecse420

Options:
	-h, --help     Show this screen.
	-v, --version  Print the current version.
"""

from minerva import MinervaSession
from docopt import docopt
import ui


def start():

	try:
		handled_exit()
	except KeyboardInterrupt:
		print '\n\nExiting...\nHope to see you soon!'


def handled_exit():
	
	args = docopt(__doc__, version='0.0.2')
	validRequest = True

	if args['register']:
		if len(args['<class_crns>']) < 10:
			print 'Trying to register to:', args['<class_crns>']
		else:
			print 'Error: Too many CRNs specified.'
			validRequest = False


	if validRequest:

		credentials = ui.get_user_credentials()

		session = MinervaSession(credentials)

		if not args['login']:
			session.login()

		session.deal_with_request(args)

		session.logout()
		print 'Logged out !'

	else:
		print 'Error: Invalid input.'
		print 'try "minerva -h" to display the help screen.'
		print 'Exiting...'