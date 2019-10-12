import quopri

import base64
import re


def test():
  ms= "ntcn\n\nhttp://localhost/mantisbt-2.22.1/verify.php?id=3D8&confirm_hash=3DOWLkLOudi\n=0OIZgbw04IXbjObToAmZ56MVzxL-ikrH-ifpJTv81L_fkzUAY68GcS98b89B9Ci20BhEolxJHT8\n\nkdjfgk"
  b2=ms[ms.find("http://localhost"):]
 #b2 = re.search("http://localhost/\w\W*", ms).group(0)
  b4 = b2
  b3 = b2.split('\n\n')[0]
  b5=quopri.decodestring(b3)
  b6 = b5.decode('utf-8')
  b7=b6
  return b5


  print(ms)