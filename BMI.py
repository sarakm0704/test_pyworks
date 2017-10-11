while True:
	h = raw_input('How tall are you(m)?:')
	if len(h) == 0:
		break
	h = float(h)
	w = float(raw_input('How much do you weight(kg)?:'))
	bmi = w / pow(h,2)
	print('Your BMI is %0.1f' % bmi)
	if bmi < 18.5:
		print('Slim.')
	elif 18.5 <= bmi < 25.:
		print('Standard')
	elif 25.0 <= bmi < 30.:
		print('Little obsity.')
	else:
		print('high obsity.')
