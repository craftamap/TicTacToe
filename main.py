game = [[1,1,1],[1,-1,1],[1,-1,-1]]

def formatvalidator(g):
  if isinstance(g, list):
    if len(g) == 3:
      if len(g[0]) == 3 and len(g[1])==3 and len(g[2]) == 3:
        for i in g:
          for i2 in i:
            if isinstance(i2, int):
              if abs(i2) == 1 or i2 == 0:
                pass
              else:
                return False
            else:
              return False
        return True
      else:
        return False
    else:
      return False
  else:
    return False
    

def rulevalidator(g):
  countx = 0
  counto = 0
  count0 = 0
  
  for i in g:
    for i2 in i:
      if i2 == 1:
        countx += 1
      elif i2 == -1:
        counto+= 1
      elif i2 == 0:
        count0 +=1
      
  if countx == counto:
    return 1
  elif countx == counto +1:
    return -1
  elif countx < == counto
  elif count0 == 0:
    return True
  else:
    return False
  
    
    
print rulevalidator(game)

