for count in range(0,100):
  if count != 99:
    print("{}".format(str(count).zfill(2)) ,end=", ")
  else:
    print ("{}".format(count))
