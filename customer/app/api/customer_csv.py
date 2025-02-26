from .. import ipss_db, db_client
import numpy as np
import pandas as pd
from flask import request
from flask_restx import Resource
from ipss_utils.decorators import login_required
from ..models.customer import Customer
from ..routes.customer import csv_customer_api_route, customer_bulk_read_response
from ..api_doc import form_fields


# customer csv upload api
@csv_customer_api_route.route('/')
class CustomerBulk(Resource):

    @login_required()
    @csv_customer_api_route.expect(customer_bulk_read_response)
    def put(self):
        data = request.json
        data = data.get('data')
        print(data)

        result = ipss_db.bulk_upload(model=Customer, data=data, db_client=db_client)
        db_client.session.commit()
        print("RESULT", result)
        return result

    ###
    @login_required()
    @csv_customer_api_route.doc(params=form_fields)
    def post(self):
        """
        Create Bulk record and return inserted id
        :return:
        """
        link = request.files['File']

        bk_data = pd.read_csv(link)
        print("BK")
        data1 = bk_data.rename(
            columns={'Type (Individual or Organization)': 'customer_type',
                     'Customer Name': 'customer_name',
                     'Organization Name': 'organization_name',
                     'Mobile Number': 'mobile_no',
                     'Additional Mobile Number': 'additional_mobile_no',
                     'Email Id': 'email',
                     'Additional Email Id': 'additional_email',
                     'Job Position': 'job_position',
                     'Website': 'website',
                     'Industry Type': 'industry_type',
                     'Address': 'address',
                     'City': 'city',
                     'State': 'state',
                     'Pincode': 'pincode' if 'Pincode' else 0,
                     'Source': 'source_csv',
                     'PAN': 'pan',
                     'GST Number': 'gst',
                     'Business Segment': 'tag',
                     'Description': 'description'

                     },
            inplace=False)
        data2 = data1.replace(np.nan, '', regex=True)
        data2 = data2.to_dict()
        length = len(data2['customer_type'])
        bulk_data = []
        for i in range(length):
            record = {
                'customer_type': data2['customer_type'][i],
                'customer_name': data2['customer_name'][i] if data2['customer_name'][i] else None,
                'organization_name': data2['organization_name'][i] if data2['organization_name'][i] else None,
                'mobile_no': data2['mobile_no'][i] if data2['mobile_no'][i] else None,
                'additional_mobile_no': data2['additional_mobile_no'][i] if data2['additional_mobile_no'][i] else None,
                'email': data2['email'][i] if data2['email'][i] else None,
                'additional_email': data2['additional_email'][i] if data2['additional_email'][i] else None,
                'job_position': data2['job_position'][i] if data2['job_position'][i] else None,
                'website': data2['website'][i] if data2['website'][i] else None,
                'industry_type': data2['industry_type'][i] if data2['industry_type'][i] else None,
                'address': data2['address'][i] if data2['address'][i] else None,
                'city': data2['city'][i] if data2['city'][i] else None,
                'state': data2['state'][i] if data2['state'][i] else None,
                'pincode': data2['pincode'][i] if data2['pincode'][i] else 0,
                'source_csv': data2['source_csv'][i] if data2['source_csv'][i] else None,
                'pan': data2['pan'][i] if data2['pan'][i] else None,
                'gst': data2['gst'][i] if data2['gst'][i] else None,
                'tag': data2['tag'][i] if data2['tag'][i] else None,
                'description': data2['description'][i] if data2['description'][i] else None
            }
            bulk_data.append(record)

        # response = Customer.post(self, bulk_data)
        return {'data': bulk_data}