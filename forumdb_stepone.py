import psycopg2

DBNAME  ="forum" 

def get_posts():
    """return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c.execute("select content, time from posts order by time desc")
    db.close()
    return c.fetchall()
    
def add_posts(content):
    """Add a post to the 'database' with the current timestamp."""
    db= psycopg2.connect(database=DBNAME)
    c=db.cursor()
    #c.execute("insert into posts values ('%s')" % content) this is old code susceptible to injection attack
    c.execute("insert into posts values (%s)" ,(content,)) 
    db.commit()
    db.close()


