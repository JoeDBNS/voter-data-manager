-- ============================================================
-- COUNTIES
-- Source: County Codes.csv
-- 83 counties in Michigan
-- county_id is globally unique (PK)
-- ============================================================
CREATE TABLE counties (
    county_id CHAR(2) NOT NULL,
    county_name VARCHAR(40),
    PRIMARY KEY (county_id)
);


-- ============================================================
-- JURISDICTIONS
-- Source: Jurisdiction Codes.csv
-- jurisdiction_id is NOT globally unique — scoped to county
-- PK: (county_id, jurisdiction_id)
-- ============================================================
CREATE TABLE jurisdictions (
    county_id CHAR(2) NOT NULL,
    jurisdiction_id VARCHAR(5) NOT NULL,
    jurisdiction_name VARCHAR(40),
    PRIMARY KEY (county_id, jurisdiction_id),
    FOREIGN KEY (county_id) REFERENCES counties(county_id)
);


-- ============================================================
-- SCHOOL_DISTRICTS
-- Source: School Codes.csv
-- A school district can span multiple county+jurisdiction pairs
-- school_district_id is not globally unique on its own
-- PK: (county_id, jurisdiction_id, school_district_id)
-- ============================================================
CREATE TABLE school_districts (
    county_id CHAR(2) NOT NULL,
    jurisdiction_id VARCHAR(5) NOT NULL,
    school_district_id VARCHAR(5) NOT NULL,
    school_district_name VARCHAR(100),
    PRIMARY KEY (county_id, jurisdiction_id, school_district_id),
    FOREIGN KEY (county_id, jurisdiction_id) REFERENCES jurisdictions(county_id, jurisdiction_id)
);


-- ============================================================
-- PRECINCTS
-- Source: Precinct Codes.csv
-- Precinct codes repeat across jurisdictions
-- PK: (county_id, jurisdiction_id, precinct_id)
-- ============================================================
CREATE TABLE precincts (
    county_id CHAR(2) NOT NULL,
    jurisdiction_id VARCHAR(5) NOT NULL,
    precinct_id VARCHAR(6) NOT NULL,
    precinct_name VARCHAR(100),
    PRIMARY KEY (county_id, jurisdiction_id, precinct_id),
    FOREIGN KEY (county_id, jurisdiction_id) REFERENCES jurisdictions(county_id, jurisdiction_id)
);


-- ============================================================
-- VILLAGES
-- Source: Village Codes.csv
-- id: auto-increment surrogate PK
-- village_id: source ID from CSV (not unique — some villages span
--   multiple county+jurisdiction pairs with the same village_id)
-- Match on (village_id, county_id, jurisdiction_id) when linking
--   from address records
-- ============================================================
CREATE TABLE villages (
    id INT NOT NULL AUTO_INCREMENT,
    village_id INT,
    county_id CHAR(2),
    jurisdiction_id VARCHAR(5),
    village_district_id VARCHAR(5),
    village_name VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (county_id, jurisdiction_id) REFERENCES jurisdictions(county_id, jurisdiction_id)
);


-- ============================================================
-- STATE_HOUSE_DISTRICTS
-- Source: working table
-- state_house_district_id is globally unique (PK)
-- ============================================================
CREATE TABLE state_house_districts (
    state_house_district_id VARCHAR(5) NOT NULL,
    state_house_district_name VARCHAR(100),
    PRIMARY KEY (state_house_district_id)
);


-- ============================================================
-- STATE_SENATE_DISTRICTS
-- Source: working table
-- state_senate_district_id is globally unique (PK)
-- ============================================================
CREATE TABLE state_senate_districts (
    state_senate_district_id VARCHAR(5) NOT NULL,
    state_senate_district_name VARCHAR(100),
    PRIMARY KEY (state_senate_district_id)
);


-- ============================================================
-- US_CONGRESS_DISTRICTS
-- Source: working table
-- us_congress_district_id is globally unique (PK)
-- ============================================================
CREATE TABLE us_congress_districts (
    us_congress_district_id VARCHAR(5) NOT NULL,
    us_congress_district_name VARCHAR(100),
    PRIMARY KEY (us_congress_district_id)
);


-- ============================================================
-- COUNTY_COMMISSIONER_DISTRICTS
-- Source: working table
-- county_commissioner_district_id is globally unique (PK)
-- ============================================================
CREATE TABLE county_commissioner_districts (
    county_commissioner_district_id VARCHAR(5) NOT NULL,
    county_commissioner_district_name VARCHAR(100),
    PRIMARY KEY (county_commissioner_district_id)
);


-- ============================================================
-- UOCAVA_STATUSES
-- Source: working table
-- UOCAVA_status_id is globally unique (PK)
-- ============================================================
CREATE TABLE UOCAVA_statuses (
    UOCAVA_status_id CHAR(1) NOT NULL,
    UOCAVA_status_name VARCHAR(40),
    PRIMARY KEY (UOCAVA_status_id)
);

