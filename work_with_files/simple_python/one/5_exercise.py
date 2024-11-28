


"""with try except"""
import os.path

# try:
#     file = open('files/value_starts.txt', 'r+')
#     value=file.readline()
#     file.seek(0)
#     file.write(str(int(value)+1))
#     file.close()
#
#
# except FileNotFoundError:
#     file = open('files/value_starts.txt', 'w')
#     file.write('1')
#     file.close()



#читай os.path
"""without try except"""
# if not os.path.exists('files/value_starts.txt'):
#     file = open('files/value_starts.txt', 'w+')
#     file.write('0')
#     file.close()
#
# file=open('files/value_starts.txt', 'r+')
# value=file.readline()
# file.seek(0)
# file.write(str(int(value)+1))
# file.close()




