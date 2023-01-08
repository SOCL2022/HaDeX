param name string
param location string = resourceGroup().location
param tags object = {}

@allowed([ 'Hot', 'Cool', 'Premium' ])
param accessTier string = 'Hot'
