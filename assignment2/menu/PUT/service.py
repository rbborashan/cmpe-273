# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

    	table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')

        table.update_item(
            Key = {'menu_id': event['menu_id']},
            UpdateExpression = 'SET selection = :val1',
            ExpressionAttributeValues = {':val1': event['selection']}
        )

        return {}
