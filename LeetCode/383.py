a = ransomNote
      b= magazine
      seta= set(a)
      setb= set(b)
      flag =0
      if not a:
          if not b:
              return (True)
          else:
              return (True)
      else:
          for i in seta:
          # 	print (a.count(i))
            if a.count(i)<=b.count(i):
          # 		print ('true')
              flag = 1
            else:
          # 		print ('false')
              flag = 2
              break
          if flag == 1:
            return (True)
          elif flag ==2:
            return (False)
