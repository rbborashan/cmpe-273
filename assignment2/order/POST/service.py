# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

        menu_table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')
        order_table = boto3.resource('dynamodb', region_name='us-west-2').Table('Order')

        order_table.put_item(
            Item = {
                'order_id': event['order_id'],
                'menu_id': event['menu_id'],
                'customer_name': event['customer_name'],
                'customer_email': event['customer_email'],
                'order': {
                    'selection': 'none',
                    'size': 'none',
                    'costs': 'none',
                    'order_time': 'none',
                }
            }
        )

        items = menu_table.get_item(Key={'menu_id': event['menu_id']}).get('Item').get('selection')
        selections = dict(enumerate(items, 1))

        choices=''.join('{}. {} '.format(key, val) for key, val in selections.items())

        message = 'Hi ' + event['customer_name'] + ', please choose one of these selections:  ' + choices

        return {'Message': message}
