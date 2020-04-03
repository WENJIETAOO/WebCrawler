USE seniordesign;

/*
Use the following template for inserting values with the last generated index ID
INSERT INTO author (name) VALUES ('Abdul Alhazred');
INSERT INTO book (title, author_id) VALUES ('Necronomicon', LAST_INSERT_ID());

INSERT INTO author (name) VALUES ('H.P. Lovecraft');
INSERT INTO book (title, author_id) VALUES
	('The call of Cthulhu', LAST_INSERT_ID()),
	('The colour out of space', LAST_INSERT_ID());
*/

insert into Urls(Url, UrlType, UrlComment) values ('www.wikipedia.com','','');
insert into Urls(Url, UrlType, UrlComment) values ('www.google.com','','');
insert into Urls(Url, UrlType, UrlComment) values ('www.unb.ca','','');

insert into Attributes(AttributeName,AttributeType,Pattern) values ('aaa','r','bbb');
insert into Attributes(AttributeName,AttributeType,Pattern) values ('ccc','x','ddd');
insert into Attributes(AttributeName,AttributeType,Pattern) values ('eee','r','fff');

EXEC addUrlIndex urlfilenameIn = 'www.wikipedia.com', 'urlList';
EXEC addURLData urlidIn = LAST_INSERT_ID(), urlIn = 'www.wikipedia.com', urltypeIn = '', urlcommentIn = '';
EXEC getAttributeData attributeIdIn = '1';
EXEC addCrawlTableData tableNameIn = 'exampleTable';
