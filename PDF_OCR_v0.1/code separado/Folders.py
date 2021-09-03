import os
# wd = os.getcwd()

# print ("El working directory que estoy usando es %s" % wd)

# proyecto = "C:/Users/34604/Documents/GitHub/PDF_OCR_v0.1"
# carpetatemp = "Tmp"
# path = os.path.join(proyecto, carpetatemp)
#
#
# access_rights = 0o755
#
# try:
#     os.mkdir(path, access_rights)
# except OSError:
#     print ("Creation of the directory %s failed" % path)
# else:
#     print ("Successfully created the directory %s" % path)

proyecto = "C:/Users/34604/Documents/GitHub/PDF_OCR_v0.1"
carpetatemp = "Tmp"
path = os.path.join(proyecto, carpetatemp)

try:
    os.rmdir(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)