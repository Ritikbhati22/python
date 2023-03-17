def game():
    return 100

score = game()
with  open("ritik.txt") as f:
 highrscore = int(f.read())

 if(score>highrscore):
    with open("ritik.txt",'w') as f:
       f.write(str(score))