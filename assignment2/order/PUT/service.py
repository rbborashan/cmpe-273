# -*- coding: utf-8 -*-
import boto3
from time import strftime

def handler(event, context):

        menu_table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')
        order_table = boto3.resource('dynamodb', region_name='us-west-2').Table('Order')

        menu_id = order_table.get_item(Key={'order_id': event['order_id']}).get('Item').get('menu_id')
        selections = dict(enumerate(menu_table.get_item(Key={'menu_id': menu_id}).get('Item').get('selection'), 1))
        prices = dict(enumerate(menu_table.get_item(Key={'menu_id': menu_id}).get('Item').get('price')))
        sizes = dict(enumerate(menu_table.get_item(Key={'menu_id': menu_id}).get('Item').get('size'), 1))
        customer_name = order_table.get_item(Key={'order_id': event['order_id']}).get('Item').get('customer_name')
        customer_email = order_table.get_item(Key={'order_id': event['order_id']}).get('Item').get('customer_email')
        message = 'We have received your order. We will email you when it is ready.'

        # Return size selection
        if order_table.get_item(Key={'order_id': event['order_id']}).get('Item').get('order').get('selection') == 'none':
            order_table.delete_item(Key={'order_id': event['order_id']})
            order_table.put_item(
                Item = {
                    'order_id': event['order_id'],
                    'menu_id': menu_id,
                    'customer_name': customer_name,
                    'customer_email': customer_email,
                    'order': {
                        'selection': selections.get(int(event['input'])),
                        'size': 'none',
                        'costs': 'none',
                        'order_time': 'none',
                    }
                }
            )

            sizes = dict(enumerate(menu_table.get_item(Key={'menu_id': menu_id}).get('Item').get('size'), 1))
            choices = ''.join('{}. {} '.format(key, val) for key, val in sizes.items())
            message = 'Which size do you want?  ' + choices

        elif order_table.get_item(Key={'order_id': event['order_id']}).get('Item').get('order').get('size') == 'none':
            order_table.delete_item(Key={'order_id': event['order_id']})
            order_table.put_item(
                Item = {
                    'order_id': event['order_id'],
                    'menu_id': menu_id,
                    'customer_name': customer_name,
                    'customer_email': customer_email,
                    'order': {
                        'selection': selections.get(int(event['input'])),
                        'size': sizes.get(int(event['input'])),
                        'costs': str(prices.get(int(event['input']) - 1)),
                        'order_time': strftime("%a, %d %b %Y %H:%M:%S"),
                    }
                }
            )
            message = 'Your order costs ' + str(prices.get(int(event['input']) - 1)) + '. We will email you when the order is ready. Thank you!'

        return {'Message': message}
