def limpiar_precios(precio):
    precio = str(precio).split(" ")[0].replace("$", "").replace(",", "").split("(Rebajado")[0]

    return precio.strip()

def limpiar_m2(m2):
    return m2.replace(" m2", "")

def limpiar_location(location):
    return location.replace("\n ", "")

def dir_checker(*args):
    import os

    DIRS = ['models', 'data']
    DIRS.extend(args)
    for d in DIRS:
        if os.path.exists(d):
            continue
        else:
            os.mkdir(d)
    
    print('DIRS checked')

def upload_df():
    import sqlalchemy
    database_username = db_data['database_username']
    database_password = db_data['database_password']
    database_ip = db_data['database_ip']
    database_name = db_data['database_name']
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
                                                        database_ip, database_name))


    database_connection.execute('drop table if exists tuhausdb.casas_vigente;')
    df_master_limpio.to_sql(con=database_connection, name='casas_vigente', if_exists='replace')
    df_master_limpio.to_sql(con=database_connection, name='casas_hist', if_exists='append')