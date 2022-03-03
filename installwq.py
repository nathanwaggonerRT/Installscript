import configparser
import sys


# Create variables for input arguments
customer_abr = sys.argv[1]
customer_full = sys.argv[2]


#======Startup========
# Create Startup.ini parser
startupconfig = configparser.ConfigParser()
startupconfig.read('C:\\inetpub\\wwwroot\\WQ\\p21_{}\\etc\\startup.ini'.format(customer_abr))

#Variables to update in startup.ini
startupconfig.set('User Database', 'userdatabase', 'P21_{}_WQMetaData'.format(customer_abr))
startupconfig.set('PHP','offlinebatdir','C:\\PHP\\tempphpscripts\\P21_{}'.format(customer_abr))
startupconfig.set('General','basedir','C:\\PHP\\tempphpscripts\\P21_{}\\'.format(customer_abr))

#Writing updates to startup.ini
with open('C:\\inetpub\\wwwroot\\WQ\\p21_{}\\etc\\startup.ini'.format(customer_abr), 'w') as startupconfigfile:
    startupconfig.write(startupconfigfile, space_around_delimiters=False)


#======DWConfig=============
#Create DWConfig.ini parser
dwconfig = configparser.ConfigParser()
dwconfig.read('C:\\inetpub\\wwwroot\\WQ\\p21_{}\\etc\\dwconfig.ini'.format(customer_abr))

#Variables to update in dwconfig.ini
dwconfig.set('MetaData', 'mddatabase', 'P21_{}_WQMetaData'.format(customer_abr))
dwconfig.set('Email', 'notifyfromname', '{} WebQuery'.format(customer_full))
dwconfig.set('ResultSets', 'resultsetdb', 'P21_{}_WQResultsets'.format(customer_abr))
dwconfig.set('Dates', 'fiscalperiodsloc', 'P21_{}_WQMetaData'.format(customer_abr))
dwconfig.set('General Config', 'sqllog', 'P21_{}_WQMetaData'.format(customer_abr))
dwconfig.set('General Config', 'schedulelog', 'P21_{}_WQMetaData'.format(customer_abr))
dwconfig.set('UI', 'pagetitle', '{} WebQuery'.format(customer_abr))

#Writing updates to dwconfig.ini
with open('C:\\inetpub\\wwwroot\\WQ\\p21_{}\\etc\\dwconfig.ini'.format(customer_abr), 'w') as dwconfigfile:
    dwconfig.write(dwconfigfile, space_around_delimiters=False)