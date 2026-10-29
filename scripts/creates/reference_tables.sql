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
