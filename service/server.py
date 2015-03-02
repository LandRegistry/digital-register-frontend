#!/usr/bin/env python
from service import app
import os
from flask import Flask, abort, render_template
import requests

register_title_api = app.config['REGISTER_TITLE_API']

@app.route('/titles/<title_ref>', methods=['GET'])
def display_title(title_ref):
    api_response = get_register_title(title_ref)
    if api_response:
        title_api = api_response.json()
        proprietor_names = get_proprietor_names(title_api['data']['proprietors'])
        address_lines = get_address_lines(title_api['data']['address'])
        title = {
            'number': title_api['title_number'],
            'last_changed': title_api['data'].get('last_application_timestamp', 'No data'),
            'address_lines': address_lines,
            'proprietors': proprietor_names,
            'tenure': title_api['data'].get('tenure', 'No data')
        }
        return render_template('display_title.html', asset_path = '../static/', title=title)
    else:
        abort(404)

def get_register_title(title_ref):
    response = requests.get(register_title_api+'titles/'+title_ref)
    return response

def get_proprietor_names(proprietors_data):
    proprietor_names = []
    for proprietor in proprietors_data:
        name = proprietor['name']
        if 'forename' in name and 'surname' in name:
            proprietor_names += [{
                "name": name['forename'] + ' ' + name['surname']
            }]
        if 'non_private_individual_name' in name:
            proprietor_names += [{
                "name": name['non_private_individual_name']
            }]
    return proprietor_names

def get_address_lines(address_data):
    address_lines = []
    if address_data:
        first_line_address = ' '.join([address_data[k] for k in ['house_no', 'street_name'] if address_data.get(k, None)])
        all_address_lines = [
            first_line_address,
            address_data.get('town', ''),
            address_data.get('postcode', '')
        ]
        address_lines = [line for line in all_address_lines if line]
    return address_lines

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8003))
    app.run(host='0.0.0.0', port=port, debug=True)
