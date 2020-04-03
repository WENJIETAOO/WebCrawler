CREATE DATABASE IF NOT EXISTS seniordesign;
USE seniordesign;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS UrlIndex;
create table UrlIndex
(
	UrlId int auto_increment,
	FileName varchar(255),
	URLListName varchar(255),
	PRIMARY KEY(UrlId)
);
ALTER TABLE UrlIndex AUTO_INCREMENT = 1;


DROP TABLE IF EXISTS Urls;
create table Urls
(
	UrlId int,
	Url varchar(255),
	UrlType varchar(255),
	UrlComment varchar(255),
	PRIMARY KEY(UrlId, Url),
	CONSTRAINT `fk_url_index`
		FOREIGN KEY (UrlId) REFERENCES UrlIndex (UrlId)
		ON DELETE CASCADE
		ON UPDATE RESTRICT
);

DROP TABLE IF EXISTS AttributeIndex;
create table AttributeIndex
(
	AttributeId int auto_increment,
	FileName varchar(255),
	AttributeListName varchar(255),
	PRIMARY KEY(AttributeId)
);
ALTER TABLE AttributeIndex AUTO_INCREMENT = 1;

DROP TABLE IF EXISTS Attributes;
create table Attributes
(
	AttributeId int,
	AttributeName varchar(255),
	AttributeType varchar(10),
	Pattern varchar(255),
	PRIMARY KEY(AttributeId, AttributeName),
	CONSTRAINT `fk_attribute_index`
		FOREIGN KEY (AttributeId) REFERENCES AttributeIndex (AttributeId)
		ON DELETE CASCADE
		ON UPDATE RESTRICT
);

DROP TABLE IF EXISTS CrawlDataIndex;
CREATE TABLE CrawlDataIndex
(
	CrawlDataId int auto_increment,
	CrawlDataTableName varchar(255),
	PRIMARY KEY(CrawlDataId)
);
# Not sure if we need the above, it serves as a list of crawl data that has been created

SET FOREIGN_KEY_CHECKS = 1;
/*select * from Urls where UrlId = 1;
Delete from Urls where UrlId = 1;*/

DELIMITER //
DROP PROCEDURE IF EXISTS getDocumentListById;
DROP PROCEDURE IF EXISTS getAttributeListById;
DROP PROCEDURE IF EXISTS addAttributeData;
DROP PROCEDURE IF EXISTS addAttributeIndex;
DROP PROCEDURE IF EXISTS addCrawlTableData;
DROP PROCEDURE IF EXISTS getCrawlTableData;
DROP PROCEDURE IF EXISTS addURLData;
DROP PROCEDURE IF EXISTS addUrlIndex;

CREATE PROCEDURE getDocumentListById(IN docid INT)
 BEGIN
	 SELECT * FROM Urls WHERE UrlId = docid;
 end;
//

CREATE PROCEDURE getAttributeListById(IN docid INT)
 BEGIN
	 SELECT * FROM Attributes WHERE AttributeId = docid;
 end;
//

CREATE PROCEDURE addAttributeIndex(IN attfilename VARCHAR(255), IN attname VARCHAR(255))
	BEGIN
		INSERT INTO AttributeIndex (FileName, AttributeListName) VALUES (attfilename, attname);
		SELECT LAST_INSERT_ID();
	end; //

CREATE PROCEDURE addAttributeData(IN attid VARCHAR(255), IN attname VARCHAR(255), IN atttype VARCHAR(255), IN attpatt VARCHAR(255))
	BEGIN
		INSERT INTO Attributes (AttributeId, AttributeName, AttributeType, Pattern) VALUES (attid, attname, atttype, attpatt);
	end; //
															     
CREATE PROCEDURE addUrlIndex(IN urlfilenameIn VARCHAR(255), IN urllistnameIn VARCHAR(255))
	BEGIN
		INSERT INTO UrlIndex (FileName, URLListName) VALUES (urlfilenameIn, urllistnameIn);
		SELECT LAST_INSERT_ID();
	end; //

CREATE PROCEDURE addURLData(IN urlidIn VARCHAR(255), IN urlIn VARCHAR(255), IN urltypeIn VARCHAR(255), IN urlcommentIn VARCHAR(255))
	BEGIN
		INSERT INTO Urls (UrlId, Url, UrlType, UrlComment) VALUES (urlidIn, urlIn, urltypeIn, urlcommentIn);
	end; //

CREATE PROCEDURE addCrawlTableData(IN tableNameIn VARCHAR(255))
	BEGIN
		IF NOT EXISTS(SELECT 1 FROM CrawlDataIndex WHERE CrawlDataTableName = tableNameIn) THEN
			INSERT INTO CrawlDataIndex (CrawlDataTableName) VALUES (tableNameIn);
			SELECT LAST_INSERT_ID();
		ELSE
				UPDATE CrawlDataIndex SET CrawlDataTableName = tableNameIn WHERE CrawlDataTableName = tableNameIn;
		end if;
	end;
//

CREATE PROCEDURE getCrawlTableData(IN tableNameIn VARCHAR(255))
	BEGIN
		SET @table_name = tableNameIn;
		SET @sql_text1 = concat('SELECT * FROM ',@table_name);
		PREPARE stmt1 FROM @sql_text1;
		EXECUTE stmt1;
		DEALLOCATE PREPARE stmt1;
	end //
DELIMITER ;


