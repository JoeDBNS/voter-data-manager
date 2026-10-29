# voter-data-manager


Total records as of March 2026 - 8291419


## Steps for first import
1) Clean .csv data
2) Create voter_data_mi database (DEV, TEST, and PROD)

In DEV:
   1) Create tables from reference_data files using **reference_tables.sql**
      1) **counties**
      2) **jurisdictions**
      3) **precincts**
      4) **school_districts**
      5) **village_districts**

   2) Insert data into reference data tables
      1) **import_counties.py**
      2) **import_jurisdictions.py**
      3) **import_precincts.py**
      4) **import_school_districts.py**
      5) **import_village_districts.py**

   3) Create **working** table using **working.sql**

   4) Import data into **working** using **import_working.py**

   5)  Create tables from **working** data in order
      1) **state_house_districts**
      2) **state_senate_districts**
      3) **us_congress_districts**
      4) **county_commissioner_districts**
      5)  **uocava_statuses**
      6)  **addresses**
      7)  **voters**

   6)  Add all forign keys in order
      1) **addresses**
      2) **voters**


## Steps for existing data
1) PLACEHOLDER