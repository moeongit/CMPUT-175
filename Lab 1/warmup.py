bulbs_sale = {'daffodil': 0.35, 'tulip': 0.33, 'crocus': 0.25, 'hyacinth': 0.75, 'bluebell': 0.50}
mary_order = {'daffodil': 50, 'tulip': 100}
bulbs_sale['tulip'] = float('{0:.2f}'.format(bulbs_sale['tulip'] + bulbs_sale['tulip'] * (25/100)))
mary_order['hyacinth'] = 30
total_bulb = 0
total_cost = 0
print("You have purchased the following bulbs:")
for i,j in sorted(mary_order.items()):
    bulb_code = i[:3].upper()
    total_bulb+= j
    bulb_cost = j * bulbs_sale[i]
    total_cost += bulb_cost
    print("{0:<5s} *{1:>4d} = ${2:>6.2f}".format(bulb_code, j, bulb_cost))

print("Thank you for purchasing {0:d} bulbs from Bluebell GreenHouses.".format(total_bulb))
print("Your total comes to ${0:.2f}".format(total_cost))