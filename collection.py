class Collection:
    def __new__(cls, *args):
        return super(Collection, cls).__new__(cls)

    def __init__(self, items={}):
        self.items = items

    def get_all(self):
        return self.items
        
    def get_all_descriptions(self):
        all_items = self.items.values()
        def get_des(item):
            return item.description
        descriptions = map(get_des,all_items)
        return list(descriptions)
    
    def get_item(self, key):
        return self.items.get(key)

    def add_item(self, item):
        self.items.update({item.key: item})
    
    def remove_item(self, key):
        return self.items.pop(key)