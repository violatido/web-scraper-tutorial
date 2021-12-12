# **IRS Utilities**

Created by Ilana Mercer


## **Requirements**
* Python 3.8.0
* Pip


## **Usage**

#### Create a virtual environment
``` bash
python3 -m venv env
```
#### activate the virtual environment
``` bash
source env/bin/activate
```
#### Install the requirements
```bash
pip3 install -r requirements.txt
```


## **Running the first utility:**
#### **input:** place form names within brackets in the print statement on line 68:
```bash
print(get_form_info(["form name", "form name", "etc"]))
```

#### run in terminal:
```bash
python3 irs-utility-1.py
```

#### **output:** output is in the terminal, preceded by a built-in string:
```bash
The requested form information is as follows:

[{"form_number": "Publ 15", "form_title": "Circular E, Employer's Tax Guide", "min_year": "1988", "max_year": "2021"}, {"form_number": "Form W-2", "form_title": "Wage and Tax Statement (Info Copy Only)", "min_year": "1954", "max_year": "2021"}]
```


## **Running the second utility:**
#### **input:** place form name, year range within brackets in the print statement on line 52:
```bash
print(search_page(["form name", "year1-year2"]))
```

#### run in terminal:
```bash
python3 irs-utility-2.py
```

#### **output:** output is in side bar of IDE, within subdirectories that will hold requested pdf files
