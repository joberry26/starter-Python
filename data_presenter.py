
#question 1-3
cupcake_invoices = open('CupcakeInvoices.csv')
for data in cupcake_invoices:
  print(data)

cupcake_invoices.close()

#question 4
cupcake_invoices = open('CupcakeInvoices.csv')
for data in cupcake_invoices:
  flavor = data.strip('\n').split(',')
  print(flavor[2])

cupcake_invoices.close()

#question 5
cupcake_invoices = open('CupcakeInvoices.csv')
for data in cupcake_invoices:
  flavor = data.strip('\n').split(',')
  sum1 = flavor[3]
  sum2 = flavor[4]
  int_sum1 = int(sum1)
  int_sum2 = float(sum2)
  sum_total = int_sum1 + int_sum2
  print(sum_total)
 
cupcake_invoices.close()

#question 6 and 7
cupcake_invoices = open('CupcakeInvoices.csv')
cupcake_total = 0

for data in cupcake_invoices:
  flavor = data.strip('\n').split(',')
  sum1 = flavor[3]
  sum2 = flavor[4]
  int_sum1 = int(sum1)
  int_sum2 = float(sum2)
  sum_total = int_sum1 + int_sum2
  cupcake_total += sum_total
  

print(cupcake_total)

cupcake_invoices.close()

#Part 3
cupcake_invoices = open('CupcakeInvoices.csv')
cupcake_total = 0

chocolate_cupcakes = 0
vanilla_cupcakes = 0
strawberry_cupcakes = 0

for data in cupcake_invoices:
  flavor = data.strip('\n').split(',')
  sum1 = flavor[3]
  sum2 = flavor[4]
  int_sum1 = int(sum1)
  int_sum2 = float(sum2)
  sum_total = int_sum1 + int_sum2
  cupcake_total += sum_total
  
  selector = sum_total, flavor[2]

  for cupcaketotal in selector:
    if cupcaketotal == 'Chocolate':
     chocolate_cupcakes += selector[0]
    elif cupcaketotal == 'Vanilla':
      vanilla_cupcakes += selector[0]
    elif cupcaketotal == 'Strawberry':
      strawberry_cupcakes += selector[0]

  

print(f'chocolate cupcake total is {chocolate_cupcakes}!')
print(f'Vanilla cupcake total is {vanilla_cupcakes}!')
print(f'Strawberry cupcake total is {strawberry_cupcakes}!')
print(cupcake_total)

cupcake_invoices.close()
