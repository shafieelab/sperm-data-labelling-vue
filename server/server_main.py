import os
import sqlite3
import time

import numpy as np
from flask import Flask, g, send_file, request, jsonify, abort

# slides = ['F039','F048','E952','F065','F014','E911','F067','F100','F109']
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

# dir_path = '/home/ubuntu/flask_server'
# dir_path = '/home/hemanthkandula/WebstormProjects/DataAnnotator/server'
dir_path = '/home/hemanthkandula/WebstormProjects/DataAnnotator/server'
dir_path = '/mnt/data_drive/flask_server'

database = dir_path + "/DataLabellingAPI.db"
image_path = dir_path + "/image_data/"
set_size = 10


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

print(database)
# TABLE CREATION
if not os.path.isfile(database):
    slides = list(set(  map(lambda x: x.split("_")[0],os.listdir(image_path))))
    # slides = ['aa']
    # slides = getslidess()
    temp_counter = [0] * len(slides)
    set_no = [0] * len(slides)
    with app.app_context():
        conn = get_db()
        print(conn)
        conn.execute('CREATE TABLE User_Table (username TEXT PRIMARY KEY, password TEXT, usernameact TEXT)')  # USER TABLE

        conn.execute('CREATE TABLE Assigned_Table (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                     'username TEXT, slide TEXT, slide_set INTEGER , UNIQUE (username,slide, slide_set))')  # Assigned TABLE

        conn.execute(
            'CREATE TABLE Image_Table  (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, imname TEXT, slide TEXT, slide_set INTEGER,'  # Image TABLE
            'label TEXT, discarded TEXT, UNIQUE (imname,username,slide, slide_set,discarded))')

        conn.execute('CREATE TABLE Pool_Table  (imname TEXT PRIMARY KEY, slide TEXT, slide_set INTEGER)')  # Pool Table

        conn.execute(
            'CREATE TABLE Slide_Table (slide TEXT PRIMARY KEY, counter INTEGER, mcount INTEGER, GA TEXT)')  # Slide Table

        conn.execute(
            'CREATE TABLE Flag_Table  (id INTEGER PRIMARY KEY, username TEXT, image_name TEXT, comment TEXT)')  # Flag_Table

        _all_images = os.listdir(image_path)

        for image in _all_images:
            for _ in range(len(slides)):
                if slides[_] in image:
                    if temp_counter[_] % set_size == 0:
                        set_no[_] += 1
                    conn.execute("INSERT INTO Pool_Table (imname, slide, slide_set) VALUES('" + image + "', '" + slides[
                        _] + "', " + str(
                        set_no[_]) + ")")  # Adding image name, slide name, set no Pool Labels
                    temp_counter[_] += 1

        for _ in range(len(slides)):
            slide = slides[_]
            conn.execute("INSERT INTO Slide_Table (slide, counter, mcount) VALUES('" + slide + "', 1, " + str(
                set_no[_]) + ")")  # Adding image name sto Image Labels

        conn.commit()
        conn.close()

        [print(_, __, ___) for _, __, ___ in zip(slides, set_no, temp_counter)]

    exit()


@app.route("/index", methods=['GET'])  # Just to check the server is running
def index():
    print("index", "=" * 50)
    return " server runing"


@app.route("/getslides", methods=['POST'])  # Just to check the server is running
def getslides():
    print("index", "=" * 50)
    conn = get_db()
    slides = [_[0] for _ in conn.execute('SELECT slide FROM Slide_Table')]

    user_data = ""
    for user in slides:
        user_data += user + ";"

    return jsonify({"slides": user_data[:-1]})


# @app.route("/getslidess", methods=['POST'])  # Just to check the server is runni$
def getslidess():
    # print("index", "=" * 50)
    conn = sqlite3.connect(database)
    slides = [_[0] for _ in conn.execute('SELECT slide FROM Slide_Table')]
    conn.close()
    return (slides)


@app.route("/getcheck", methods=['POST'])  # Just to check the server is runni$
def getchecks():
    print("index", "=" * 50)
    # conn = get_db()
    # slides = [_[0] for _ in conn.execute('SELECT slide FROM Slide_Table')]
    ssss = getslidess()
    return jsonify(ssss)


