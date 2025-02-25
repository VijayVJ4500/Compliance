import datetime
from flask import request
from flask_restx import Resource
from ipss_utils.ipss_db import query_to_dict
from sqlalchemy import text
from .. import ipss_db, db_client
from ipss_utils.ipss_api_doc import list_api_params

from ..api_doc import type_list_request, list_api_params
from ..models.customer import Customer
from ipss_utils.decorators import login_required
from ..routes.customer import customer_api_route, customer_list_response, create_customer_response, \
    update_customer_model, update_customer_response, get_single_response
from ..routes.customer import create_customer_model, get_customer_response

# Primary key name
primary_key = 'customer_id'


@customer_api_route.route('/')
class CustomerTagApi(Resource):
    per_page = 20

    @customer_api_route.marshal_with(customer_list_response)
    @customer_api_route.doc(params=list_api_params)
    @login_required()
    def get(self):
        """
        List of customers with pagination
        TODO: Search customer
        :return:
        """
        paged = int(request.args.get('paged')) if request.args.get('paged') else 1
        results_per_page = int(request.args.get('results_per_page')) if request.args.get(
            'results_per_page') else self.per_page
        offset = (paged - 1) * results_per_page
        current_user = request.args.get('current_user')
        print(current_user)
        compcode = current_user.get('compcode')
        sql_query_count = text("SELECT COUNT(customer.*) as total "
                               "FROM customer "
                               # "Left Join customercategory on customercategory.category_id = customer.cat_id "
                               f"WHERE customer.deleted IS NOT TRUE AND "
                               f"customer.customer_id IS NOT NULL and customer_type is not null "
                               )
        type_name = request.args.get('type')
        print("type", type_name)
        # sql_condition = ""
        # if type_name and type_name != "ALL":
        #     sql_condition += " customer.type = :type AND "
        sql_query = text("SELECT customer.*,"
                         "TRIM(customer.industry_type) as industry_type,"
                         "TRIM(customer.address) as address,"
                         "TRIM(customer.city) as city,"
                         "TRIM(customer.state) as state,"
                         # "customercategory.category_name as cat_name,"
                         # "customersource.source_name as source_name,"
                         "TRIM(customer.job_position) as job_position "
                         "FROM customer "
                         # "Left Join customercategory on customercategory.category_id = custo/mer.cat_id "
                         f"WHERE customer.deleted IS NOT TRUE AND "
                         f"customer.customer_id IS NOT NULL and customer_type is not null "
                         "ORDER BY customer.customer_id desc")

        results = query_to_dict(db_client.engine.execute(
            sql_query))
        print("RESULT", results)
        count_result = query_to_dict(db_client.engine.execute(
            sql_query_count))

        # tag post

        for i in results:
            if results[results.index(i)]['tag'] != None:
                results[results.index(i)]['tag'] = list(i.get('tag', None).split(","))
                my_list = results[results.index(i)]['tag']
                results[results.index(i)]['tag'] = [''.join(e for e in string if e.isalnum()) for string in my_list]
                print("str", results[results.index(i)]['tag'])

            else:
                results[results.index(i)]['tag'] = []

        return {
            'primary_key': primary_key,
            'total_results': count_result[0].get('total') if len(count_result) else 0,
            'page': paged,
            'results_per_page': results_per_page,
            'results': results
        }

    @customer_api_route.expect(create_customer_model)
    @customer_api_route.marshal_with(create_customer_response)
    @login_required(permission='vendor_asset.add||service_provider_asset.add')
    def post(self):
        """
        Create customer record and return inserted id
        :return:
        """
        data = request.json
        print("gomathi", data)
        # remove primary key if exists
        data.pop(primary_key, None)
        current_user = request.args.get('current_user')
        data = ipss_db.add_created_user(data, current_user)

        # Duplication check for email and mobile number
        data['email'] = data.get('email')
        data['mobile_no'] = data.get('mobile_no')
        data['pan'] = data.get('pan')
        data['gst'] = data.get('gst')
        email_query = text(
            "SELECT * FROM customer WHERE customer.email =:email AND deleted = false LIMIT 1")
        mobile_no_query = text(
            "SELECT * FROM customer WHERE customer.mobile_no =:mobile_no AND deleted = false LIMIT 1")
        pan_query = text(
            "SELECT * FROM customer WHERE customer.pan =:pan AND deleted = false LIMIT 1")
        gst_query = text(
            "SELECT * FROM customer WHERE customer.gst =:gst AND deleted = false LIMIT 1")

        email_detail = db_client.engine.execute(
            email_query,
            email=data['email']
        )
        mobile_no_detail = db_client.engine.execute(
            mobile_no_query,
            mobile_no=data['mobile_no']
        )
        pan_detail = db_client.engine.execute(
            pan_query,
            pan=data['pan']
        )
        gst_detail = db_client.engine.execute(
            gst_query,
            gst=data['gst']
        )
        email_result = query_to_dict(email_detail)
        mobile_no_result = query_to_dict(mobile_no_detail)
        pan_result = query_to_dict(pan_detail)
        gst_result = query_to_dict(gst_detail)
        # For title
        if data.get('type') != None:
            data["type"] = data.get('type').title()
            type_name = data.get('type')
            sql = text(
                'SELECT * from customer WHERE customer.type=:type AND deleted is not true')
            res = query_to_dict(db_client.engine.execute(sql, type=type_name))

        # Duplication check
        if len(email_result) and len(mobile_no_result) and len(pan_result) and len(gst_result):
            return {
                'success': False,
                'message': "User already exists.",
            }, 409
        # Duplication check for email
        elif len(email_result):
            return {
                'success': False,
                'message': "Email already exists.",
            }, 409
        # Duplication check for mobile number
        elif len(mobile_no_result):
            return {
                'success': False,
                'message': "Mobile number already exists.",
            }, 409
        elif len(pan_result):
            return {
                'success': False,
                'message': "The PAN number already exists.",
            }, 409
        elif len(gst_result):
            return {
                'success': False,
                'message': "GST number already exists.",
            }, 409
        else:

            result = ipss_db.insert_record(
                model=Customer,
                values=data
            )
            print("result", result)

        return ipss_db.created_response(
            result=result,
            message="Created successfully.",
            primary_key=primary_key
        )


