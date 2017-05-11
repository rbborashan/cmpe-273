# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

    	table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')

        return {
            'status': '200',
            'body': table.get_item(Key=event).get('Item'),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