@app.route("/version", methods=['GET'])  # Just to check the server is running
def version():
    print("version_check", "=" * 50)
    ver = open(dir_path + "/version.txt").read()
    return ver


def discard_set(set_no, username, slide):
    #    print("/rest_slide", "=" * 20, user_data)

    conn = sqlite3.connect(database)

    conn.execute(
        "UPDATE Image_Table SET discarded = 'true' WHERE username LIKE '" + username + "' and slide_set LIKE '" + set_no + "' and slide LIKE '" + slide + "'")

    if (not username == "" and not slide == ""):
        set_no, max_c = conn.execute("SELECT counter, mcount FROM Slide_Table WHERE slide = '" + slide + "'").fetchone()
        if set_no + 1 > max_c:
            conn.execute("UPDATE Slide_Table SET counter = 1 WHERE slide = '" + slide + "'")
        else:
            conn.execute("UPDATE Slide_Table SET counter = " + str(set_no + 1) + " WHERE slide = '" + slide + "'")
        conn.commit()

        conn.execute("Delete from Assigned_Table where  username ='" + username + "', slide = '" + slide + "'")

        # Set the same in assigned table
        conn.execute(
            "INSERT INTO Assigned_Table (username, slide, slide_set) VALUES('" + username + "', '" + slide + "', " + str(
                set_no) + ")")

        # Add images for user with empty labels.
        # 1) Get images
        images = conn.execute(
            "SELECT imname FROM Pool_Table WHERE slide = '" + slide + "' AND slide_set = " + str(set_no)).fetchall()

        # 2) add it to image_table
        for image in images:
            conn.execute(
                "INSERT INTO Image_Table (username, imname, slide, slide_set) VALUES('" + username + "', '" + image[
                    0] + "', '" + slide + "', " + str(
                    set_no) + ")")

        conn.commit()


def caluclate_accuracy(set_no, username, slide):
    conn = sqlite3.connect(database)
    user_good_count = conn.execute(
        "SELECT count(*) FROM Image_Table WHERE username = '" + username + "' AND slide_set = " + str(
            set_no) + " AND slide = '" + slide +
        "' AND label like '0' AND discarded IS null ORDER BY id DESC").fetchone()[0]

    user_total_count = conn.execute(
        "SELECT count(*) FROM Image_Table WHERE username = '" + username + "' AND slide_set = " + str(
            set_no) + " AND slide = '" + slide +
        "' AND label not like '4' AND discarded IS null ORDER BY id DESC").fetchone()[0]
    accuracy = user_good_count / user_total_count * 100
    print(accuracy)
    return accuracy


def check_set(set_no, username, slide):
    # acc= caluclate_accuracy(set_no,username,slide)
    acc = 10
    listo = [['E014', '4'], ['E030', '5'], ['E031', '5'], ['E034', '7'], ['E044', '14'], ['E047', '6'], ['E064', '8'],
             ['E066', '10'], ['E073', '3'], ['E088', '2'], ['E090', '4'], ['E098', '2'], ['E101', '3'], ['E102', '2'],
             ['E109', '6'], ['E857', '10'], ['E858', '3'], ['E859', '5'], ['E878', '3'], ['E880', '2'], ['E883', '9'],
             ['E884', '8'], ['E885', '6'], ['E886', '9'], ['E895', '6'], ['E892', '12'], ['E894', '13'], ['E901', '3'],
             ['E902', '3'], ['E903', '2'], ['E900', '6'], ['E910', '9'], ['E911', '8'], ['E912', '5'], ['E913', '6'],
             ['E914', '5'], ['E915', '8'], ['E918', '5'], ['E919', '6'], ['E928', '6'], ['E929', '11'], ['E931', '4'],
             ['E932', '6'], ['E934', '10'], ['E942', '2'], ['E943', '5'], ['E944', '12'], ['E948', '6'], ['E949', '8'],
             ['E950', '3'], ['E952', '9'], ['E953', '7'], ['E954', '8'], ['E955', '4'], ['E959', '8'], ['E960', '3'],
             ['E961', '3'], ['E962', '8'], ['E963', '3'], ['E964', '5'], ['E873', '6'], ['E979', '6'], ['E986', '10'],
             ['E989', '1'], ['E990', '3'], ['E995', '6'], ['E996', '3'], ['E997', '2'], ['E998', '6'], ['E999', '3']]

    for x in (listo):
        if slide in x:
            clarliee_acc = int(x[1])
            print(x[1])

            if ((clarliee_acc - 2) <= acc <= (clarliee_acc + 2)):
                kkkkk = 1
                print(str(acc) + 'worked')
            else:
                discard_set('3', 'Sneha', 'E014')


