# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

    	table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')
        
        return {
            'status': '200',
            'body': table.put_item(Item=event),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
