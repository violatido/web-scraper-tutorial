import json
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
form_dict = dict()

def add_update_dict(name, title, year):
  """ Takes in a form name, form title, and form year.

  Updates the form year if the name is already in the dictionary, adds a dictionary entry otherwise.
  """
  if name not in form_dict:
    form_dict[name] = {
          "form_number": name,
          "form_title": title,
          "min_year": year,
          "max_year": year
        }
  elif year < form_dict[name]["min_year"]:
    form_dict[name]["min_year"] = year
  elif year > form_dict[name]["max_year"]:
    form_dict[name]["max_year"] = year

def parse_info(trs, form_name):
  """ Takes in a form name, list of table rows containing the form name. 

  The function loops through each row, and extracts text from the three inner <td> elements. 

  If the form name of the current row is an exact match to the form name passed in, 
  the unpacked form info is passed to add_update_dict()
  """
  for row in trs:
    form_info = row.text.split("\n")
    name, title, year = form_info[0], form_info[1], form_info[2]
    if name == form_name:
      add_update_dict(name, title, year)

def search_page(form_name):
  """ Takes in a form name and loops through each page to find table rows containing the form name.
  
  All matching rows on each page are collected in a list and passed into the parse_info() along with the form name
  """

  for page in r.html:
    trs = page.find('tr', containing=form_name)
    if trs:
      form_info = parse_info(trs, form_name)

def get_form_info(form_names):
  """ Takes in a list of form names, passes each name to for table row searches.

  After the form dictionary has been completed, the values from the dictionary are placed into a list
  and returned in JSON format.
  """
  for name in form_names:
    search_page(name)

  form_list = [value for value in form_dict.values()]
  jd = json.dumps(form_list, indent = 4)

  return f"The requested form information is as follows:\n\n{jd}"

## BLANK INPUT ##
# print(get_form_info([]))

## EXAMPLE INPUT ##
print(get_form_info(["Publ 15", "Form W-2"]))
