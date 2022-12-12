import pymysql, traceback

def getRigistRequest(user, password):
    db = pymysql.connect("localhost","root","mysql","***" )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    sql = f"INSERT INTO user(user, password) VALUES ({user}, {password})"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        db.close()
        return 1
    except Exception:
        #抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        db.close()
        return 0
    
def getLoginRequest(user, password):
    db = pymysql.connect("localhost","root","mysql","***" )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 查询语句
    sql = f"select * from user where user={user} and password={password}"
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(len(results))
        db.close()
        return 1 if len(results)==1 else 0
    except Exception:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        db.close()
        return 0