import re

testing_list=['abc1234','abcd123.455abc','sdadasd123456dasdasdj12314','zxcnzvxv134.123vccmnv12345']

def get_numeric_value(str_value):
	result = []
	final_list=re.compile(r"\d+\.?\d{2}",re.S).findall(str_value)
	for final_value in final_list:
		if final_value.find('.') == -1:
			result.append(final_value+'.00')
		else:
			result.append(final_value)
	return result

for test_value in testing_list:
	print(f"test str: {test_value}, result is {','.join(get_numeric_value(test_value))}")