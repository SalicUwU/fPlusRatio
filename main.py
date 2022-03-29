#!/bin/python3
from flask import Flask, request, render_template
from flask_api import status
from ipwhois import IPWhois
import country_converter as coco
import sys

if len(sys.argv) != 2:
    sys.exit("Please specify host ip")

else:
    hostname = sys.argv[1]

app = Flask(__name__)

@app.route("/")
def index():
    try:
        obj = IPWhois(request.remote_addr)
        results = obj.lookup_rdap()
            
        if results["asn_description"] == "None":
            sourceISP = "None"
            sourceCountry = results["asn_country_code"]

        elif results["asn_country_code"] == "None":
            sourceCountry = "None"
            sourceISP = results["asn_description"]
            sourceISP = sourceISP.removesuffix(", " + sourceCountry)

        elif (results["asn_country_code"]) and (results["asn_description"]) == "None":
            sourceISP = "None"
            sourceCountry = "None"

        else:
            sourceCountry = results["asn_country_code"]
            sourceISP = results["asn_description"]
            sourceISP = sourceISP.removesuffix(", " + sourceCountry)
            sourceIP = request.remote_addr

        iso2_codes = coco.convert(names=sourceCountry, to='name_short')

    except:
        sourceIP = request.remote_addr
        sourceISP = "Fuck if i know, ask your system admin"
        iso2_codes = "Local Internet System"
    
    return render_template("index.html", sourceIP=sourceIP, sourceCountry=iso2_codes, sourceISP=sourceISP)

@app.route("/lookup")
def lookup():
    try:
        obj = IPWhois(request.args.get("IP"))
        results = obj.lookup_rdap()

        if results["asn_description"] == "None":
            sourceISP = "None"
            sourceCountry = results["asn_country_code"]

        elif results["asn_country_code"] == "None":
            sourceCountry = "None"
            sourceISP = results["asn_description"]
            sourceISP = sourceISP.removesuffix(", " + sourceCountry)

        elif (results["asn_country_code"]) and (results["asn_description"]) == "None":
            sourceISP = "None"
            sourceCountry = "None"

        else:
            sourceCountry = results["asn_country_code"]
            sourceISP = results["asn_description"]
            sourceISP = sourceISP.removesuffix(", " + sourceCountry)
            sourceIP = request.args.get("IP")

        iso2_codes = coco.convert(names=sourceCountry, to='name_short')

    except:
        return "IP Argument was not supplied", status.HTTP_400_BAD_REQUEST

    return render_template("lookup.html", sourceIP=sourceIP, sourceCountry=iso2_codes, sourceISP=sourceISP)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host=hostname)