@customer_api_route.route('/<customer_config_id>/')
class CustomerUpdateApi(Resource):
    @staticmethod
    def update_record(data, customer_config_id):
        data = request.json
        # remove primary key if exists
        data.pop(primary_key, None)
        current_user = request.args.get('current_user')
        print(current_user)
        user_id = current_user.get('userid')
        data = ipss_db.add_created_user(data, current_user)
        # Unique check in patch(Same id can accept the exists data by passing customer_config id)
        email = data.get('email')
        mobile_no = data.get('mobile_no')
        pan = data.get('pan')
        gst = data.get('gst')
        print(email)
        print(mobile_no)
        sql_email = text("SELECT email FROM customer WHERE email=:email and customer_id !=:id and deleted=false")
        sql_phone = text(
            "SELECT mobile_no FROM customer WHERE mobile_no=:mobile_no and customer_id != :id and deleted=false")
        sql_pan = text(
            "SELECT pan FROM customer WHERE pan=:pan and customer_id != :id and deleted=false")
        sql_gst = text(
            "SELECT gst FROM customer WHERE gst=:gst and customer_id != :id and deleted=false")
        email_result = query_to_dict(db_client.engine.execute(sql_email, email=email, id=customer_config_id))
        phone_result = query_to_dict(db_client.engine.execute(sql_phone, mobile_no=mobile_no, id=customer_config_id))
        pan_result = query_to_dict(db_client.engine.execute(sql_pan, pan=pan, id=customer_config_id))
        gst_result = query_to_dict(db_client.engine.execute(sql_gst, gst=gst, id=customer_config_id))
        print(sql_phone)
        print(sql_email)
        # For title
        if data.get('type') != None:
            data["type"] = data.get('type').title()
            type_name = data.get('type')
            sql = text(
                'SELECT * from customer WHERE customer.type=:type AND deleted is not true')
            res = query_to_dict(db_client.engine.execute(sql, type=type_name))
        if len(phone_result) and len(email_result) and len(pan_result) and len(gst_result):
            return {
                'success': False,
                'message': 'User already exists.'
            }, 409
        elif len(phone_result):

            return {
                'success': False,
                'message': 'Mobile number already exists.'
            }, 409
        elif len(email_result):

            return {
                'success': False,
                'message': 'Email already exists.'
            }, 409
        elif len(pan_result):

            return {
                'success': False,
                'message': 'PAN number already exists.'
            }, 409
        elif len(gst_result):

            return {
                'success': False,
                'message': 'GST number already exists.'
            }, 409

        else:
            result = ipss_db.update_record(
                model=Customer,
                condition=Customer.customer_id == customer_config_id,
                values=data
            )
            return result

        # return ipss_db.created_response(
        #     result=result,
        #     message="User updated successfully.",
        #     primary_key=primary_key
        # )

    @customer_api_route.marshal_with(get_customer_response)
    @login_required(permission='vendor_asset.view||service_provider_asset.view')
    def get(self, customer_config_id):
        """
        Read user record / single record
        :param customer_config_id:
        :return:
        """

        query = text("SELECT customer.*,"
                     "TRIM(customer.industry_type) as industry_type,"
                     "TRIM(customer.address) as address,"
                     "TRIM(customer.city) as city,"
                     "category_mast.category_name as category_name_asset,"
                     "category_detail.sub_category_name as type_name_asset,"
                     # "customercategory.category_name as cat_name,"
                     # "customersource.source_name as source_name,"
                     "TRIM(customer.state) as state,"
                     "TRIM(customer.job_position) as job_position "
                     "FROM customer "
                     "LEFT JOIN category_mast on CAST(customer.category as int) = category_mast.category_id "
                     "LEFT JOIN category_detail on customer.source = category_detail.sub_category_id "
                     "WHERE customer.customer_id =:id")
        results = query_to_dict(db_client.engine.execute(query, id=customer_config_id))

        # tag post
        for i in results:
            if results[results.index(i)]['tag'] != None:
                results[results.index(i)]['tag'] = list(i.get('tag', None).split(","))
                my_list = results[results.index(i)]['tag']
                results[results.index(i)]['tag'] = [''.join(e for e in string if e.isalnum()) for string in my_list]
                print("str", results[results.index(i)]['tag'])

            else:
                results[results.index(i)]['tag'] = []

        if results != None:
            response = results[0]
        else:
            response = None
        return response

    @customer_api_route.expect(update_customer_model)
    @customer_api_route.marshal_with(update_customer_response)
    @login_required(permission='vendor_asset.edit||service_provider_asset.edit')
    def put(self, customer_config_id):
        """
        Update customer record
        :return:
        """
        data = request.json
        response = self.update_record(data, customer_config_id)
        return response

    @customer_api_route.expect(update_customer_model)
    @customer_api_route.marshal_with(update_customer_response)
    @login_required(permission='vendor_asset.edit||service_provider_asset.edit')
    def patch(self, customer_config_id):
        """
        Partial Update customer record
        :return:
        """
        data = request.json
        # remove primary key if exists
        data.pop(primary_key, None)

        response = self.update_record(data, customer_config_id)
        return response

    @customer_api_route.marshal_with(update_customer_response)
    @login_required(permission='vendor_asset.delete||service_provider_asset.delete')
    def delete(self, customer_config_id):
        """
        Soft delete customer record
        TODO: Make soft delete
        :return:
        """
        result = ipss_db.update_record(
            model=Customer,
            condition=Customer.customer_id == customer_config_id,
            values={
                'deleted': True,
                'deleted_at': datetime.datetime.now()
            }
        )
        # If customer_id deleted then the kanban data should be deleted which contains customer data
        might = text("UPDATE kanbanboard SET deleted=True where customer_map_id=:id")
        db_client.engine.execute(might, id=customer_config_id)
        return result