# check_set('3','Sneha','E014')


def check_slide_completed(conn, username, slide):
    images = conn.execute(
        "SELECT imname FROM Pool_Table where slide ='" + slide + "' Except SELECT imname FROM Image_Table where slide ='" + slide + "' and username ='" + username + "' and discarded IS null ").fetchall()
    conn.commit()
    if len(images) == 0:
        return True
    else:
        return False


def assign_next_set(conn, slide, username):
    set_no, max_c = conn.execute("SELECT counter, mcount FROM Slide_Table WHERE slide = '" + slide + "'").fetchone()

    if set_no + 1 > max_c:

        # return(max_c)
        print(max_c)
        conn.execute("UPDATE Slide_Table SET counter = 1 WHERE slide = '" + slide + "'")
    else:
        conn.execute("UPDATE Slide_Table SET counter = " + str(set_no + 1) + " WHERE slide = '" + slide + "'")
        conn.commit()

    # Set the same in assigned table
    conn.execute(
        "INSERT INTO Assigned_Table (username, slide, slide_set) VALUES('" + username + "', '" + slide + "', " + str(
            set_no) + ")")

    # Add images for user with empty labels.
    # 1) Get images
    images = conn.execute(
        "SELECT imname FROM Pool_Table WHERE slide = '" + slide + "' AND slide_set = " + str(set_no)).fetchall()

    # 2) add it to image_table
    for image in images:
        conn.execute(
            "INSERT INTO Image_Table (username, imname, slide, slide_set) VALUES('" + username + "', '" + image[
                0] + "', '" + slide + "', " + str(
                set_no) + ")")

    conn.commit()


def assign_sets_to_user(conn, username):
    slides = getslidess()
    # slides = ['F039']
    # slides = ['F039', 'F048', 'E952']
    for slide in slides:
        if (not check_slide_completed(conn, username, slide)):

            try:
                assign_next_set(conn, slide, username)
            except:
                assign_next_set(conn, slide, username)


@app.route("/register", methods=['POST'])  # Register
def create_new_user():
    user_data = request.json
    print("/register", "=" * 20, user_data)
    conn = get_db()
    user = conn.execute('SELECT * FROM User_Table WHERE username="' + user_data["username"] + '"').fetchall()
    if len(user) > 0:
        return jsonify({'response': 'failed',
                        'error': 'User already exist!'})
    else:
      # usernameact
        q = "INSERT INTO User_Table VALUES ('" + user_data['username'] + "', '" + user_data['password']+ "', '" + user_data['usernameact'] + "')"
        conn.execute(q)
        conn.commit()

        assign_sets_to_user(conn, user_data["username"])

        return jsonify({'response': 'success'})


@app.route("/login", methods=['POST'])  # Login
def login():
    user_data = request.json
    ver = open(dir_path + "/version.txt").read()[:-1]
    print("/login", "=" * 20, user_data)
    conn = get_db()
    user = conn.execute('SELECT * FROM User_Table WHERE username="' + user_data["username"] + '"').fetchall()
    if len(user) == 1:  # ==1 as measure to check sql injection
        password = user[0][1]
        # usernameact = user[0][2]
        if password == user_data["password"]:
            return jsonify({'response': 'success',
                            'version': ver,
                            'user': user[0][0],
                            'usernameact': user[0][2]
                            }
                           )
        else:
            return jsonify({'response': 'failed',
                            'version': ver,
                            'error': "Invalid Password!"})
    else:
        return jsonify({'response': 'failed',
                        'version': ver,
                        'error': "User doesn't exist!"})


@app.route("/login_admin", methods=['POST'])  # Login
def login_admin():
    user_data = request.json
    auth = open(dir_path + "/auth_key.txt").read()[:-1]

    print("/login_admin", "=" * 20, user_data)
    user = user_data["username"]
    if user == 'cb334' and "mghivf" == user_data["password"] and user_data["auth"] == auth:
        return jsonify({'response': 'success'})
    else:
        return jsonify({'response': 'failed'})


