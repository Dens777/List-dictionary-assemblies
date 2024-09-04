first_strings=['Elon','Musk','Programmer','Monitors','Variable']
second_string=['Task','Git','Comprehension','Java','Computer','Assembler']

first_result=[len(x) for x in first_strings if len(x)>=5]
print(first_result)

second_result=[(a,b) for a in first_strings for b in second_string if len(a)==len(b)]
print(second_result)

third_result={c:len(c) for c in first_strings + second_string if len(c)%2==0}
print(third_result)

