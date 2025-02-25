from flask_restx import fields
from ipss_utils.ipss_api_doc import list_api_params

customer_post_fields = {
    'customer_id': fields.Integer,
    'customer_type': fields.String,
    'user_id': fields.Integer,
    'module_type': fields.String,
    'organization_name': fields.String,
    'industry_type': fields.String,
    'mobile_no': fields.String,
    'email': fields.String,
    'compcode': fields.Integer,  # New field for asset management
    'type': fields.String,  # New field for asset management (string conversion field)
    'service_provider': fields.Boolean,  # New field for asset management
    'additional_mobile_no': fields.String,
    'additional_email': fields.String,
    'website': fields.String,
    'description': fields.String,
    'source': fields.Integer,
    'source_csv': fields.String,
    'customer_type_csv': fields.String,
    'address': fields.String,
    'city': fields.String,
    'state': fields.String,
    'pincode': fields.Integer,
    'gst': fields.String,
    'category': fields.String,  # (string conversion field)
    'customer_group': fields.String,  # (string conversion field)
    # 'cat_id': fields.Integer,
    'tag': fields.List(fields.String(), required=False, default=["tag", "tag"]),
    'country': fields.String,
    'customer_name': fields.String,
    'upload_logo': fields.String,
    'organization_name_map': fields.String,
    'job_position': fields.String,
    'pan': fields.String,
    'lead_category': fields.String,
    'category_name_asset': fields.String,
    'type_name_asset': fields.String,
    'modified_by': fields.String,
    'modified_on': fields.String,
    'created_by': fields.String,
    'created_on': fields.String,
    'deleted': fields.Boolean,
    'deleted_at': fields.String
}

customer_list_fields = {
    'customer_id': fields.Integer,
    'customer_type': fields.String,
    'user_id': fields.Integer,
    'organization_name': fields.String,
    'industry_type': fields.String,
    'mobile_no': fields.String,
    'email': fields.String,
    'compcode': fields.Integer,  # New field for asset management
    'type': fields.String,  # New field for asset management
    'service_provider': fields.Boolean,  # New field for asset management
    'additional_mobile_no': fields.String,
    'additional_email': fields.String,
    'website': fields.String,
    'description': fields.String,
    'source': fields.String,
    # 'source_name': fields.String,
    'source_csv': fields.String,
    'customer_type_csv': fields.String,
    'address': fields.String,
    'city': fields.String,
    'state': fields.String,
    'pincode': fields.Integer,
    'gst': fields.String,
    'category': fields.String,
    'customer_group': fields.String,
    'country': fields.String,
    # 'cat_id': fields.Integer,
    # 'cat_name': fields.String,
    'customer_name': fields.String,
    'upload_logo': fields.String,
    'organization_name_map': fields.String,
    'job_position': fields.String,
    'pan': fields.String,
    'lead_category': fields.String,
    'category_name_asset': fields.String,
    'type_name_asset': fields.String,
    'modified_by': fields.String,
    'modified_on': fields.String,
    'created_by': fields.String,
    'created_on': fields.String,
    'deleted': fields.Boolean,
    'deleted_at': fields.String
}
# csv
form_fields = {
    "File": {
        "name": "file",
        "in": "formData",
        "description": "file to upload",
        "required": False,
        "type": "file"

    }
}

# For Filtering
type_list_request = {
    **list_api_params,
    'type_name': {
        'type': 'string',
        'description': "for asset(vendor or service provider)"
    }
}
