# import requests
# import json

# # set the array of version numbers
# # versions = ['7.33', '7.08']
# json_data = '{"patches":[{"patch_number":"7.08","patch_name":"7.08","patch_timestamp":1517472000},{"patch_number":"7.09","patch_name":"7.09","patch_timestamp":1518681600},{"patch_number":"7.10","patch_name":"7.10","patch_timestamp":1519891200},{"patch_number":"7.11","patch_name":"7.11","patch_timestamp":1521097200},{"patch_number":"7.12","patch_name":"7.12","patch_timestamp":1522306800},{"patch_number":"7.13","patch_name":"7.13","patch_timestamp":1523516400},{"patch_number":"7.13b","patch_name":"7.13b","patch_timestamp":1523602800},{"patch_number":"7.14","patch_name":"7.14","patch_timestamp":1524553200},{"patch_number":"7.15","patch_name":"7.15","patch_timestamp":1525935600},{"patch_number":"7.16","patch_name":"7.16","patch_timestamp":1527404400},{"patch_number":"7.17","patch_name":"7.17","patch_timestamp":1528614000},{"patch_number":"7.18","patch_name":"7.18","patch_timestamp":1529910000},{"patch_number":"7.19","patch_name":"7.19","patch_timestamp":1532847600},{"patch_number":"7.19b","patch_name":"7.19b","patch_timestamp":1535785200},{"patch_number":"7.19c","patch_name":"7.19c","patch_timestamp":1536908400},{"patch_number":"7.19d","patch_name":"7.19d","patch_timestamp":1539327600},{"patch_number":"7.20","patch_name":"7.20","patch_timestamp":1542614400,"patch_website":"720","patch_website_anchor":"General"},{"patch_number":"7.20b","patch_name":"7.20b","patch_timestamp":1542700800},{"patch_number":"7.20c","patch_name":"7.20c","patch_timestamp":1543046400},{"patch_number":"7.20d","patch_name":"7.20d","patch_timestamp":1543564800},{"patch_number":"7.20e","patch_name":"7.20e","patch_timestamp":1544342400},{"patch_number":"7.21","patch_name":"7.21","patch_timestamp":1548748800},{"patch_number":"7.21b","patch_name":"7.21b","patch_timestamp":1550304000},{"patch_number":"7.21c","patch_name":"7.21c","patch_timestamp":1551513600},{"patch_number":"7.21d","patch_name":"7.21d","patch_timestamp":1553410800},{"patch_number":"7.22","patch_name":"7.22","patch_timestamp":1558681200},{"patch_number":"7.22b","patch_name":"7.22b","patch_timestamp":1558940400},{"patch_number":"7.22c","patch_name":"7.22c","patch_timestamp":1560063600},{"patch_number":"7.22d","patch_name":"7.22d","patch_timestamp":1561878000},{"patch_number":"7.22e","patch_name":"7.22e","patch_timestamp":1563087600},{"patch_number":"7.22f","patch_name":"7.22f","patch_timestamp":1564297200},{"patch_number":"7.22g","patch_name":"7.22g","patch_timestamp":1567753200},{"patch_number":"7.22h","patch_name":"7.22h","patch_timestamp":1569740400},{"patch_number":"7.23","patch_name":"7.23","patch_timestamp":1574755200,"patch_website":"outlanders","patch_website_anchor":"PatchNotesAnchor"},{"patch_number":"7.23a","patch_name":"7.23a","patch_timestamp":1574841600},{"patch_number":"7.23b","patch_name":"7.23b","patch_timestamp":1575014400},{"patch_number":"7.23c","patch_name":"7.23c","patch_timestamp":1575619200},{"patch_number":"7.23d","patch_name":"7.23d","patch_timestamp":1576051200},{"patch_number":"7.23e","patch_name":"7.23e","patch_timestamp":1576310400},{"patch_number":"7.23f","patch_name":"7.23f","patch_timestamp":1578297600},{"patch_number":"7.24","patch_name":"7.24","patch_timestamp":1580025600},{"patch_number":"7.24b","patch_name":"7.24b","patch_timestamp":1582704000},{"patch_number":"7.25","patch_name":"7.25","patch_timestamp":1584428400},{"patch_number":"7.25a","patch_name":"7.25a","patch_timestamp":1584514800},{"patch_number":"7.25b","patch_name":"7.25b","patch_timestamp":1585033200},{"patch_number":"7.25c","patch_name":"7.25c","patch_timestamp":1586156400},{"patch_number":"7.26","patch_name":"7.26","patch_timestamp":1587106800},{"patch_number":"7.26a","patch_name":"7.26a","patch_timestamp":1587452400},{"patch_number":"7.26b","patch_name":"7.26b","patch_timestamp":1588057200},{"patch_number":"7.26c","patch_name":"7.26c","patch_timestamp":1588402800},{"patch_number":"7.27","patch_name":"7.27","patch_timestamp":1593327600},{"patch_number":"7.27a","patch_name":"7.27a","patch_timestamp":1593846000},{"patch_number":"7.27b","patch_name":"7.27b","patch_timestamp":1594796400},{"patch_number":"7.27c","patch_name":"7.27c","patch_timestamp":1594969200},{"patch_number":"7.27d","patch_name":"7.27d","patch_timestamp":1598425200},{"patch_number":"7.28","patch_name":"7.28","patch_timestamp":1608192000,"patch_website":"mistwoods","patch_website_anchor":"PatchNotes"},{"patch_number":"7.28a","patch_name":"7.28a","patch_timestamp":1608537600},{"patch_number":"7.28b","patch_name":"7.28b","patch_timestamp":1610265600},{"patch_number":"7.28c","patch_name":"7.28c","patch_timestamp":1613721600},{"patch_number":"7.29","patch_name":"7.29","patch_timestamp":1617951600,"patch_website":"dawnbreaker","patch_website_anchor":"PatchSection"},{"patch_number":"7.29b","patch_name":"7.29b","patch_timestamp":1618556400},{"patch_number":"7.29c","patch_name":"7.29c","patch_timestamp":1619679600},{"patch_number":"7.29d","patch_name":"7.29d","patch_timestamp":1621839600},{"patch_number":"7.30","patch_name":"7.30","patch_timestamp":1629183600},{"patch_number":"7.30b","patch_name":"7.30b","patch_timestamp":1629615600},{"patch_number":"7.30c","patch_name":"7.30c","patch_timestamp":1631257200},{"patch_number":"7.30d","patch_name":"7.30d","patch_timestamp":1632553200},{"patch_number":"7.30e","patch_name":"7.30e","patch_timestamp":1635404400},{"patch_number":"7.31","patch_name":"7.31","patch_timestamp":1645603200,"patch_website":"primalbeast"},{"patch_number":"7.31b","patch_name":"7.31b","patch_timestamp":1646035200},{"patch_number":"7.31c","patch_name":"7.31c","patch_timestamp":1651474800},{"patch_number":"7.31d","patch_name":"7.31d","patch_timestamp":1654671600},{"patch_number":"7.32","patch_name":"7.32","patch_timestamp":1661238000},{"patch_number":"7.32b","patch_name":"7.32b","patch_timestamp":1661842800},{"patch_number":"7.32c","patch_name":"7.32c","patch_timestamp":1664262000},{"patch_number":"7.32d","patch_name":"7.32d","patch_timestamp":1669708800},{"patch_number":"7.32e","patch_name":"7.32e","patch_timestamp":1678089600},{"patch_number":"7.33","patch_name":"7.33","patch_timestamp":1681974000,"patch_website":"newfrontiers"},{"patch_number":"7.33b","patch_name":"7.33b","patch_timestamp":1682406000}],"success":true}'

