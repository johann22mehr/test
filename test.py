from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
#Set a default screensize...
#There are other ways of setting up the browser so that we can grab the full browser view,
#even long pages that would typically require scrolling to see completely
#For example: https://blog.ouseful.info/2019/01/16/converting-pandas-generated-html-data-tables-to-png-images/
driver.set_window_size(800, 400)
 
#Load a webpage at a specified URL
driver.get( URL )
 
#Handy bits...
#EC.visibility_of_element_located
#EC.presence_of_element_located
#EC.invisibility_of_element_located
 
#Let's wait for the spinny thing to disappear...
element = WebDriverWait(driver, 10).until( EC.invisibility_of_element_located((By.ID, undesiredId)))
 
#Save the page
driver.save_screenshot( outfile )
print('Screenshot saved to {}'.format(outfile))