@app.route("/get_users", methods=['POST'])  # Login
def get_users():
    user_data = request.json
    auth = open(dir_path + "/auth_key.txt").read()[:-1]

    print("get_users", "=" * 20)
    users = []

    if user_data["auth"] == auth:
        conn = get_db()
        rv = conn.execute('SELECT * FROM User_Table')
        users = [_[0] for _ in rv]

    user_data = ""
    for user in users:
        user_data += user + ";"

    return jsonify({"data": user_data[:-1]})


@app.route("/get_image_list", methods=['POST'])  # Login
def get_image_list():
    user_data = request.json
    auth = open(dir_path + "/auth_key.txt").read()[:-1]

    print("get_users", "=" * 20)
    users = []

    if user_data["auth"] == auth:
        conn = get_db()
        rv = conn.execute(
            "SELECT imname, label FROM Image_Table where username = '" + user_data["username"] + "' and slide = '" +
            user_data["slide"] + "'")
        users = [str(_[0]) + ":" + str(_[1]) for _ in rv]

    user_data = ""
    for user in users:
        user_data += user + ";"

    return jsonify({"data": user_data[:-1]})


@app.route("/get_image_number", methods=['POST'])  # Get image Number
def get_image_number():
    time.sleep(0.1)
    conn = get_db()
    user_data = request.json
    print("/get_image_number", "=" * 20, user_data)

    username = user_data["username"]
    slide = user_data["slide"]

    # Get the latest set.
    set_no = conn.execute(
        "SELECT slide_set FROM Assigned_Table WHERE username = '" + user_data["username"] + "' AND slide = '" + slide +
        "' ORDER BY id DESC").fetchone()[0]

    # Get image for that slide_set and slide.
    empty_label_images = [_[0] for _ in conn.execute("SELECT imname FROM Image_Table WHERE username = '" + username +
                                                     "' AND slide_set = " + str(
        set_no) + " AND slide = '" + slide + "' AND label IS null AND discarded IS null").fetchall()]

    print("/get_image_number", "=" * 20, len(empty_label_images))

    if len(empty_label_images) == 0:
        # Check for if all sets are done
        # Ask user to try another slide
        all_empty_images = [_[0] for _ in conn.execute("SELECT imname FROM Image_Table WHERE username = '" + username +
                                                       "' AND label IS null AND discarded IS null").fetchall()]
        #  check_set(set_no,username,slide)
        if len(all_empty_images) == 0:
            assign_sets_to_user(conn, username)
            return jsonify({'response': 'completed'})
        else:
            return jsonify({'response': 'slide_completed'})
    else:
        # Send picture FROM empty label images
        return jsonify({'response': 'success', 'image_name': empty_label_images[0]})


@app.route("/get_image", methods=['POST'])
def get_image():
    image_data = request.json["image_name"]
    if image_data == "":
        abort(401)
    print("/get_image", "=" * 20, "'", image_data, "'")
    return send_file(image_path + image_data)


# APP ====================================================================================
@app.route("/get_app")
def send_app():
    print("get_app", "=" * 50)
    return send_file(dir_path + '/index.html')




@app.route("/give_label", methods=['POST'])
def give_label():
    conn = get_db()

    user_data = request.json
    print("/give_label", "=" * 20, user_data)
    username = user_data["username"]
    imname = user_data["image_name"]
    label = user_data['label']

    if imname == "" or username == "" or label == "":
        abort(401)

    id = conn.execute("SELECT id FROM Image_Table WHERE username = '" + username + "' AND imname = '" +
                      imname + "' ORDER BY id DESC").fetchone()[0]

    conn.execute("UPDATE Image_Table SET label = '" + str(label) + "' WHERE id = " + str(id))

    id_ = -1

    if int(user_data['label']) == -1:
        id_ = id
        conn.execute("INSERT INTO Flag_Table(id, username, image_name, comment) VALUES"
                     "(" + str(id_) + ", '" + user_data["username"] + "', '" + user_data["image_name"] + "', '" +
                     user_data["comment"] + ":-1')")

    conn.commit()
    return jsonify({'response': 'success', 'id': str(id_)})