# For Asset management
@customer_api_route.route('/asset')
class ASSETApi(Resource):
    per_page = 20

    @customer_api_route.marshal_with(customer_list_response)
    @customer_api_route.doc(params=type_list_request)
    @login_required(permission='vendor_asset.list||service_provider_asset.list')
    def get(self):
        """
        List of customers with pagination
        TODO: Search vendor/service_provider
        :return:
        """
        paged = int(request.args.get('paged')) if request.args.get('paged') else 1
        results_per_page = int(request.args.get('results_per_page')) if request.args.get(
            'results_per_page') else self.per_page
        offset = (paged - 1) * results_per_page
        current_user = request.args.get('current_user')
        print(current_user)
        compcode = current_user.get('compcode')
        type_name = request.args.get('type_name')
        print("type", type_name)
        sql_condition = ""
        if type_name and type_name != "ALL":
            sql_condition += " and (customer.type = :type_name or customer.type is null) "
        sql_query_count = text("SELECT COUNT(customer.*) as total "
                               "FROM customer "
                               # "Left Join customercategory on customercategory.category_id = customer.cat_id "
                               f"WHERE customer.deleted IS NOT TRUE {sql_condition} and customer_type is null "
                               )

        sql_query = text("SELECT customer.*,"
                         "TRIM(customer.industry_type) as industry_type,"
                         "TRIM(customer.address) as address,"
                         "TRIM(customer.city) as city,"
                         "TRIM(customer.state) as state,"
                         "category_mast.category_name as category_name_asset,"
                         "category_detail.sub_category_name as type_name_asset,"
                         # "customercategory.category_name as cat_name,"
                         # "customersource.source_name as source_name,"
                         "TRIM(customer.job_position) as job_position "
                         "FROM customer "
                         # "Left Join customercategory on customercategory.category_id = custo/mer.cat_id "
                         # "Left Join customersource on customersource.source_id = customer.source "
                         "LEFT JOIN category_mast on CAST(customer.category as int) = category_mast.category_id "
                         "LEFT JOIN category_detail on customer.source = category_detail.sub_category_id "
                         f"WHERE customer.deleted IS NOT TRUE {sql_condition} and customer_type is null "
                         "ORDER BY customer.created_on desc")

        results = query_to_dict(db_client.engine.execute(
            sql_query, type_name=type_name))
        print("RESULT", results)
        count_result = query_to_dict(db_client.engine.execute(
            sql_query_count, type_name=type_name))

        # tag post

        for i in results:
            if results[results.index(i)]['tag'] != None:
                results[results.index(i)]['tag'] = list(i.get('tag', None).split(","))
                my_list = results[results.index(i)]['tag']
                results[results.index(i)]['tag'] = [''.join(e for e in string if e.isalnum()) for string in my_list]
                print("str", results[results.index(i)]['tag'])

            else:
                results[results.index(i)]['tag'] = []

        return {
            'primary_key': primary_key,
            'total_results': count_result[0].get('total') if len(count_result) else 0,
            'page': paged,
            'results_per_page': results_per_page,
            'results': results
        }
