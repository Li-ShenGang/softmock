import sqlite3


def clear():
    db = sqlite3.connect("soft_mock.db")
    cursor = db.cursor()
    sql = "delete from Mock1"

    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    print('清理完成')
