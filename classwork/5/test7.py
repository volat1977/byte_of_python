def convert_dates(date_list):
    converted_date = []
    for i in date_list:
        converted_date.append(str(datetime.strptime(i, '%d-%m-%Y').date()))
    return converted_date

result_dates = convert_dates(date_list)
