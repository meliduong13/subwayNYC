class Stop:
    def __init__(self, name, latitude, longitude, location_type, parent_station):
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
        self._location_type = location_type
        self._parent_station = parent_station

    def get_name(self):
        return self._name

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitude

    def get_location_type(self):
        return self._location_type

    def get_parent_station(self):
        return self._parent_station

    def set_name(self):
        return self._name

    def set_latitude(self, latitude):
        self._latitude = latitude

    def set_longitude(self, longitude):
        self._longitude = longitude

    def set_location_type(self, location_type):
        self._location_type = location_type

    def set_parent_station(self, parent_station):
        self._parent_station = parent_station
