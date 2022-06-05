SeleniumWithPython

info:  
 --browser [chrome, firefox, ie] --html=..\..\reports\Report.html -m mark_name

run:  
 --browser chrome --html=..\..\reports\Report.html -m smoke
 
headless:  
--browser chrome --html=..\..\reports\Report.html -m smoke --headless 1
