DROP TABLE IF EXISTS contacts
;
CREATE TABLE contacts(
    contact_id NUMBER(20) PRIMARY KEY,
    fullname VARCHAR2(50),
    phone VARCHAR2(50),
    email VARCHAR2(50)
)
;
