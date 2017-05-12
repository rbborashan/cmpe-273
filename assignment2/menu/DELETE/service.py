# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

    	table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')

        key = {}
        key['menu_id'] = event['menu_id']

        return {
            'statusCode': '200',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': table.delete_item(Key = key)
        }