@app.route("/update_label", methods=['POST'])
def update_label():
    conn = get_db()

    user_data = request.json
    print("/update_label", "=" * 20, user_data)
    username = user_data["username"]
    imname = user_data["image_name"]
    label = user_data['label']
    id = user_data['id']

    conn.execute("UPDATE Image_Table SET label = '" + str(label) + "' WHERE id = " + id)

    # delete FROM User_Table WHERE username='r'
    conn.execute("DELETE FROM Flag_Table WHERE id = " + str(id))

    if int(user_data['label']) == -1:
        conn.execute("INSERT INTO Flag_Table(id, username, image_name, comment) VALUES"
                     "(" + str(id) + ", '" + username + "', '" + imname + "', '" + user_data["comment"] + "')")

    conn.commit()

    return jsonify({'response': 'success', 'id': str(user_data['id'])})


@app.route("/get_history", methods=['POST'])
def get_history():
    conn = get_db()

    user_data = request.json
    print("/get_history", "=" * 20, user_data)
    username = user_data["username"]
    slide = user_data["slide"]

    if username == "" or slide == "":
        abort(401)

    set_no = conn.execute(
        "SELECT slide_set FROM Assigned_Table WHERE username = '" + user_data[
            "username"] + "' AND slide = '" + slide + "' ORDER BY id DESC").fetchone()[0]
    # print("/get_history","="*20,set_no)

    countQ = conn.execute("SELECT * FROM Image_Table WHERE username = '" + username + "' AND slide_set = " + str(
        set_no) + " AND slide = '" + slide +
                          "' AND label IS NOT null AND discarded IS null ORDER BY id DESC").fetchall()
    # (id, username, imname, set, label, discarded)

    history = ""

    for _ in countQ[:20]:
        history += str(_[0]) + ":" + _[2] + ":" + str(_[5]) + ";"

    history = history[:-1]
    # print("/get_history", "=" * 20, history, "Size:", len(history.split(';')))
    return jsonify({"data": history})


@app.route("/get_stats", methods=['POST'])
def get_stats():
    user_data = request.json
    print("/get_stats", "=" * 20, user_data)
    # slides = ['F039', 'F048', 'E952']
    #    slides = ['s12015a', 's12015b', 's22015a', 's22015b', 's12016a', 's12016b', 's22016a', 's22016b', '2017a', '2017b']
    slides = getslidess()
    selected_user = user_data["username"]
    set_size = 250

    conn = get_db()

    ga = {}
    rows = conn.execute("SELECT slide, GA FROM Slide_Table").fetchall()
    for i in rows:
        ga[i[0]] = i[1]

    rows = conn.execute(
        "SELECT slide, count(*) FROM IMAGE_TABLE WHERE username = '" + selected_user + "' AND label IS NOT NULL GROUP BY slide, slide_set").fetchall()
    completed = {}
    for slide in slides:
        completed[slide] = 0
    for i in rows:
        completed[i[0]] = i[1] / set_size
    print(completed)

    try:
        conn.execute("DROP VIEW FINISHED_SETS")
        conn.execute("DROP VIEW FILTERED_IMAGE_TABLE")
        conn.execute("DROP VIEW COUNT_GOOD")
        conn.execute("DROP VIEW COUNT_OTHER")
        conn.execute("DROP VIEW MERGED_COUNT")


    except:
        pass

    conn.execute(
        "CREATE VIEW FINISHED_SETS AS SELECT username, slide, slide_set FROM Image_Table WHERE label is not null and label is not -1 and discarded is null GROUP BY username, slide, slide_set HAVING count(*)>=20").fetchall()
    conn.execute(
        "CREATE VIEW FILTERED_IMAGE_TABLE AS SELECT * FROM FINISHED_SETS, IMAGE_TABLE WHERE FINISHED_SETS.username = IMAGE_TABLE.username AND FINISHED_SETS.slide = IMAGE_TABLE.slide AND FINISHED_SETS.slide_set = IMAGE_TABLE.slide_set").fetchall()

    conn.execute(
        "CREATE VIEW COUNT_GOOD AS SELECT slide, username, count(*) CNT FROM FILTERED_IMAGE_TABLE WHERE label = 0 AND discarded is NULL GROUP BY slide, username")
    conn.execute(
        "CREATE VIEW COUNT_OTHER AS SELECT slide, username, count(*) CNT "
        "FROM FILTERED_IMAGE_TABLE "
        "WHERE label <> -1 and label <> 4 and label IS NOT null "
        "AND discarded IS NULL GROUP BY slide, username")

    conn.execute(
        "CREATE VIEW MERGED_COUNT AS SELECT COUNT_GOOD.slide, COUNT_GOOD.username, COUNT_GOOD.CNT, COUNT_OTHER.CNT FROM COUNT_GOOD, COUNT_OTHER WHERE COUNT_GOOD.slide = COUNT_OTHER.slide AND COUNT_GOOD.username = COUNT_OTHER.username")
    rows = conn.execute("SELECT * FROM MERGED_COUNT").fetchall()

    lab_avgs = {}
    lab_stddev = {}
    user_avg = {}
    for s in slides:
        users_avs = {}
        for row in rows:
            if row[0] == s:
                users_avs[row[1]] = row[2] / (row[2] + row[3])
        try:
            user_avg[s] = users_avs[selected_user]
            lab_avgs[s] = np.mean(list(users_avs.values()))
            lab_stddev[s] = np.std(list(users_avs.values()))
        except:
            user_avg[s] = 0
            lab_avgs[s] = 0
            lab_stddev[s] = 0

    to_send = ""
    for s in slides:
        to_send += str(ga[s]) + ":" + "%.2f %%(sd= %.2f %%)" % (
            lab_avgs[s] * 100, lab_stddev[s] * 100) + ":" + "%.2f" % (
                           user_avg[s] * 100) + " %:" + "%.2f" % (completed[s] * 100) + " %;"

    return jsonify({"data": to_send[:-1]})


