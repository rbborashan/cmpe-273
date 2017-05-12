# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

        table = boto3.resource('dynamodb', region_name='us-west-2').Table('Order')

        return table.get_item(Key=event).get('Item')
