# from config import MySQLConfig
# import pymysql
# import re
#
# db = pymysql.connect(
#     host=MySQLConfig.host, port=MySQLConfig.port, user=MySQLConfig.user, password=MySQLConfig.password,
#     database=MySQLConfig.database, charset='utf8'
# )
#
# sql = '''
#     select id,image
#     from museum_items_of_china_v2
#     where image like 'https://www.nms.ac.uk/explore-our-collections/collection-search-results%'
# '''
# cursor = db.cursor()
#
# db.begin()
# res = cursor.execute(sql)
# results = cursor.fetchall()
#
# cnt = 0
# for i in results:
#     url = i[1]
#     match = re.search(r"(search.axd.*)", url)
#     try:
#         if match:
#             result = match.group(1)
#             new_url = 'https://www.nms.ac.uk/' + result
#             sql = f'''
#                 update museum_items_of_china_v2
#                 set image = '{new_url}'
#                 where id = {i[0]}
#             '''
#             cursor.execute(sql)
#             print(new_url)
#     except Exception:
#         print("nnonon")
#         db.rollback()
#
# db.commit()
a=[(1,2,3),(2,3,3)]
print('\n'.join([str(i) for i in a]))