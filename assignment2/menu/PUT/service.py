# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

    	table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')

        return {
            'status': '200',
            'body': table.update_item(
                        Key = event['key'],
                        UpdateExpression = 'SET selection = :val1',
                        ExpressionAttributeValues = {':val1': event['body']['selection']}
            ),
            'headers': {
                'Content-Type': 'application/json',
            }
        }
