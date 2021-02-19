def xmlelement_to_dict(xmlelement):
    newobj = {}
    for prop in list(xmlelement):
        key = prop.tag.lower()
        if key == 'navnelbnr':
            newobj[key] = int(prop.text)
        elif key in ['geo_lng', 'geo_lat']:
            if not prop.text:
                newobj[key] = prop.text
            else:
                newobj[key] = float(prop.text)
        else:
            # Fallback to string representation
            newobj[key] = prop.text
    return newobj


def sort_navnelbnr(lst):
    lst.sort(key=lambda x: x.get('navnelbnr'))
