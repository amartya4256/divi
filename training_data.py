import pandas as pd, sqlite3, os
files = "static/"
counter = 0

for file in os.listdir(files):
    conn = sqlite3.connect(files+"{}".format(file))
    cur = conn.cursor()

    limit = 5000
    last_unix = 0
    cur_len = limit
    tested = False

    while cur_len == limit:
        data = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} AND parent NOT NULL AND score > 10 ORDER BY unix ASC LIMIT {}".format(last_unix, limit), conn)
        last_unix = data.tail(1)['unix'].values[0]
        cur_len = len(data)

        if not tested:
            with open("test_from", "a", encoding="utf8") as f:
                for parent_content in data['parent']:
                    f.write(parent_content+"\n")

            with open("test_to", "a", encoding="utf8") as f:
                for parent_content in data['comment']:
                    f.write(parent_content+"\n")

            tested = True

        else:
            with open("train_from", "a", encoding="utf8") as f:
                for parent_content in data['parent']:
                    f.write(parent_content + "\n")

            with open("train_to", "a", encoding="utf8") as f:
                for parent_content in data['comment']:
                    f.write(str(parent_content) + "\n")

        counter += 1

        if counter%20==0:
            print(counter*limit, "rows completed...")