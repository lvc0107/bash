import os

client = "Auth0 Management API"
if client == "Auth0 Management API":
    os.environ["CLIENT_ID"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    os.environ["CLIENT_SECRET"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxVSHEXbvfDr6x"
if client == "NatGeoTestApp":
    os.environ["CLIENT_ID"] = "xxxxxxxxxxxxxxxxxxx"
    os.environ["CLIENT_SECRET"] = "xxxxxxxxxxxxxxxxxxxxxxxxPL"
os.environ["DOMAIN"] = "https://domain-test.auth0.com"
os.environ["AUDIENCE"] = "https://domain-test.auth0.com/api/v2/"
os.environ["CONNECTION"] = "db"
