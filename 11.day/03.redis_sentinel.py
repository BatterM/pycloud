# import redis
# import logging.config
# from redis import sentinel
#
# logging.config.fileConfig('e:\\development\\logconfig.conf')
# sentinel01=sentinel.Sentinel([('192.168.132.20',26379)])
#
# try:
#     master=sentinel01.discover_master('mymaster')
#     print(master)
# except Exception as error:
#     logging.getLogger('sentinellog')
#     logging.error(error)
# finally:
#     master=sentinel01.discover_master('mymaster')
#     if master !=('192.168.132.20',6381):
#         logging.warning('master on {}'.format(master))