# data = json.loads(json_data)

# version_numbers = []
# for patch in data['patches']:
#     version_numbers.append(patch['patch_number'])

# # create an empty list to store the patch data
# patch_data_list = []

# for version in version_numbers:
#     # set the URL and parameters
#     url = 'https://www.dota2.com/datafeed/patchnotes'
#     params = {'version': version, 'language': 'english'}

#     # send a GET request to the URL with the parameters
#     response = requests.get(url, params=params)

#     # parse the JSON data
#     data = response.json()

#     # append the patch data to the list
#     patch_data_list.append(data)

# # save the data to a file
# filename = 'patch_notes.json'
# with open(filename, 'a') as file:
#     json.dump(patch_data_list, file, indent=4)

# print(f'JSON data saved to {filename}')



import requests
from bs4 import BeautifulSoup
from datetime import datetime
from bs4 import NavigableString
import json

def fetch_release_date(soup):
    release_date_header = soup.find('div', string='Release Date')
    if not release_date_header:
        print('No release date header found')
        return None

    release_date_header = soup.find('div', string='Release Date')
    if not release_date_header:
        print('No release date header found')
        return None

    date_str = None
    date_div = release_date_header.find_next_sibling('div')
    if date_div:
        date_text = date_div.get_text(separator='|', strip=True).split('|')[-1]
        date_str = date_text.strip()

    if not date_str:
        print('No date found')
        return None

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except Exception as e:
        return None
    epoch_time = int(date_obj.timestamp())
    
    return epoch_time

