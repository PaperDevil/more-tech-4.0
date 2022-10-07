def preprocess_post(
        post_id,
        group_id,
        location,
        post_type,
        text,
        image_link,
        explicit,
        tags):
    structure = {
        'post_id': post_id,
        'group_id': group_id,
        'country': location['country_id'] if 'country_id' in location else 0,
        'city': location['city_id'] if 'city_id' in location else 0,
        'post_type': post_type,
        'text': text,
        'image_link': image_link,
        'explicit': explicit,
        'tags': tags,
    }
    return structure