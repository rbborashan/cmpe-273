# -*- coding: utf-8 -*-
import boto3

def handler(event, context):

    	table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')

        table.put_item(Item=event)

        return {}
