def store_obj(store):
    return {
      "id":             store.external_id,
      "neighborhood":   store.neighborhood,
      "name":           store.name,
      "street_address": store.street_address,
      "city":           store.city,
      "state":          store.state,
      "zip":            store.zip,
      "phone":          store.phone,
      "links": [
        { "rel": "self", "href": "/stores/" + store.external_id },
        { "rel": "self", "href": "/stores/" + store.name },
        { "rel": "pets", "href": "/stores/%s/pets/" % store.external_id }
      ]
    }

def stores_obj(stores):
    stores_obj = []
    for store in stores.items:
        stores_obj.append(store_obj(store))
    return stores_obj
