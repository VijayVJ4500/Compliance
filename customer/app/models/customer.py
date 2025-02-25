import enum

from sqlalchemy import Column, BigInteger, VARCHAR, DateTime, ForeignKey, Boolean
from sqlalchemy_serializer import SerializerMixin

from .. import db_client


class CustomerType(enum.Enum):
    ORGANIZATION = "Organization"
    INDIVIDUAL = "Individual"


class Customer(db_client.Model, SerializerMixin):
    __tablename__ = 'customer'

    customer_id = Column(BigInteger, primary_key=True)
    customer_type = Column(VARCHAR(20))
    user_id = Column(BigInteger)
    organization_name = Column(VARCHAR(300))
    industry_type = Column(VARCHAR(300))
    mobile_no = Column(VARCHAR(30))
    additional_mobile_no = Column(VARCHAR(30))
    email = Column(VARCHAR(300))
    compcode = Column(BigInteger)  # New field for asset management
    type = Column(VARCHAR(50))  # New field for asset management
    service_provider = Column(Boolean, default=False)  # New field for asset management
    additional_email = Column(VARCHAR(300))
    website = Column(VARCHAR(300))
    source = Column(BigInteger)
    source_csv = Column(VARCHAR(300))
    customer_type_csv = Column(VARCHAR(300))
    address = Column(VARCHAR(300))
    city = Column(VARCHAR(300))
    state = Column(VARCHAR(300))
    pincode = Column(BigInteger)
    gst = Column(VARCHAR(100))
    category = Column(VARCHAR(100))
    customer_group = Column(VARCHAR(100))
    tag = Column(VARCHAR(500))
    country = Column(VARCHAR(100))
    description = Column(VARCHAR(300))
    customer_chkbox = Column(Boolean, default=False)
    organization_name_map = Column(VARCHAR(300))
    customer_name = Column(VARCHAR(300))
    cat_id = Column(BigInteger)
    type_id = Column(BigInteger)
    tag_id = Column(BigInteger)
    job_position = Column(VARCHAR(300))
    pan = Column(VARCHAR(100))
    upload_logo = Column(VARCHAR(300))
    lead_category = Column(VARCHAR(300))
    # module_type = Column(VARCHAR(50))
    modified_by = Column(VARCHAR(255))
    modified_on = Column(DateTime)
    created_by = Column(VARCHAR(255))
    created_on = Column(DateTime)
    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)

