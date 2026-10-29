# voter-data-manager


Total records as of March 2026 - 8291419


## Steps for first import
1) Clean .csv data
2) Create voter_data_mi database (DEV, TEST, and PROD)

In DEV:
   1) Create all tables from reference_data files using **reference_tables.sql**

   2) Run **find_distinct_pairs.py** to build additional reference data from the source data

   2) Insert data into reference data tables
      1) **import_counties.py**
      2) **import_jurisdictions.py**
      3) **import_precincts.py**
      4) **import_school_districts.py**
      5) **import_village_districts.py**
      6) **import_congress_districts.py**
      7) **import_county_commissioner_districts.py**
      8) **import_house_districts.py**
      9) **import_senate_districts.py**
      10) **import_uocava_statuses.py**

   3) Create **working** table using **working.sql**

   4) Import data into **working** using **import_working.py**

   5)  Create tables from **working** data in order
      1) **addresses**
      2) **voters**

   6)  Add all forign keys in order
      1) **addresses**
      2) **voters**


## Steps for existing data
1) PLACEHOLDER