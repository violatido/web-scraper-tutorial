# Taking a list of tax form names (ex: "Form W-2", "Form 1095-C"), 
# search the website and return some informational results. 
# Specifically, you must return the "Product Number", the "Title", 
# and the maximum and minimum years the form is available for download. 
# The forms returned should be an exact match for the input (ex: "Form W-2" should not return "Form W-2 P", etc.) 
# The results should be returned as json, in the format of the following example:

# [
#   {
#     "form_number": "Form W-2",
#     "form_title": "Wage and Tax Statement (Info Copy Only)",
#     "min_year_": 1954,
#     "max_year": 2021
#   }
# ]