@app.route("/get_stats2", methods=['POST'])
def get_stats2():
    slides = getslidess()
    #    slides = ['s12015a', 's12015b', 's22015a', 's22015b', 's12016a', 's12016b', 's22016a', 's22016b', '2017a', '2017b']
    # slides = ['F039', 'F048', 'E952']
    user_data = request.json
    username = user_data["username"]

    print("/get_stats", "=" * 20, user_data)
    conn = get_db()

    users = conn.execute("SELECT username FROM User_Table").fetchall()

    to_send_data = ""
    for slide in slides:
        slide_avg = 0
        username_avg = 0

        no_sets = conn.execute("SELECT mcount FROM Slide_Table WHERE slide ='" + slide + "'").fetchone()[0]
        lab_sets_completed = 0
        user_sets_completed = 0
        avgs_ = []
        std_slide = 0

        for set_no in range(1, no_sets + 1):
            set_avg = 0

            for user in users:
                user_good_count = conn.execute(
                    "SELECT count(*) FROM Image_Table WHERE username = '" + user[0] + "' AND slide_set = " + str(
                        set_no) + " AND slide = '" + slide +
                    "' AND label like '0' AND discarded IS null ORDER BY id DESC").fetchone()[0]
                user_total_count = conn.execute(
                    "SELECT count(*) FROM Image_Table WHERE username = '" + user[0] + "' AND slide_set = " + str(
                        set_no) + " AND slide = '" + slide +
                    "' AND label not like '4' AND discarded IS null ORDER BY id DESC").fetchone()[0]

                if not user_total_count == 0:
                    avg = user_good_count / user_total_count
                    set_avg += avg
                    lab_sets_completed += 1
                    if user[0] == username:
                        username_avg = avg
                        user_sets_completed += 1

            slide_avg += (set_avg / len(users))
            avgs_.append(slide_avg * 100)

        current_set_no = \
            conn.execute("SELECT slide_set FROM Assigned_Table WHERE username = '" + user_data["username"] +
                         "' AND slide = '" + slide + "' ORDER BY id DESC").fetchone()[0]

        images_in_set = conn.execute(
            "SELECT count(*) FROM Image_Table WHERE username = '" + username + "' AND slide_set = " + str(
                current_set_no) +
            " AND slide = '" + slide + "' AND discarded IS null ORDER BY id DESC").fetchone()[0]
        completed = conn.execute(
            "SELECT count(*) FROM Image_Table WHERE username = '" + username + "' AND slide_set = " + str(
                current_set_no) +
            " AND slide = '" + slide + "' AND label is not null AND discarded IS null ORDER BY id DESC").fetchone()[
                        0] / images_in_set

        try:
            slide_avg /= lab_sets_completed
            username_avg /= user_sets_completed
            std_slide = np.std(np.array(avgs_))
        except:
            pass

        ga = conn.execute("SELECT GA FROM Slide_Table WHERE slide ='" + slide + "'").fetchone()[0]

        # to_send_data += str(ga) + " %:" + str(slide_avg * 100)[:5] + " %:" + str(username_avg * 100)[:5] + " %:" + str(completed * 100)[:5] + " %:0 %" + ";"
        to_send_data += str(ga) + " %:" + "%.2f (std dev= %.2f %%)" % (
            slide_avg * 100, std_slide * 100) + ":" + "%.2f" % (username_avg * 100) + " %:" + "%.2f" % (
                                completed * 100) + " %;"
    return jsonify({"data": to_send_data[:-1]})