def get_title(section_title):
    if "heroes" in section_title:
        return "heroes"
    else:
        return "items"

def fetch_patch_notes(url, version):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    patch_notes = {
        "patch_number": version,
        "patch_timestamp": None,
        "general": [],
        "items": {},
        "heroes": {"Added": []}
    }

    
    release_date_epoch = fetch_release_date(soup)
    if release_date_epoch:
        patch_notes["patch_timestamp"] = release_date_epoch


    h_elements = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])
    if not h_elements:
        print('No header elements found')
        return patch_notes

    for h in h_elements:
        section = h.find('span', {'class': 'mw-headline'})

        if section:
            section_title = section.text.strip().lower()

            if "heroes" in section_title or "items" in section_title:
                next_sibling = h.find_next_sibling()

                while next_sibling and next_sibling.name != 'h2':
                    if next_sibling.name == 'h2':
                        next_sibling = next_sibling.next_sibling
                        continue
                    if isinstance(next_sibling, NavigableString):
                        next_sibling = next_sibling.next_sibling
                        continue
                    
                    div = next_sibling
                    name_anchor = div.find('a')
                    if name_anchor:
                        name = name_anchor['title']
                        if "Old Abilities" in name:
                            name = name.split("/")[0]
                        changes = []
                        if h.name == 'h2':

                            # special case to handle newly added heroes
                            if "heroes" in section_title:
                                for heores_added in div.find_all('div', {'class': 'heroentrytext'}):
                                    patch_notes["heroes"]["Added"].append(heores_added.text.strip())
                            
                            # ignore img or else each h2 tag is repeated twice
                            if  not name_anchor.find('img'):
                                if div.get('class') is None:
                                    changes = [li.text.strip() for li in div.find_next('ul').find_all('li')]
                                elif 'heroentry' in div.get('class'):
                                    # print(div.get('class'), div.text.strip())
                                    pass
                                else:
                                    changes = [li.text.strip() for li in div.find_next('ul').find_all('li')]

                        if len(changes) > 0:
                            patch_notes[get_title(section_title)].setdefault(name, []).extend(changes)
                        

                        # special case to handle dd/dl tags
                        changes = []
                        dd_elements = div.find_all('dd')
                        name = div.find_previous_sibling('div').text.strip()
                        dd_responses = set()
                        for dd in dd_elements:
                            # Skip nested <dd> elements
                            if dd.find('dd'):
                                continue

                            # Fetch the text content of the <dd> element
                            dd_text = dd.get_text(separator=' ').strip()
                            if dd_text and dd_text not in dd_responses:
                                changes.append(dd_text)
                                dd_responses.add(dd_text)


                        if len(changes) > 0:
                            patch_notes[get_title(section_title)].setdefault(name, []).extend(changes)


                    next_sibling = next_sibling.next_sibling

            else:
            # elif "general" in section_title:
                ul_element = h.find_next("ul")
                if ul_element:
                    for li in ul_element.find_all('li'):
                        patch_notes["general"].append(li.text.strip())
    
    return patch_notes






patch_versions = ["6.00","6.01","6.02","6.03","6.04","6.05","6.06","6.07","6.08","6.09","6.10","6.11","6.12","6.13","6.14","6.15","6.16","6.17","6.18","6.19","6.20","6.21","6.22","6.23","6.24","6.25","6.26","6.27","6.28","6.29","6.30","6.31","6.32","6.33","6.34","6.35","6.36","6.37","6.38","6.39","6.40","6.41","6.42","6.43","6.44","6.45","6.46","6.47","6.48","6.49","6.50","6.51","6.52","6.53","6.54","6.55","6.56","6.57","6.58","6.59","6.60","6.61","6.62","6.63","6.64","6.65","6.66","6.67","6.68","6.69","6.70","6.71","6.72","6.73","6.74","6.75","6.76","6.77","6.78","6.79","6.80","6.81","6.82","6.83","6.84","6.85","6.86","6.87","6.88","6.88b","6.88c","6.88d","7.00","7.01","7.02","7.03","7.04","7.05","7.06","7.06b","7.06c"]
# patch_versions = ["6.00", "6.01"]
patch_data_list = []
for version in patch_versions:
    try:
        patch_notes_url = "https://dota2.fandom.com/wiki/Version_{}".format(version)
        patch_notes = fetch_patch_notes(patch_notes_url, version)
        patch_data_list.append(patch_notes)
        print("Completed {}".format(version))
    except Exception as e:
        print(e.__str__, version)

if patch_notes:
    with open('patch_notes_new.json', 'a') as f:
        json.dump(patch_data_list, f, indent=4)