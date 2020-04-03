import pymysql


connectionInstance   = pymysql.connect(host="127.0.0.1",port=3306,user="root", password="abc123",
charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

#change to your password

try:

    cursorInsatnce        = connectionInstance.cursor()                                    

    sqlQuery     = "use crawler"

    cursorInsatnce.execute(sqlQuery)

    sqlQuery     = "show tables"

    cursorInsatnce.execute(sqlQuery)

    databaseList   = cursorInsatnce.fetchall()

    for datatbase in databaseList:

        print(datatbase)

    print("which function you want use?\n 1. insert\n 2. select\n 3. delete\n 4. select for specific Id")

    a = input()

    if a == '1':
        print("1 forUrls\n2 for Attributes")
        b = input()
        if b == '1':
            print("Enter Url")
            UrlIn = input()
            
            print("Enter Comment")
            ComIn = input()
            
            sqlQuery = "insert into Urls(Url,UrlComment) values ('%s','%s')" % (UrlIn,ComIn)
            try:
                cursorInsatnce.execute(sqlQuery)
                connectionInstance.commit()
            except:
                connectionInstance.rollback()
            
            sqlQuery = "select UrlId from Urls where Url = '%s'" % (UrlIn)
            cursorInsatnce.execute(sqlQuery)
            IdIns = cursorInsatnce.fetchall()
            print(IdIns)


        if b == '2':
            print("Enter Attribute Name ")
            name = input()

            print("Enter RegexOrXpath r for Regex x for Xpath")
            RorX = input()
 
            print("Enter pattern")
            pat = input()
            sqlQuery = "insert into Attributes(AttributeName,RegexOrXpath,Pattern)  values ('%s','%s','%s')" % (name,RorX,pat)
            try:
                cursorInsatnce.execute(sqlQuery)
                connectionInstance.commit()
            except:
                connectionInstance.rollback()

    if a == '2':
        print("1 forUrls\n2 for Attributes")
        c = input()
        if c == '1':
            sqlQuery     = "select * from Urls"
            cursorInsatnce.execute(sqlQuery)
            Urls = cursorInsatnce.fetchall()
            for UrlList in Urls:
                print(UrlList)

        if c == '2':
            sqlQuery     = "select * from Attributes"
            cursorInsatnce.execute(sqlQuery)
            Attributes = cursorInsatnce.fetchall()
            for AttList in Attributes:
                print(AttList)

    if a == '3':
        print("1 forUrls\n2 for Attributes")
        d = input()
        if d == '1':
            print("Enter the UrlId you want delete")
            UrlDel = input();
            sqlQuery = "Delete from Urls where Url = '%s'" % (UrlDel)
            try:
                cursorInsatnce.execute(sqlQuery)
                connectionInstance.commit()
            except:
                connectionInstance.rollback()
        if d =='2':
            print("Enter the AttributeId you want delete")
            AttDel = input();
            sqlQuery = "Delete from Attributes where AttributeName = '%s'" % (AttDel)
            try:
                cursorInsatnce.execute(sqlQuery)
                connectionInstance.commit()
            except:
                connectionInstance.rollback()

    if a =='4':
        print("1 forUrls\n2 for Attributes")
        e = input()
        if e == '1':
            print("Enter the Id you want select")
            idSel = int(input())
            sqlQuery     = "select * from Urls where UrlId = %d" % (idSel)
            cursorInsatnce.execute(sqlQuery)
            Url = cursorInsatnce.fetchall()
            print(Url)

        if e == '2':
            print("Enter the Id you want select")
            idSel = int(input())
            sqlQuery     = "select * from Attributes where AttributeId = %d" % (idSel)
            cursorInsatnce.execute(sqlQuery)
            Attribute = cursorInsatnce.fetchall()
            print(Attribute)
except Exception as e:

    print("Exeception occured:{}".format(e))
        


finally:
    connectionInstance.close()
