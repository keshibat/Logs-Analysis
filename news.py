#!/usr/bin/env python

import psycopg2
import datetime

DBNAME = "news"

query1 = ("""SELECT title, count(*) AS num_views
           FROM articles, log
           WHERE log.path = concat('/article/',articles.slug)
           group by articles.title ORDER BY num_views DESC LIMIT 3;""")

query2 = ("""SELECT name, num_views FROM authors, article_views
           WHERE article_views.author = authors.id;""")

query3 = ("""SELECT date, perc FROM percent_error WHERE perc >= 1;""")


def popluar_article(query1):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    for t, v in results:
        print('"{0}" -- {1} views'.format(t, v))
    db.close()


def poplular_author(query2):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query2)
    results = c.fetchall()
    for t, v in results:
        print('"{0}" -- {1} views'.format(t, v))
    db.close()


def error_percent(query3):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query3)
    results = c.fetchall()
    for t, v in results:
        print("{} -- {:.1f}% errors".format(t.strftime("%B %d, %y"), v))
    db.close()


if __name__ == '__main__':
    print("The 3 most poplular articles of all time are:")
    popluar_article(query1)
    print("\n")
    print("The most popular article authors of all time are")
    poplular_author(query2)
    print("\n")
    print("Days did more than 1% of requests lead to errors")
    error_percent(query3)
