# SRM-evarsityCalc
Calculates required hours to make attendance at least 75%, and number of hours available to bunk if attendance is greater than 75%, in short it is a crude version of now discontinued 'INSTIFY'
It uses BeautifulSoup 4.4 for scraping data from web page along with urllib.request to retrive web page. Due to restriction against inspecting elements on evarsity website, web page download is neccessary.

To excute:                                                        
> python 3                        
> install BeautifulSoup v4.0 or above                      
> save 'testRes' folder any directory (else see instruction-2)                         
> specify 'loc' variable in evarsitycalc.py with testRes direcory                             
  
To exceute with diffrent evarsity account(instruction-2):              
> log in your evarsity account                              
> go to 'Attendance' section                                
> save the webpage in system                              
> specify directory of webpage in 'loc' variable                                   
> configure 'start' and 'end' variables of evarsity.py file                               
> this is one time configuration for any specific account                              
