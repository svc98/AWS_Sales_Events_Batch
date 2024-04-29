def lambda_handler(event, context):
    print(event)

    if "contact-info" in event:
        print("Order Processing...")
        return event
    else:
        print("ERROR: Contact Information not found!!!")
        raise Exception("ContactInfoNotFound")
