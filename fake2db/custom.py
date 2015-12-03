def faker_options_container():
    '''
    Following dictionary is mapped with fake-factory
    providers, so that custom db creation be made with
    faker.

    for detailed info for providers:

    http://fake-factory.readthedocs.org/en/latest/#

    '''
    faker_options = {"name_male": "varchar(200)",
                     "address": "varchar(300)",
                     "am_pm": "varchar(3)",
                     "boolean": "varchar(10)",
                     "opera": "varchar(300)",
                     "paragraph": "varchar(300)",
                     "bs": "varchar(300)",
                     "building_number": "INT",
                     "password": "varchar(300)",
                     "century": "varchar(50)",
                     "phone_number": "varchar(250)",
                     "chrome": "varchar(300)",
                     "postalcode": "varchar(300)",
                     "city": "varchar(300)",
                     "postalcode_plus4": "varchar(300)",
                     "city_prefix": "varchar(300)",
                     "postcode": "varchar(300)",
                     "city_suffix": "varchar(300)",
                     "prefix": "varchar(300)",
                     "color_name": "varchar(300)",
                     "prefix_female": "varchar(300)",
                     "company": "varchar(300)",
                     "prefix_male": "varchar(300)",
                     "company_email": "varchar(300)",
                     "profile": "varchar(300)",
                     "company_suffix": "varchar(300)",
                     "provider": "varchar(300)",
                     "country": "varchar(300)",
                     "country_code": "varchar(300)",
                     "credit_card_expire": "varchar(300)",
                     "credit_card_full": "varchar(300)",
                     "credit_card_number": "varchar(300)",
                     "credit_card_provider": "varchar(300)",
                     "credit_card_security_code": "varchar(300)",
                     "currency_code": "varchar(30)",
                     "date": "varchar(300)",
                     "date_time_ad": "varchar(300)",
                     "date_time_between": "varchar(300)",
                     "date_time_between_dates": "varchar(300)",
                     "random_digit": "INT",
                     "random_digit_not_null": "varchar(300)",
                     "date_time_this_decade": "varchar(300)",
                     "random_digit_not_null_or_empty": "varchar(300)",
                     "date_time_this_month": "varchar(300)",
                     "random_digit_or_empty": "varchar(300)",
                     "date_time_this_year": "varchar(300)",
                     "random_element": "varchar(300)",
                     "day_of_month": "varchar(300)",
                     "random_int": "INT",
                     "day_of_week": "varchar(300)",
                     "random_letter": "varchar(5)",
                     "domain_name": "varchar(300)",
                     "random_number": "INT",
                     "domain_word": "varchar(300)",
                     "ean": "varchar(300)",
                     "rgb_color": "varchar(300)",
                     "ean13": "varchar(300)",
                     "rgb_color_list": "varchar(300)",
                     "ean8": "varchar(300)",
                     "prgb_css_color": "varchar(300)",
                     "email": "varchar(300)",
                     "safari": "varchar(300)",
                     "file_extension": "varchar(300)",
                     "safe_color_name": "varchar(300)",
                     "file_name": "varchar(300)",
                     "safe_email": "varchar(300)",
                     "firefox": "varchar(300)",
                     "safe_hex_color": "varchar(300)",
                     "first_name": "varchar(300)",
                     "secondary_address": "varchar(300)",
                     "first_name_female": "varchar(300)",
                     "first_name_male": "varchar(300)",
                     "sentence": "varchar(300)",
                     "free_email": "varchar(300)",
                     "free_email_domain": "varchar(300)",
                     "sha1": "varchar(300)",
                     "geo_coordinate": "varchar(300)",
                     "sha256": "varchar(300)",
                     "slug": "varchar(300)",
                     "hex_color": "varchar(300)",
                     "ssn": "varchar(300)",
                     "image_url": "varchar(300)",
                     "state": "varchar(300)",
                     "internet_explorer": "varchar(300)",
                     "state_abbr": "varchar(300)",
                     "ipv4": "varchar(300)",
                     "street_address": "varchar(300)",
                     "ipv6": "varchar(300)",
                     "street_name": "varchar(300)",
                     "iso8601": "varchar(300)",
                     "street_suffix": "varchar(300)",
                     "job": "varchar(300)",
                     "suffix": "varchar(300)",
                     "language_code": "varchar(300)",
                     "suffix_female": "varchar(300)",
                     "last_name": "varchar(300)",
                     "suffix_male": "varchar(300)",
                     "last_name_female": "varchar(300)",
                     "text": "varchar(300)",
                     "last_name_male": "varchar(300)",
                     "time": "varchar(300)",
                     "latitude": "varchar(300)",
                     "time_delta": "varchar(300)",
                     "timezone": "varchar(300)",
                     "linux_platform_token": "varchar(300)",
                     "tld": "varchar(300)",
                     "linux_processor": "varchar(300)",
                     "unix_time": "varchar(300)",
                     "locale": "varchar(300)",
                     "uri": "varchar(300)",
                     "longitude": "varchar(300)",
                     "uri_extension": "varchar(300)",
                     "mac_address": "varchar(300)",
                     "uri_page": "varchar(300)",
                     "mac_platform_token": "varchar(300)",
                     "uri_path": "varchar(300)",
                     "mac_processor": "varchar(300)",
                     "url": "varchar(300)",
                     "md5": "varchar(300)",
                     "user_agent": "varchar(300)",
                     "military_apo": "varchar(300)",
                     "user_name": "varchar(300)",
                     "military_dpo": "varchar(300)",
                     "uuid4": "varchar(300)",
                     "military_ship": "varchar(300)",
                     "windows_platform_token": "varchar(300)",
                     "military_state": "varchar(300)",
                     "word": "varchar(300)",
                     "mime_type": "varchar(300)",
                     "words": "varchar(300)",
                     "month": "varchar(300)",
                     "year": "varchar(300)",
                     "month_name": "varchar(300)",
                     "zipcode": "varchar(300)",
                     "name": "varchar(300)",
                     "zipcode_plus4": "varchar(300)",
                     "name_female": "varchar(300)",
    }
    
    return faker_options
