import requests
import xmltodict
import json


def fetch_xml_convert_json(nuts_code):
    """Fetch XML data for a given NUTS code and convert it to a Python dictionary."""
    url = f"https://volby.cz/pls/prez2023nss/vysledky_kraj?kolo=1&nuts={nuts_code}"
    response = requests.get(url)
    data_dict = xmltodict.parse(response.content)
    return data_dict


def extract_obec_objects(json_data):
    """Extract OBEC objects from the nested JSON data and include NAZ_KRAJ."""
    obec_list = []
    for item in json_data:
        try:
            krajs = item['VYSLEDKY_KRAJ']['KRAJ']
            if isinstance(krajs, dict):  # Ensure it's a list
                krajs = [krajs]
            for kraj in krajs:
                kraj_name = kraj['@NAZ_KRAJ']  # Get the NAZ_KRAJ value
                okresy = kraj['OKRES']
                if isinstance(okresy, dict):
                    okresy = [okresy]
                for okres in okresy:
                    obecs = okres['OBEC']
                    if isinstance(obecs, dict):
                        obecs = [obecs]
                    for obec in obecs:
                        # Append the NAZ_KRAJ value to each OBEC
                        obec['krajName'] = kraj_name
                    obec_list.extend(obecs)
        except KeyError as e:
            print(f"Error processing data: {e}")
    return obec_list


def main():
    nuts_codes = [
        'CZ010', 'CZ020', 'CZ031', 'CZ032', 'CZ041', 'CZ042', 'CZ051', 'CZ052',
        'CZ053', 'CZ063', 'CZ064', 'CZ071', 'CZ072', 'CZ080'
    ]

    all_data = []
    for nuts_code in nuts_codes:
        print(f"Fetching data for NUTS code: {nuts_code}")
        data_dict = fetch_xml_convert_json(nuts_code)
        all_data.append(data_dict)

    # Extract OBEC objects from the fetched data and include NAZ_KRAJ
    obec_data = extract_obec_objects(all_data)

    # Save the modified OBEC data to a JSON file
    with open('filtered_obec_data_with_kraj.json', 'w') as outfile:
        json.dump(obec_data, outfile, ensure_ascii=False, indent=4)

    print(
        "Filtered OBEC data with NAZ_KRAJ has been saved to filtered_obec_data_with_kraj.json"
    )


if __name__ == "__main__":
    main()
