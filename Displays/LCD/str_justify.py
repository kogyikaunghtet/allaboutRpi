str = "this is string example"
row = "Hello world"
num_cols=16
space = 20
print str.ljust(30, '0')
print str.rjust(30, '0')
print row.ljust(num_cols, '0')[:space]
print row.rjust(num_cols)[:space]
