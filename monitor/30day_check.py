# -*- coding: utf-8 -*-
# by wangcc
# mail:wangcc_sd@163.com

import pymysql
import datetime

# mysql配置
conn = pymysql.connect('localhost','root','123456','vulnerability')
cursor = conn.cursor()

sqlone = "select count(*) from vulnerability_database;"
cursor.execute(sqlone)
datacount = cursor.fetchone()

sqltwo = "select * from vulnerability_database;"
cursor.execute(sqltwo)
dataall = cursor.fetchall()

for i in range(0,datacount[0]):
    print(dataall[i][1])
    print("创建时间：",dataall[i][23])
    print("更新时间：",dataall[i][24])

    createtime = datetime.datetime.strptime(dataall[i][23],'%Y-%m-%d %H:%M:%S')
    updatetime = datetime.datetime.strptime(dataall[i][24],'%Y-%m-%d %H:%M:%S')

    hour = int(str(updatetime - createtime).split(':')[0])
    gxsql = 'update vulnerability_database set status="1" where id="{}";'.format(str(dataall[i][0]))

    if hour>=720:
        cursor.execute(gxsql)
        conn.commit()


conn.commit()
cursor.close()
conn.close()



