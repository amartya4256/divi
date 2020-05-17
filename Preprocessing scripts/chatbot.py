import json
import sqlite3
from datetime import datetime
import sys

sql_transaction = []
timeframe = sys.argv[1].split("/")[-1]
print(timeframe)

connection = sqlite3.connect("static/{}.db".format(timeframe))
c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, 
    parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)""")

def find_parent(pid):
    try:

        sql = 'SELECT comment FROM parent_reply WHERE comment_id = "{}" LIMIT 1'.format(pid)
        c.execute(sql)
        res = c.fetchone()
        if res!=None:
            return res[0]
        else:
            return False
    except Exception as e:
        return False

def find_existing_score(pid):
    try:
        sql = 'SELECT score FROM parent_reply WHERE parent_id =' + pid + ' LIMIT 1'
        c.execute(sql)
        res = c.fetchone()
        if res != None:
            print(res[0])
            return res[0]
        else:
            return False
    except Exception as e:
        return False

def format_data(data):
    data = data.replace('\n', '  newlinechar  ').replace('\r', '  newlinechar  ').replace('"', "'")
    return data

def acceptable(data):
    if len(data.split(' '))>50 or len(data)<1:
        return False
    elif len(data)>1000:
        return False
    elif data == '[deleted]' or data == '[removed]':
        return False
    else:
        return True

def sql_insert_replace_commnet(comment_id, parent_id, parent_data, body, subreddit, created_utc, score):
    try:
        sql = "UPDATE parent_reply set parent_id = '{}', comment_id = '{}', parent = '{}', comment = '{}', subreddit = '{}', unix = '{}', score = '{}' WHERE parent_id = '{}';".format(parent_id, comment_id, parent_data, body, subreddit, created_utc, score, parent_id)
        transaction_builder(sql)
    except Exception as e:
        print('sql_insert_replace_comment', e)

def sql_insert_has_parent(comment_id, parent_id, parent_data, body, subreddit, created_utc, score, row_counter):
    try:
        sql = "INSERT INTO parent_reply (parent_id, comment_id, parent, comment, subreddit, unix, score) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(parent_id, comment_id, parent_data, body, subreddit, created_utc, score)
        transaction_builder(sql)
    except Exception as e:
        print('sql_insert_has_parent', e)

def sql_insert_no_parent(comment_id, parent_id, body, subreddit, created_utc, score):
    try:
        sql = "INSERT INTO parent_reply (parent_id, comment_id, comment, subreddit, unix, score) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(parent_id, comment_id, body, subreddit, created_utc, score)
        transaction_builder(sql)
    except Exception as e:
        print('sql_insert_has_parent', row_counter, e)

def transaction_builder(sql):
    global sql_transaction
    sql_transaction.append(sql)
    if len(sql_transaction)>1000 :
        c.execute('BEGIN TRANSACTION')
        for i in sql_transaction:
            try:
                c.execute(i)
            except:
                pass
        connection.commit()
        sql_transaction = []


if __name__== "__main__":
    create_table()
    row_counter = 0
    paired_row = 0

    with open("project data/"+timeframe) as f:
        for row in f:
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            subreddit = row['subreddit']
            comment_id = row['name']
            parent_data = find_parent(parent_id)

            if score >= 2 and acceptable(body):
                existing_comment_score =  find_existing_score(parent_id)
                if existing_comment_score:
                    if existing_comment_score < score:
                        sql_insert_replace_commnet(comment_id, parent_id, parent_data, body, subreddit, created_utc, score)
                        print("buu yeah")

                else:
                    if parent_data:
                        sql_insert_has_parent(comment_id, parent_id, parent_data, body, subreddit, created_utc, score, row_counter)
                        paired_row += 1
                    else:
                        sql_insert_no_parent(comment_id, parent_id, body, subreddit, created_utc, score)

            if row_counter % 100000 == 0:
                print("Total rows read : {}, Total paired rows : {}, Time : {}".format(row_counter, paired_row, str(datetime.now())))


