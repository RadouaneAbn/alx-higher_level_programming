-- This script converts a database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

ALTER TABLE hbtn_0c_0.first_table
	CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
