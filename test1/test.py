import quopri

import base64


def test():
  ms= "http://localhost/mantisbt-2.22.1/verify.php?id=3D8&confirm_hash=3DOWLkLOudi=0OIZgbw04IXbjObToAmZ56MVzxL-ikrH-ifpJTv81L_fkzUAY68GcS98b89B9Ci20BhEolxJHT8"
  #msglines=ms.encode('utf-8')
  msgtext = quopri.decodestring(ms)
  ms2=msgtext.decode('utf-8')


  print(ms)