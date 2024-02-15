from typing import Tuple

from selenium.webdriver.common.by import By


class Locators:
    # loginpage

    USER_NAME = (By.XPATH, "//input[@id='mui-1']")
    PASSWORD = (By.XPATH, "//input[@id='mui-2']")
    VISIBLE_EYE = (
        By.XPATH, "//button[@aria-label='toggle password visibility']//*[name()='svg']")
    SIGNIN = (By.XPATH, "//button[normalize-space()='Log In']")
    USERNAME_PASSWORD_REQ_MSG = (By.XPATH,
                                 "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeMedium MuiFormHelperText-contained css-v7esy']")

    # SIDEBAR
    MENU = (By.XPATH, "//button[@aria-label='open drawer']//*[name()='svg']")
    CONFIGURE = (By.XPATH, "//div[@role='button']//*[name()='svg']")
    COMPANY_CODE = (By.XPATH, "//span[normalize-space()='Company Code']")
    USER_ROLES = (By.XPATH, "//div[@role='button']//*[name()='svg']")
    GROUP = (By.XPATH, "//span[normalize-space()='Group']")
    DATA_TABLE = (By.XPATH, "//span[normalize-space()='Data Table']")
    MANAGE_DATA = (By.XPATH, "//span[normalize-space()='Manage Data']")
    DOCUMENT_CREATION = (By.XPATH, "//span[contains(text(),'Document Creation')]")
    MANAGE_DOCUMENT = (By.XPATH, "//a[@href='/documents/data']//li[@class='MuiListItem-root MuiListItem-gutters']")
    APP_CONFIGURATION = (By.XPATH, "//span[normalize-space()='App Configuration']")
    ASSET_TYPES = (By.XPATH, "//span[normalize-space()='Asset Types']")
    ACTION_STAGE = (By.XPATH, "//span[normalize-space()='Action Stage']")
    HOME = (By.XPATH, "//span[normalize-space()='Home']")
    DEFINE_TEMPLATES = (By.XPATH, "//span[normalize-space()='Define Templates']")
    ESTABLISH_RELATION = (By.XPATH, "//span[normalize-space()='Establish Relation']")
    ASSIGN = (By.XPATH, "(//span[normalize-space()='Assign'])[1]")
    ACTION_TRACKER = (By.XPATH, "//span[normalize-space()='Action Tracker']")
    CALENDER = (By.XPATH, "//span[normalize-space()='Calendar']")
    REPORTS = (By.XPATH, "//span[normalize-space()='Reports']")

    # HOMEPAGE
    DATA = (By.XPATH, "//div[@id='LT0']//div[@class='MuiCardContent-root cardStyle2l css-1qw96cp']")
    BACK = (By.XPATH, "//button[normalize-space()='Back']")

    # DEFINE TEMPLATES
    ADD_FORM = (By.XPATH, "//button[@id='Form_Add-Button']")
    CHECK_BOX = (By.XPATH, "//input[@id='ag-119-input']")
    EDIT_FORM = (By.XPATH, "//button[@id='Form_Edit-Button']//*[name()='svg']")
    DELETE_FORM = (By.XPATH, "//button[@id='Form_Delete-Button']")
    PREVIEW_FORM = (By.XPATH, "(//button[@id='Form_Edit-Button'])[2]")
    TEMPLATES_NAME = (By.XPATH, "//input[@id='Form_Add_Template-name']")
    TEMPLATES_CLICK = (By.XPATH, "//div[@id='Form_Add_Template-type']")
    QUESTION_TYPE = (By.XPATH, "//ul[@role='listbox']/li")
    DESCRIPTION = (By.XPATH, "//input[@id='Form_Add_Template-description']")
    TEMP_ICON_CLICK = (By.XPATH, "//button[@id='Form_Select-Icon_Button']")
    TEMP_ICON_SEARCH = (By.XPATH, "//input[@id='Form_Search-Icon_Button']")
    TEMP_ICON_BUILD = (By.XPATH, "//button[5]//*[name()='svg']")
    FORM_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[65]")
    ELEMENT1 = (
        By.XPATH,
        "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 css-vuzb25'])[3]")
    ELEMENT2 = (
        By.XPATH,
        "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 css-vuzb25'])[4]")
    FORM_REQ_MSG = (By.XPATH,
                    "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained css-hjvdj6']")
    SOP_CHECKLIST = (By.XPATH, "//li[normalize-space()='SOP checklist']")
    # First Question
    FORM_DATA_TABLE = (By.XPATH, "//input[@role='combobox']")
    QUESTION_NAME = (By.XPATH, "//input[@id='Form_Add_Template-Question-0-title']")
    REPORT_TITLE = (By.XPATH, "(//input[@id='Form_Add_Template-Question-0-report_title'])[1]")
    ANSWER_CLICK = (By.XPATH, "//div[@id='Form_Add_Template-Question-0-type']")
    ANSWER_TYPE = (By.XPATH, "//ul[@role='listbox']/li")
    REQUIRED = (By.XPATH,
                "//span[@class='MuiButtonBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary Mui-checked PrivateSwitchBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary Mui-checked Mui-checked css-1nr2wod']")
    FORM_SUBMIT = (By.XPATH, "//button[@type='submit']//*[name()='svg']")
    FORM_DUPLICATE = (By.XPATH, " //button[@id='Form_Add_Template-Question0-Duplicate'][1]")

    ADD_QUESTION = (By.XPATH, "//button[@id='Form_Add_Template-add']//*[name()='svg']")
    UPLOAD_CHECKBOX = (By.XPATH, "(//label)[10]")
    JPGE_CHECKBOX = (By.XPATH, "(//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd "
                               "css-1jaw3da'])[3]")
    PNG_CHECKBOX = (By.XPATH, "(//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd "
                              "css-1jaw3da'])[4]")
    NO_OF_UPLOADS_CLICK = (By.XPATH,
                           "(//div[@id='mui-component-select-form_fields[0].field_attributes.options[0].no_upload'])[1]")
    NO_OF_UPLOADS_ALLOWED = (By.XPATH, "//ul[@role='listbox']/li")
    LIST_TYPE_CLICK = (By.XPATH, "(//div[@id='mui-component-select-form_fields[0].field_attributes.Apitype'])[1]")
    LIST_TYPE = (By.XPATH, "(//ul[@role='listbox'])/li")
    SELECT_DATA_TABLE = (By.XPATH, "//input[@name='form_fields[0].field_attributes.asset_type_id']")
    ASSET_QUESTION = (By.XPATH, "//input[@placeholder='Define Title / Question']")
    EXPECTED_ANSWER = (By.XPATH, "//span[normalize-space()='Expected Answer']")
    EXC_YES = (By.XPATH, "(//span[contains(@class,'MuiTouchRipple-root css-w0pj6f')])[11]")
    EXC_NO = (By.XPATH, "(//span[normalize-space()='No'])[1]")
    RATING_SCALE_CLICK = (
        By.XPATH, "(//div[@id='mui-component-select-form_fields[0].field_attributes.RatingScale'])[1]")
    RATING_SCALE_NAME = (By.XPATH, "//ul[@role='listbox']/li")

    # Second Question
    SEC_QUESTION_NAME = (By.XPATH, "//input[@id='Form_Add_Template-Question-1-title']")
    SEC_REPORT_TITLE = (By.XPATH, "//input[@id='Form_Add_Template-Question-1-report_title']")
    SEC_ANS_CLICK = (By.XPATH, "//div[@id='Form_Add_Template-Question-1-type']")
    SEC_ANS_TYPE = (By.XPATH, "//ul[@role='listbox']/li")
    SEC_OPTION1 = (By.XPATH, "(//input[@name='form_fields[1].field_attributes.options[0].option'])[1]")
    SEC_OPTION2 = (By.XPATH, "(//input[@name='form_fields[1].field_attributes.options[1].option'])")
    SEC_OPT_DETAILS = (By.XPATH, "//div[@id='Form_Add_Template-Question1-option0option_type']")
    SEC_OPT_DETAILS2 = (By.XPATH, "//div[@id='Form_Add_Template-Question1-option1option_type']")
    SEC_OPT_DETAILS_CLICK = (By.XPATH, "(//ul[@role='listbox'])/li")
    SEC_UPLOAD1 = (By.XPATH,
                   "(//span[@class='MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium css-zun73v'])[3]")
    SEC_UPLOAD2 = (By.XPATH,
                   "(//span[contains(@class,'MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium css-zun73v')])[5]")

    def SEC_UPLOAD(self, n):
        return (By.XPATH,
                "(//span[@class='MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium css-zun73v'])[{}]".format(
                    n))

    SEC_JPGE_CHECKBOX = (By.XPATH,
                         "(//span[@class='MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall css-zun73v'])[8]")
    SEC_PNG_CHECKBOX = (
        By.XPATH, "(//span[@class='MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall css-zun73v'])[8]")
    SEC_NO_OF_UPLOADS_CLICK = (By.XPATH, "(//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall  css-fvipm8'])[7]")
    SEC_NO_OF_UPLOADS_ALLOW = (By.XPATH, "//ul[@role='listbox']/li")
    SEC_EXC_ANS = (By.XPATH, "(//span[normalize-space()='Expected Answer'])[2]")
    SEC_EXC_YES = (By.XPATH, "(//span[normalize-space()='Yes'])[1]")
    SEC_EXC_NO = (By.XPATH,
                  "(//span[@class='MuiButtonBase-root MuiRadio-root MuiRadio-colorPrimary PrivateSwitchBase-root MuiRadio-root MuiRadio-colorPrimary Mui-checked MuiRadio-root MuiRadio-colorPrimary css-1a5icme'])[1]")

    # third question
    THR_QUESTION_NAME = (By.XPATH, "//input[@id='Form_Add_Template-Question-2-title']")
    THR_REPORT_TITLE = (By.XPATH, "//input[@id='Form_Add_Template-Question-2-report_title']")
    THR_ANSWER_CLICK = (By.XPATH, "(//div[@class='MuiListItemText-root css-1tsvksn'])[3]")
    THR_ANSWER_TYPE = (By.XPATH, "//ul[@role='listbox']/li")
    THR_VALID_QUES =(By.XPATH,"//div[@id='Form_Add_Template-Question2-Validation-type']")
    THR_VALID_QUES_TYPE = (By.XPATH,"//ul[@role='listbox']/li")
    THR_VALID_ANS =(By.XPATH,"//div[@id='Form_Add_Template-Question2-Validation_value']")
    THR_VALID_ANS_TYPE = (By.XPATH,"//ul[@role='listbox']/li")



    # Report page
    REPORT_PERIOD = (By.XPATH, "//div[@id='report-period']")
    REPORT_PERIOD_LIST = (By.XPATH, "(//li[@role='option'])")
    PDF_DOWNLOAD = (By.XPATH, "//button[normalize-space()='PDF']")
    EXCEL_DOWNLOAD = (By.XPATH, "//button[normalize-space()='Excel']")
    # Checklist Report_Page
    CHECKLIST = (By.XPATH, "//button[normalize-space()='Checklist']")
    COMP_CODE_LIST = (By.XPATH, "//input[@id='compcode']")
    SORT_BY = (By.XPATH, "//input[@id='jor_status']")
    CHECK_VIEW_REPORT = (
        By.XPATH, "//span[@id='cell-Remarks-7']")
    IMAGE_VIEW = (By.XPATH, "(//img[@id='img-0-1'])[1]")

    # Formfilled Report Page
    FORMFILLED_REPORT = (By.XPATH, "(//button[normalize-space()='Form Filled Report'])[1]")
    FORMFILL_VIEW_REPORT = (
        By.XPATH, "(//span[@class='MuiButton-startIcon MuiButton-iconSizeMedium css-6xugel'])[5]")
    REPORT_ASSIGN = (By.XPATH, "(//button[@type='button'][normalize-space()='Assign'])[1]")
    ASSIGN_ITEM = (By.XPATH, "(//input[@id='Action_Item'])[1]")
    ASSIGN_TO = (By.XPATH, "//input[@id='assigned_to']")
    EXPECTED_DATE = (By.XPATH, "//input[@id='exp_end_date']")
    PRIORITY = (By.XPATH, "//input[@id='customer_priority']")
    ASS_SUBMIT = (By.XPATH, "//button[@id='submit']")
    FORMFILL_ASSIGN_ALL_REQ_MSG = (By.XPATH,
                                   "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained Mui-required css-hjvdj6']")

    # Deafult Reportpage
    DEAFULT_REPORT = (By.XPATH, "//button[normalize-space()='Defaulter Report']")
    # CAL =(By.XPATH,"(//*[name()='svg'][@aria-label='calendar'])[1]")
    # FROM_DATE = (By.XPATH,"//div[@title='30 Nov 2023']")
    # TO_DATE = (By.XPATH,"//div[@title='04 Dec 2023']")
    CLOSE = (By.XPATH, "/html/body/div[3]/div[4]")

    # Aging Report
    AGING_REPORT = (By.XPATH, "//button[normalize-space()='Aging Report']")
    AGING_ACTION_STAGE = (By.XPATH, "//input[@id='action_stage']")
    AGING_ASSIGN_TO = (By.XPATH, "//input[@id='assigned_to']")
    ECD_DATE = (By.XPATH, "//span[@class='rs-input-group-addon']")
    ECD_DATE_BOX = (By.XPATH, "//div[@title='19 Feb 2024']")
    NEXT_MONTH = (By.XPATH,"//button[@aria-label='Next month']")
    RESET = (By.XPATH, "(//button[normalize-space()='Reset'])[1]")
    AGING_VIEW = (By.XPATH, "(//span[@class='MuiButton-startIcon MuiButton-iconSizeMedium css-6xugel'])[6]")
    SCROLL = (By.XPATH, "//div[@class='ag-body-horizontal-scroll-viewport']")
    OUTSIDE_CLICK = (By.XPATH, "(//div[@role='none presentation'])[1]")

    # Assign page
    FIRST_BOX = (By.XPATH, "(//input[@role ='combobox'])[1]")
    SECOND_BOX = (By.XPATH, "(//input[@role ='combobox'])[2]")
    THIRD_BOX = (By.XPATH, "(//input[@id='combo-box-demo'])[3]")
    ASSIGN_SEARCH = (By.XPATH, "(//input[@placeholder='Search'])[1]")
    ASSIGN_CHECKBOX = (By.XPATH, "(//span[@class='MuiTypography-root MuiTypography-body2 MuiListItemText-primary css-14tqbo1'])[1]")
    ASSIGN_BUTTON = (By.XPATH, "//button[normalize-space()='Assign >']")
    DEASSIGN_BUTTON = (By.XPATH, "(//button[normalize-space()='< Deassign'])[1]")
    ASSIGN_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")

    # Action Tracker
    ACTION_ITEM = (By.XPATH, "//input[@id='action_item']")
    ACTION_TRACKER_STAGE = (By.XPATH, "//input[@id='action_stage']")
    ACTION_ASSIGN_TO = (By.XPATH, "(//input[@id='assigned_to'])[1]")
    ACTION_ASSIGN_BY = (By.XPATH, "//input[@id='assigned_by']")
    ACTION_PRIORITY = (By.XPATH, "(//input[@id='assigned_to'])[2]")
    ASSIGN_NEXT = (By.XPATH, "//input[@id='action_item_for_next']")
    ACTION_RESET = (By.XPATH, "//button[@id='act_reset']")
    SOURCE = (By.XPATH,
              "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root kanbanod_cards_spec css-s18byi'])[1]")
    TARGET = (By.XPATH, "(//div[@class='kanbanod_stages_spec col-sm-4'])[2]")
    ACTION_EDIT = (By.XPATH, "(//*[name()='svg'][@id='kanbanod_editlead'])[1]")
    EDIT_ITEM = (By.XPATH, "//input[@id='item']")
    EDIT_ECD = (By.XPATH, "//input[@id='exp_end_date']")
    EDIT_PRIORITY = (By.XPATH, "//input[@id='statusid']")
    EDIT_SUBMIT = (By.XPATH, "//span[normalize-space()='Submit']")
    ACTION_DELETE = (By.XPATH, "(//*[name()='svg'][@id='kanbanod_deletelead'])[1]")

    # Establish realation
    ER_ADD = (By.XPATH, "//button[@id='Allocate_config_Add-Button']")
    ER_EDIT = (By.XPATH, "//button[@id='Allocate_config_Edit-Button']")
    ER_DELETE = (By.XPATH, "//button[@id='Allocate_config_Delete-Button']")
    ER_DELETE_YES = (By.XPATH, "(//button[normalize-space()='Yes'])[1]")
    FIRST_ASSET_TYPE = (By.XPATH, "(//input[@id='mui-3'])[1]")
    SEC_ASSET_TYPE = (By.XPATH, "(//input[@id='mui-5'])[1]")
    ASSET_MAPPING = (By.XPATH, "(//div[@id='Assert_type-3'])[1]")
    ER_SUBMIT = (By.XPATH, "(//button[normalize-space()='Submit'])[1]")
    ER_CANCEL = (By.XPATH, "//button[@id='Cancel']")
    ER_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[54]")
    ASS_MAP_CLICK = (By.XPATH, "(//div[@id='Assert_type-3'])[1]")
    ASS_MAP_ER_EDIT = (By.XPATH, "(//ul[@role='listbox'])[1]")
    ER_UPDATE = (By.XPATH, "(//button[normalize-space()='Update'])[1]")
    ER_ASSET_REQ_MSG = (By.XPATH,
                        "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained css-hjvdj6']")

    # Calendar
    CAL_ADD = (By.XPATH, "(//button[@id='Form_Add-Button'])[1]")
    CAL_EDIT = (By.XPATH, "(//button[@id='Form_Edit-Button'])[1]")
    CAL_DELETE = (By.XPATH, "(//button[@id='Form_Delete-Button'])[1]")
    CAL_EVENT_NAME = (By.XPATH, "(//input[@id='mui-1'])[1]")
    EVENT_DESC = (By.XPATH, "(//textarea[@id='mui-2'])[1]")
    START_DATE = (By.XPATH, "(//input[@id='mui-3'])[1]")
    END_DATE = (By.XPATH, "(//input[@id='mui-5'])[1]")
    CAL_REPEAT = (By.XPATH, "(//input[@id='mui-4'])[1]")
    CAL_REPEAT_DAY = (By.XPATH, "//ul[@role='listbox']/li")
    CAL_HOURSLY = (
        By.XPATH, "(//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd css-1jaw3da'])[1]")
    CAL_REP_HRS = (By.XPATH, "(//input[@id='mui-6'])[1]")
    CAL_START_TIME = (By.XPATH, "(//input[@id='mui-7'])[1]")
    CAL_END_TIME = (By.XPATH, "(//input[@id='mui-8'])[1]")
    CAL_SUBMIT = (By.XPATH, "(//button[normalize-space()='Submit'])[1]")
    CAL_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[107]")
    CAL_UPDATE = (By.XPATH, "(//button[normalize-space()='Update'])[1]")
    CAL_EDIT_START_TIME = (By.XPATH, "(//input[@id='mui-21'])[1]")
    CAL_DELETE_YES = (By.XPATH, "(//button[normalize-space()='Yes'])[1]")
    CAL_ALL_REQ_MSG = (By.XPATH,
                       "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained css-hjvdj6']")

    # ACTION_STAGE
    ACTION_STAGE_ADD = (By.XPATH, "(//button[@id='add_stage'])[1]")
    ACTION_STAGE_EDIT = (By.XPATH, "(//button[@id='edit_stage'])[1]")
    ACTION_STAGE_DELETE = (By.XPATH, "(//button[@id='delete_stage'])[1]")
    ACTION_STAGE_DOWNLOAD = (By.XPATH, "(//button[@id='download_stage'])[1]")
    ACTION_STAGE_CHECKBOX = (By.XPATH, "(//span[@id='cell-action_level-12'])[1]")
    ACTION_LAST_STAGE = (
        By.XPATH,
        "//label[contains(@class,'MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd css-1jaw3da')]")
    ACTION_STAGE_SUBMIT = (By.XPATH, "(//span[normalize-space()='Submit'])[1]")
    ACTION_STAGE_UPDATE = (By.XPATH, "(//span[normalize-space()='Submit'])[1]")
    ACTION_STAGE_DELETE_YES = (By.XPATH, "(//button[normalize-space()='Yes'])[1]")
    ACTION_LEVEL = (By.XPATH, "(//input[@id='action_level'])[1]")
    ACTION_STAGE_NAME = (By.XPATH, "(//input[@id='action_name'])[1]")
    ACTION_STAGE_DESC = (By.XPATH, "(//input[@id='action_description'])[1]")

    # Asset_type page
    ASSET_ADD = (By.XPATH, "//button[@id='Asset_types_Add-Button']")
    ASSET_EDIT = (By.XPATH, "//button[@id='Asset_types_Edit-Button']")
    ASSET_DELETE = (By.XPATH, "//button[@id='Asset_types_Delete-Button']")
    ASSET_CHECKBOX = (By.XPATH, "//div[@class='ag-wrapper ag-input-wrapper ag-checkbox-input-wrapper ag-checked']")
    ADD_ASSET_TYPE = (By.XPATH, "//input[@id='asset_type_assert_type']")
    ADD_ASSET_PATH = (By.XPATH, "//input[@id='asset_type_path']")
    ADD_ASSET_LABEL1 = (By.XPATH, "//input[@id='asset_type_label1']")
    ADD_ASSET_LABEL2 = (By.XPATH, "//input[@id='asset_type_label2']")
    ADD_ASSET_SUBMIT = (By.XPATH, "//button[@id='Submit']")
    ADD_ASSET_CANCEL = (By.XPATH, "//button[@id='Cancel']")

    # Group Page
    GROUP_TITLE = (By.XPATH, "//input[@id='title']")
    GROUP_DESC = (By.XPATH, "//input[@id='description']")
    GROUP_ICON = (By.XPATH, "//button[@id='Form_Select-Icon_Button']")
    GROUP_ICON_SEARCH = (By.XPATH, "//input[@id='Form_Search-Icon_Button']")
    GROUP_ICON_FIRE = (By.XPATH, "//div[@role='dialog']//button[2]")
    GROUP_ADD = (By.XPATH, "//button[normalize-space()='Add']")
    GROUP_EDIT = (By.XPATH, "(//button[@type='button'][normalize-space()='Edit'])[1]")
    GROUP_DELETE = (By.XPATH, "(//button[@type='button'][normalize-space()='Delete'])[1]")
    GROUP_UPDATE = (By.XPATH, "//button[normalize-space()='Update']")

    # CompCode Page
    COMPCODE_ADD = (By.XPATH, "//button[@id='Allocate_config_Add-Button']")
    COMPCODE_EDIT = (By.XPATH, "//button[@id='Allocate_config_Edit-Button']")
    COMPCODE_DELETE = (By.XPATH, "//button[@id='Allocate_config_Delete-Button']")
    COMPCODE_COMP_NAME = (By.XPATH, "//input[@id='CompanyName']")
    COMPCODE_COMP_CODE = (By.XPATH, "//input[@id='compcode']")
    COMPCODE_SUBMIT = (By.XPATH, "//button[@id='Submit']")
    COMPCODE_CANCEL = (By.XPATH, "//button[@id='Cancel']")
    COMPCODE_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[53]")
    COMPCODE_ASSIGN = (By.XPATH, "//button[normalize-space()='Assign']")
    COMPCODE_ASSIGN_SELECTE1 = (By.XPATH, "(//div[@id='demo-simple-select'])[1]")
    COMPCODE_ASSIGN_SELECTE1_LIST = (By.XPATH, "//ul[@role='listbox']/li")
    COMPCODE_ASSIGN_SELECTE2 = (By.XPATH, "//input[@id='combo-box-demo']")
    COMPCODE_ASSIGN_SELECTE3 = (By.XPATH, "(//div[@id='demo-simple-select'])[2]")
    COMPCODE_ASSIGN_SELECTE3_LIST = (By.XPATH, "//ul[@role='listbox']/li")
    COMPCODE_ASSIGN_SEARCH = (By.XPATH, "(//input[@placeholder='Search'])[1]")
    COMPCODE_ASSIGN_CHECKBOX = (By.XPATH, "//span[normalize-space()='test123']")
    COMPCODE_ASSIGN_BUTTON = (By.XPATH, "//button[normalize-space()='Assign >']")
    COMPCODE_DEASSIGN_BUTTON = (By.XPATH, "//button[normalize-space()='< Deassign']")

    # Datatabel
    DATATABLE_ADD = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root'])[5]")
    DATATABLE_EDIT = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root'])[6]")
    DATATABLE_DELETE = (
        By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[18]")
    DATATABLE_GOBACK = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root'])[7]")
    DATATABLE_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
    DATATABLE_CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']")
    DATATABLE_ADDLABEL = (By.XPATH, "//button[@id='Form_Add_Template-add']")

    ##First Question
    DATATABLE_CATEGORY = (By.XPATH, "(//input[@id='Form_Add_Template-name'])[1]")
    DATATABLE_CATEGORY_DESC = (By.XPATH, "(//input[@id='Form_Add_Template-description'])[1]")
    DATATABLE_LABEL1 = (By.XPATH, "//input[@id='Form_Add_Template-Question-0-external_name']")
    DATATABLE_QUESTION_TYPE = (By.XPATH, "//div[@id='Form_Add_Template-Question-0-type']")
    DATATABLE_QUES_TYPE_LIST = (By.XPATH, "//ul[@role='listbox']/li")
    DATABLE_VALID_QUES_TYPE = (By.XPATH, "//div[@id='Form_Add_Template-Question0-Validation-type']")
    DATABLE_VALID_QUES_TYPE_LIST = (By.XPATH, "//ul[@role='listbox']/li")
    SPECIAL_TEXT_TYPE = (By.XPATH, "//div[@id='Form_Add_Template-Question0-Validation_value']")
    SPECIAL_TEXT_TYPE_LIST = (By.XPATH, "//li[normalize-space()='PAN No']")
    DATATABLE_REQUIRED1 = (By.XPATH, "//input[@id='Form_Add_Template-Question0-is_required']")
    DATABLE_DUPLICATE = (By.XPATH, "//button[@id='Form_Add_Template-Question0-Duplicate']")
    DATABLE_DELETE = (By.XPATH,
                      "//button[@id='Form_Add_Template-Question0-Delete']//*[name()='svg']//*[name()='path' and contains(@d,'M6 19c0 1.')]")
    ###Second Question
    DATATABLE_LABEL2 = (By.XPATH, "//input[@id='Form_Add_Template-Question-1-external_name']")
    DATA_VALID_TYPE = (By.XPATH, "//div[@id='Form_Add_Template-Question1-Validation-type']")
    DATA_VALID_TYPE_LIST = (By.XPATH, "//ul[@role='listbox']/li")
    DATATABLE_REGEX_PATTERN = (By.XPATH, "//input[@id='Form_Add_Template-Question1-Validation_regex']")
    DATABLE_VALID_QUES_TYPE2 = (By.XPATH, "(//div[@id='Form_Add_Template-Question1-Validation-type'])[1]")
    DATABLE_VALID_QUES_TYPE_LIST2 = (By.XPATH, "//ul[@id='mui-7']/li")

    ###Third Questions
    DATATABLE_CLICK = (By.XPATH,
                       "//div[@class='MuiButtonBase-root MuiListItemButton-root MuiListItemButton-gutters Mui-selected MuiListItemButton-root MuiListItemButton-gutters Mui-selected css-1uwabd6']")
    DATATABLE_LABEL3 = (By.XPATH, "//input[@id='Form_Add_Template-Question-2-external_name']")
    DATATABLE_QUESTION_TYPE2 = (By.XPATH,
                                "//div[@id='Form_Add_Template-Question-2-type']//div//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-yb0lig']")
    DATABLE_OPTION = (By.XPATH, "//button[@id='Form_Add_Template-Question2-option_add']")
    DATABLE_OPTION_TEXT = (By.XPATH, "//input[@id='Form_Add_Template-Question2-option2option_name']")

    # Managedata
    MANAGE_DATA_CLICK = (By.XPATH, "//span[normalize-space()='Externals Data']")
    MANAGE_DATA_ADD = (By.XPATH, "(//button[@type='button'])[3]")
    MANAGE_DATA_EDIT = (By.XPATH, "(//button[@type='button'])[4]")
    MANAGE_DATA_DELETE = (By.XPATH, "(//button[@type='button'])[5]")
    MANAGE_DATA_GO_BACK = (By.XPATH,
                           "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium n_btn css-1ujsas3']")
    MANAGE_DATA_FIRST_INPUT = (By.XPATH,
                               "(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[1]")
    MANAGE_DATA_SEC_INPUT = (By.XPATH,
                             "(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[2]")
    MANAGE_DATA_THRID_INPUT = (By.XPATH, "(//div[@role='combobox'])[1]")
    MANAGE_DATA_OPTION = (By.XPATH, "//ul[@role='listbox']/li")
    MANAGE_DATA_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
    MANAGE_DATA_ERR_MSG = (By.XPATH, "(//p[@id='mui-10-helper-text'])[1]")
    MANAGE_DATA_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[43]")

    ##Document creation
    DOCUMENT_ADD = (By.XPATH, "(//button[@type='button'])[3]")
    DOCUMENT_EDIT = (By.XPATH, "(//button[@type='button'])[4]")
    DOCUMENT_DELETE = (By.XPATH, "(//button[@type='button'])[5]")
    DOCUMENT_GOBACK = (By.XPATH, "(//button[@type='button'])[6]")
    DOCUMENT_CLICK = (By.XPATH, "//span[normalize-space()='License']")

    # First Doc
    DOCUMENT_NAME = (By.XPATH, "//input[@id='Form_Add_Template-name']")
    DOCUMENT_DESC = (By.XPATH, "//input[@id='Form_Add_Template-description']")
    DOCUMENT_LABEL1 = (By.XPATH, "//input[@id='Form_Add_Template-Question-0-external_name']")
    DOCUMENT_QUES_TYPE = (By.XPATH, "(//div[@class='MuiListItemText-root css-1tsvksn'])[1]")
    DOCUMENT_QUES_TYPE_LIST = (By.XPATH, "(//ul[@role='listbox'])/li")
    DOCUMENT_QUES_VALID_TYPE = (By.XPATH, "//div[@id='Form_Add_Template-Question0-Validation-type']")
    DOCUMENT_QUES_VALID_TYPE_LIST = (By.XPATH, "(//ul[@role='listbox'])/li")
    DOCUMENT_ANS_VALID_TYPE = (By.XPATH, "(//div[@id='Form_Add_Template-Question0-Validation_value'])[1]")
    DOCUMENT_ANS_VALID_TYPE_LIST = (By.XPATH, "//li[normalize-space()='Numeric Only']")
    DOCUMENT_ADD_LABEL = (By.XPATH, "//button[@id='Form_Add_Template-add']")
    DOCUMENT_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
    DOCUMENT_CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']")

    ##Seco Docu
    DOCUMENT_LABEL2 = (By.XPATH, "//input[@id='Form_Add_Template-Question-1-external_name']")
    DOCUMENT_QUES_TYPE2 = (By.XPATH, "(//div[@class='MuiListItemText-root css-1tsvksn'])[2]")
    DOCUMENT_DATA_TABLE = (
        By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall "
                  "MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1']"
                  "[@name='config_attributes[1].attribute.asset_type_id']")
    DOCUMENT_DATA_COLUMN = (By.XPATH,
                            "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd "
                            "MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1'][contains(@name,'config_attributes[1].attribute.asset_type_label')]")

    ##Third DOC
    DOCUMENT_LABEL3 = (By.XPATH, "//input[@id='Form_Add_Template-Question-2-external_name']")
    DOCUMENT_QUES_TYPE3 = (By.XPATH, "(//div[@class='MuiListItemText-root css-1tsvksn'])[3]")
    DOCUMENT_PDF = (By.XPATH, "//p[normalize-space()='PDF']")
    DOCUMENT_DOCX = (By.XPATH, "//p[normalize-space()='DOCX'] ")
    DOCUMENT_CSV = (By.XPATH, "//p[normalize-space()='CSV']")

    ##Fourth DOC
    DOCUMENT_EXP_DATE = (By.XPATH, "//span[normalize-space()='Expiry Date']")
    DOCUMENT_LABEL4 = (By.XPATH, "//input[@id='Form_Add_Template-Question-3-external_name']")
    DOCUMENT_QUES_TYPE4 = (By.XPATH, "(//div[@class='MuiListItemText-root css-1tsvksn'])[4]")

    ##Managedocument
    MANAGE_DOC_CLICK = (By.XPATH, "(//div[@role='button'])[2]")
    MANAGE_DOC_ADD = (By.XPATH, "(//button[@type='button'])[3]")
    MANAGE_DOC_EDIT = (By.XPATH, "(//button[@type='button'])[4]")
    MANAGE_DOC_DELETE = (By.XPATH, "(//button[@type='button'])[5]")
    MANAGE_DOC_GOBACK = (By.XPATH, "(//button[@type='button'])[6]")
    MANAGE_DOC_FIRST_INPUT = (By.XPATH, "//input[@type='ShortAnswer']")
    MANAGE_DOC_SEC_INPUT = (By.XPATH, "//input[@id='search-single']")
    MANAGE_DOC_THR_INPUT = (By.ID, 'upload_10df985a-fbfe-4345-a672-4d20f12db08a')
    MANAGE_DOC_FOUR_INPUT = (By.XPATH, "//input[@type='date']")
    MANAGE_DOC_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
    MANAGE_DOC_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[67]")
    MANAGE_DOC_UPLOAD_DELETE = (By.XPATH,
                                "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-colorError MuiIconButton-sizeMedium css-1oh31is']")
