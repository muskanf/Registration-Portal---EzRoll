-- use ezroll;
-- --  SHOW VARIABLES LIKE 'secure_file_priv';

-- DROP TABLE IF EXISTS Classes;
-- CREATE TABLE Classes (
--     TERM_CODE VARCHAR(100) NOT NULL,
--     CRN VARCHAR(100) NOT NULL,
--     TERM_DESC VARCHAR(200) NOT NULL,
-- 	TITLE VARCHAR(200) NOT NULL,
--     SUBJ_CODE VARCHAR(10) NOT NULL,
--     SUBJ_DESC VARCHAR(100) NOT NULL,
--     CRSE_NUM VARCHAR(100) NOT NULL,
--     SEQ_NUM VARCHAR(100) NOT NULL,
--     XLST_GROUP VARCHAR(100),
--     SCHD_DESC VARCHAR(200) NOT NULL,
--     MAX_ENRL VARCHAR(100) NOT NULL,
--     CREDIT_HR VARCHAR(100) NOT NULL,
--     COLL_DESC VARCHAR(200) NOT NULL,
--     DEPT_DESC VARCHAR(200) NOT NULL,
--     BLDG_DESC VARCHAR(200) NOT NULL,
--     ROOM_CODE VARCHAR(10),
--     BEGIN_TIME VARCHAR(100) NOT NULL,
--     END_TIME VARCHAR(100) NOT NULL,
--     START_DATE VARCHAR(100),
--     END_DATE VARCHAR(100),
--     SUN_DAY VARCHAR(10),
--     MON_DAY VARCHAR(10),
--     TUE_DAY VARCHAR(10),
--     WED_DAY VARCHAR(10),
--     THU_DAY VARCHAR(10),
--     FRI_DAY VARCHAR(10),
--     SAT_DAY VARCHAR(10),
--     HRS_WEEK VARCHAR(100)
--     -- PRIMARY KEY (CRN)
-- );

-- LOAD DATA INFILE '2021-2022_Course_schedule.csv' 
-- INTO TABLE Classes 
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

-- Do not alter, bestif everything is kept as a string
-- ALTER TABLE CLASSES
-- MODIFY COLUMN CREDIT_HR INT,
-- MODIFY COLUMN MAX_ENRL INT,
-- MODIFY COLUMN BEGIN_TIME INT,
-- MODIFY COLUMN END_TIME INT;
