import gspread
from chalice import Chalice

gc = gspread.service_account(filename = 'credentials.json')
sh = gc.open_by_key('1sTyqNxQrxBNxnAoU7N7l9jxPVnZKazQK_CNz0eYk0MM')
worksheet = sh.get_worksheet(0)
worksheet1 = sh.get_worksheet(1)
worksheet2 = sh.get_worksheet(2)

app = Chalice(app_name='final')

@app.route('/buy_stock', methods = ['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body
    
    data = [webhook_message['position'],
		webhook_message['close'],
		webhook_message['ticker'],
		webhook_message['position size'],
		webhook_message['time']
    ]

    
    if data[2] == "SPY":
        worksheet.append_row(data)
    elif data[2] == "QQQ":
        worksheet1.append_row(data)
    else:
        worksheet2.append_row(data)
    
    return {
        'message' : ' Finish',
        'webhook_message': webhook_message
    }