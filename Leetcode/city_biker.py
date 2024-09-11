"""City Biker needs to return the highest altitude of a point."""

n=int(input())
gain_loss_speed=[]
for i  in range(n):
    gain_loss_speed.append(int(input()))

biker_speed=0
maximum=0

for i in gain_loss_speed:
  biker_speed=biker_speed+i
  if maximum<biker_speed:
    maximum=biker_speed

print(maximum)