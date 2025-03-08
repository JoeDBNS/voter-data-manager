# voter-data-manager

## Steps for first import
1) Clean .csv data
2) Create voter_data_mi database (DEV, TEST, and PROD)

In DEV:
   1) Create **working** table
   2) Import data into **working**
   3) Create tables from **working** data in order
      1) **counties**
      2) **jurisdictions**
      3) **school_districts**
      4) **state_house_districts**
      5) **state_senate_districts**
      6) **us_congress_districts**
      7) **county_commissioner_districts**
      8) **village_districts**
      9) **uocava_statuses**
      10) **addresses**
      11) **voters**
   4) Add all forign keys in order
      1) **addresses**
      2) **voters**


## Steps for existing data
1) PLACEHOLDER