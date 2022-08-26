print("import")
from sqlalchemy import create_engine
import pandas as pd
print("engine")
engine = create_engine(
    'postgresql+psycopg2://root:root@localhost/postgres')

print("select vw_artist")
sql = '''
select * from vw_artist;
'''
df_artist =  pd.read_sql_query(sql,engine)

print("\n\ndf_artist")
print(df_artist)




# df_song = pd.read_sql_query('select * from vw_song;',engine)

#print("\n\tdf_song\n",df_song)

sql = '''
insert into tb_artist (
SELECT t1."date"
	,t1."rank"
	,t1.artist
	,t1.song 
FROM PUBLIC."Billboard" AS t1 
where t1.artist like 'Nirvana'
order by t1.artist, t1.song , t1."date" 
);

'''


engine.execute(sql)
