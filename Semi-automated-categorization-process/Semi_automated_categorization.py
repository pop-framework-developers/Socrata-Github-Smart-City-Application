#script which create a view called socrata_data_city_usalooks for data.json at socrata portals and store the info of every dataset in socrata_data table
import bdUtils
import jsonUtils
import sqlite3
import re

#open db
conn=bdUtils.openDB()
conn.row_factory = sqlite3.Row

                       
try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Administration & Finance" WHERE THEME IN ("A Well Run City","Administration & Finance","Annual Audit Plan & Reports","Audit Highlights","Audits and Memos","Audits and Reports","Budget","Budget and Management Services","City Administration","City Administration and Finance","City Finance and Budget","City Finances","City Government","City Hall","Economic Data","Economy","FY 2009-2010","FY 2010-2011","FY 2011-2012","FY 2012-2013","FY 2013-2014","FY 2014-2015","FY 2015-2016","Fees","Finance","Financial","Financial Data","Fiscal Year 2013","Fiscal Year 2014","Fiscal Year 2014 Proposed to Council","Fiscal Year 2015","Fiscal Year 2015 Proposed to Council","Fiscal Year 2016","Fiscal Year 2016 Proposed to Council","Fiscal Year 2017","Fiscal Year 2017 Proposed to Council","Forms","Forms and Applications","Government Administration","High Performing Government","Liabilities and Assets","Municipal Court","Purchasing","Revenue")')
except:
    print 'Update Administration & Finance failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Business" WHERE THEME IN ("Business","City Business","City Businesses","Community & Economic Development","Community and Economic Development","Economic Development","Economic Development & Redevelopment","Economy and Community","Economy and Workforce","Growing Economy","KC Bizcare","NYC BigApps","Regulated Industries")')
except:
    print 'Update Business failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Demographics" WHERE THEME IN ("Census","CitiStat","Demographics","Focus","Forecasts","Happiness","Labor","MIDAS","Neighborhoods","Statistics","Stronger Neighborhoods")')
except:
    print 'Update Demographics failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Education" WHERE THEME IN ("Education","Education/Youth/Family","Schools","Smarter Students")')
except:
    print 'Update Education failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Ethics & Democracy" WHERE THEME IN ("City Management and Ethics","Common Investment Meetings (CIM)","Elections","Elections, Politics","Ethics","Expenditures","FOIA","General Information","Governance","Government","Human Relations","Human Resources","Information Bulletins","Legislation","Legislative Info","Local Law 11 Compliance Plan","Monthly Status Reports","Payroll","Peer Review","People", "Permits","Permitting","Personal","Polling Places","Procurement Plan Local Law 63","Public Works","Reference","Regulatory","Regulatory Codes","Scope Statement","State of Vermont","Taxes")') 
except:
    print 'Update Ethics & Democracy failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Geospatial" WHERE THEME IN ("Facilities & Geographic Boundaries","GIS","GIS / Mapping","GIS data","Geographic","Geographic Base Layers","Geographic Boundaries","Geographic Locations and Boundaries","Location")')
except:
    print 'Update Geospatial failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Health" WHERE THEME IN ("Health","Health & Human Services","Health and Human Services","Health and Social Services","Health, Education, and Social Services","Public Health")')
except:
    print 'Update Health failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Recreation & Culture" WHERE THEME IN  ("Arts and Culture", "Arts, Culture, History", "Culture & Arts","Culture and Recreation","Events","Greenways","Historic Preservation","Innovation","Library","Parks & Recreation","Parks and Recreation","Recreation","Recreation and Culture")')
except:
    print 'Update Recreation & Culture failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Safety" WHERE THEME IN ("Code Enforcement","Crime","Emergency","Fire","Police","Police & Fire","Public Safety","Public Safety and Preparedness","Safer Streets","Safety","Wake County EMS")')
except:
    print 'Update Safety failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Services" WHERE THEME IN  ("311","311 Call Center","311 Service Center","City Services","Community","Customer Service","Facilities","Government Buildings and Structures","Inspectional Services","Public Property","Public Services","Requests for Service","Service Requests")')
except:
    print 'Update Services failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Sustainability" WHERE THEME IN ("Agriculture","Brownfields","Energy","Energy and Environment","Environment","Environment & Energy","Environment & Sustainable Development","Environment and Natural Resources","Environment and Sustainability","Environmental","Environmental Management Commission","Food","KC City Energy Project","Natural Resources","Sustainability")')
except:
    print 'Update Sustainability failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Transport & Infrastructure" WHERE THEME IN ("Airport","City Infrastructure","Infrastructure","Infrastructure & Transportation","Infrastructure and Transportation","KCI Terminal Advisory","Metro Transportation","Parking","Streetcar","Traffic","Traffic Sign Changes","Transit","Transportation","Transportation and Infrastructure")')
except:
    print 'Update Transport & Infrastructure failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Urban Planning & Housing" WHERE THEME IN ("Area Plans","Building and Safety","Buildings","Buildings & Trails","City Facilities","city infrastructure","City Park and Tree Data","Construction","Development","Development Review","Housing","Housing & Development","Housing / Development","Housing and Buildings","Housing and Development","Housing, Land Use, and Blight","Land Base","Land Development","Land Use","Parks","Planning","Planning and Development","Planning, Zoning","Property","Real Estate, Land Records","Urban Planning")')
except:
    print 'Update Urban Planning & Housing failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Welfare" WHERE THEME IN ("BERS (NYC Board of Education Retirement System)","FIRE (NYC Fire Department Pension Fund)","Human Potential","Human Services","Insurance","Life Enrichment","NYCERS (NYC Employees\' Retirement System)","POLICE (NYC Police Pension Fund)","Quality of Life","Retirement","Sanitation","Social Services","TRS (Teachers\' Retirement System City of New York)")')
except:
    print 'Update Welfare failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'Update USA_CITY_DATASETS_CATEGORIZED set CATEGORY="Others" WHERE THEME IN  ("Archived","Auction","Code Interpretations","Internal")')
except:
    print 'Update Others failed'
conn.commit()


  
print '--BD  updated!'
conn.close()
print '--BD  closed!'

