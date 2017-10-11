import MOREDICE

num = input('4,6,8,12,20. what is your choice?')
my_dice = MOREDICE.Dice(num)
cpu_dice = MOREDICE.Dice(num)

my_pip = my_dice.shoot()
cpu_pip = cpu_dice.shoot()

print('CPU : ' + str(cpu_pip) + ' YOU : ' + str(my_pip))

if my_pip > cpu_pip:
	print('Congratutaion! You win!')
elif my_pip < cpu_pip:
	print('Owww! You lose!')
else:
	print('Draw!')
