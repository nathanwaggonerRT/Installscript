@echo off

::Create inputs
set /p customer_abr=Customer Abreviation:
set /p customer_full=Customer Full Name: 

::Build new customer directory from template
robocopy C:\inetpub\wwwroot\WQ\webquery C:\inetpub\wwwroot\WQ\p21_%customer_abr% /E

::Create tempphpscript logging directory
mkdir C:\PHP\tempphpscripts\P21_%customer_abr%

::Run python script to update newly added configs
python %~dp0\installwq.py %customer_abr% %customer_full%

pause