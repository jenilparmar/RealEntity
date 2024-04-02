@app.route('/view_order_details/<int:table_number>')
def view_order_details(table_number):
    print("Table Number:", table_number)
    
    # Find matching orders for the given table number
    matching_orders = order_collection.find({'table_number': table_number})
    list = []
    vangi = []
    sankhya = []
    bhav  =[]
    for item in matching_orders[0]['items'].items():
        list.append(item)
    for dish , quentity in list:
        vangi.append(dish)
        sankhya.append(quentity)
    
    x=0
    dc = {}
    for v in vangi:
        for i in item_collection.find():
            for j in i:
                if x==0:
                    x = 1
                    continue
                for k in i[j]:
                    if v in i[j]:
                        dc[v] = i[j][k]
            x=0    
    
    
    return render_template('OrderSuccess2.html', orders=matching_orders ,dc=dc)
