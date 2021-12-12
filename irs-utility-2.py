# Taking a tax form name (ex: "Form W-2") and a range of years 
# (inclusive, 2018-2020 should fetch three years), 
# download all PDFs available within that range. 
# The forms returned should be an exact match for the input 
# (ex: "Form W-2" should not return "Form W-2 P", etc.) 
# The downloaded PDFs should be downloaded to a subdirectory 
# under your script's main directory with the name of the form, 
# and the file name should be the "Form Name - Year" (ex: Form W-2/Form W-2 - 2020.pdf)

# write function taking in form name, min year, max year
# use logic from search page function in irs-utility-1 to find all table rows containing form name
# use logic from parse_info() in irs-urility-1 to find records that fully match form name, and if year is valid
# if year is valid and name matching, call new function that downloads the pdf into subdirectory with a specified name
# to download the pdf:
  # find the 'a' tag content within the current tr. 
  # use with open('pdf url', 'wb') as f: to open the pdf (remember to close it)

import requests
import os
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')

def get_pdf(row, name, year):
  url = list(row.absolute_links)[0]
  file_name = f"{name} - {year}.pdf"
  file_path = os.path.join(name, file_name)

  if not os.path.exists(name):
    os.makedirs(name)
  
  with open(file_path, "wb") as f:
    f.write(requests.get(url).content)

def parse_info(trs, form_name, min_year, max_year):
  """ Takes in a form name, list of table rows containing the form name. 

  The function loops through each row, and extracts text from the three inner <td> elements. 
  
  If the form name of the current row is an exact match to the form name passed in, 
  the unpacked form info is passed to add_update_dict()
  """
  for row in trs:
    form_info = row.text.split("\n")
    name, title, year = form_info[0], form_info[1], form_info[2]
    if name == form_name:
      if int(year) in range(min_year, max_year + 1):
        get_pdf(row, name, year)


def search_page(form_name, year_range):
  """ Takes in a form name and year range and loops through each page to find table rows containing the form name.
  
  All matching rows on each page are collected in a list and passed into the parse_info() along with the form name
  """
  years = year_range.split('-')
  min_year, max_year = int(years[0]), int(years[1])
  for page in r.html:
    trs = page.find('tr', containing=form_name)
    if trs:
      form_info = parse_info(trs, form_name, min_year, max_year)


search_page('Form W-2', '1984-2012')