#! /usr/bin/env python3

import psycopg2
import time

DBNAME="news"

query1="select title, count(*) as num_views from articles, log where log.path = concat('/article/',articles.slug) group by articles.title order by num_views desc limit 3;"
query2="select name, num_views from authors, article_views where article_views.author = authors.id;"
query3="select time, perc from percent_error where perc >= 1;"


def poplular_article(query1):
    db = psycopg2.connect("database=DBNAME")
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    print(results)
    db.close()





