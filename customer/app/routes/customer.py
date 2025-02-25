from flask_restx import Namespace, Resource, fields
from ..api_doc import  customer_post_fields,customer_list_fields
from ipss_utils.ipss_api_doc import create_record_response, update_record_response, list_response_model

# Initialize API routes
customer_api_route = Namespace('customer', path='/customer')

# List customer API docs
customer_model = customer_api_route.model('customer', {
    **customer_list_fields,
    "tag": fields.List(fields.String(), required=False, default=["tag", "tag"] if "tag" else []),
    'deleted': fields.Boolean,
    'created_on': fields.String,
    'modified_on': fields.String
})

customer_list_response = customer_api_route.model('customer_list_response', {
    **list_response_model,
    **{
        'results': fields.List(fields.Nested(customer_model))
    }
})
customer_bulk_read_response = customer_api_route.model('customer_bulk_read_response', {
    **{
        'data': fields.List(fields.Nested(customer_model))
    }
})

# Create customer model
create_customer_model = customer_api_route.model('create_customer', customer_post_fields)
create_customer_response = customer_api_route.model('create_customer_response', create_record_response)

# Get customer records model
get_customer_response = customer_api_route.model('get_customer_response', customer_post_fields)
# single get
get_single_response = customer_api_route.model('get_single_response', customer_post_fields)

# Update user record
update_customer_fields = customer_post_fields
update_customer_model = customer_api_route.model('update_customer', update_customer_fields)
update_customer_response = customer_api_route.model('update_customer_response', update_record_response)

# customer csv API routes
csv_customer_api_route = Namespace('customer/csv_upload', path='/customer/import-from-csv/upload')