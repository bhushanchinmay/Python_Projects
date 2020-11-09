array = []

def stop_processing_42(number):
  if number != 42:
    array.append(number)
    return True
  else:
    return False

if __name__ == "__main__":
  stop = not False
  while stop:
    n = int(input())
    stop = stop_processing_42(n)
  for i in array:
    print(i)
		