@app.route("/get_flags", methods=['POST'])
def get_flags():
    user_data = request.json
    print("/get_flag", "=" * 20, user_data)
    conn = get_db()
    flag_query = conn.execute(
        "SELECT * FROM Flag_Table WHERE username='" + user_data['username'] + "' ORDER BY id desc").fetchall()
    flags = ''
    # [id, username, image_name, comment]
    if len(flag_query) == 0:
        return jsonify({'response': 'empty'})
    for _ in flag_query:
        flags += str(_[0]) + ':' + _[2] + ":" + _[3] + ';'
    flags = flags[:-1]
    return jsonify({'response': 'success', 'data': flags})


@app.route("/reset_slide", methods=['POST'])
def reset_slide():
    user_data = request.json
    print("/rest_slide", "=" * 20, user_data)

    conn = get_db()
    username = user_data["username"]
    slide = user_data["slide"]
    check_reset(conn, username, slide)

    conn.execute(
        "UPDATE Image_Table SET discarded = 'true' WHERE username LIKE '" + username + "' and slide LIKE '" + slide + "'")

    if (not username == "" and not slide == ""):
        set_no, max_c = conn.execute("SELECT counter, mcount FROM Slide_Table WHERE slide = '" + slide + "'").fetchone()
        if set_no + 1 > max_c:
            conn.execute("UPDATE Slide_Table SET counter = 1 WHERE slide = '" + slide + "'")
        else:
            conn.execute("UPDATE Slide_Table SET counter = " + str(set_no + 1) + " WHERE slide = '" + slide + "'")
        conn.commit()

        conn.execute("Delete from Assigned_Table where  username ='" + username + "' and  slide = '" + slide + "'")

        # Set the same in assigned table
        conn.execute(
            "INSERT INTO Assigned_Table (username, slide, slide_set) VALUES('" + username + "', '" + slide + "', " + str(
                set_no) + ")")

        # Add images for user with empty labels.
        # 1) Get images
        images = conn.execute(
            "SELECT imname FROM Pool_Table WHERE slide = '" + slide + "' AND slide_set = " + str(set_no)).fetchall()

        # 2) add it to image_table
        for image in images:
            conn.execute(
                "INSERT INTO Image_Table (username, imname, slide, slide_set) VALUES('" + username + "', '" + image[
                    0] + "', '" + slide + "', " + str(
                    set_no) + ")")

        conn.commit()
    return jsonify({'response': 'success'})


def check_reset(conn, username, slide):
    images = conn.execute(
        "Select imname from Image_Table where  username ='" + username + "' and  slide = '" + slide + "'and  discarded = 'true' ").fetchall()
    conn.commit()

    if (len(images) == 0):
        return
    else:
        conn.execute(
            "Delete from Image_Table where  username ='" + username + "' and  slide = '" + slide + "'and  discarded = 'true' ")
        conn.commit()


with app.app_context():
    conn = get_db()
    print("-" * 100)
    # print( caluclate_accuracy('3','Sneha','F109'))

    rv = conn.execute('SELECT * FROM User_Table')
    # caluclate_accuracy('3','Sneha','F109')

    [print(_) for _ in rv]

if __name__ == "__main__":
    # context = ('certificate.crt', 'ssl.key')
    # app.run(host='0.0.0.0', port=5000, ssl_context=context)
    app.run(host='0.0.0.0', port=8000,debug=True)
