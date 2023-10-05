import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

ID = input("Enter NCBI number: ")

def edit_val(value_id, intended_value):
    v = driver.find_element(By.NAME, value_id)
    v.clear()
    v.send_keys(str(intended_value))
    return v


opts = Options()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.ncbi.nlm.nih.gov/tools/primer-blast/index.cgi?ORGANISM=10090&INPUT_SEQUENCE=' + str(ID) +
           '&LINK_LOC=nuccore')


PCR_product_min = edit_val('PRIMER_PRODUCT_MIN', 100)
PCR_product_max = edit_val('PRIMER_PRODUCT_MAX', 150)
PCR_min_Tm = edit_val('PRIMER_MIN_TM', 60)
PCR_opt_Tm = edit_val('PRIMER_OPT_TM', 61.5)
PCR_delta_Tm = edit_val('PRIMER_MAX_DIFF_TM', 1)
Intron_min_length = edit_val('MIN_INTRON_SIZE', 200)

intron_sep = driver.find_element(By.ID, "SPAN_INTRON")
driver.execute_script("arguments[0].click();", intron_sep)
