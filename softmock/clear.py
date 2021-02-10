import sqlite3
from softmock.database import database


def clear():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "delete from Mock1"

    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    print('清理完成')
