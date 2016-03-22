from datetime import datetime

import googlemaps

class DirectionsEngine(object):
    def __init__(self, **kwargs):
        required_kwargs = [
            'gmaps_key',
            'home_address',
            'work_address',
            'transport_mode'
        ]
        if not all(key in kwargs for key in required_kwargs):
            raise Exception('Not all options present')

        if kwargs['transport_mode'] != 'driving':
            raise Exception('Only driving is supported')

        for field in required_kwargs:
            setattr(self, field, kwargs[field])

    def run(self):
        self.gmaps = googlemaps.Client(key=self.gmaps_key)
        # Request directions
        now = datetime.now()
        directions_result = gmaps.directions(home, work,
            mode=self.transport_mode, departure_time=now)

        try:
            time_to_commute = directions_result[0]['duration_in_traffic']
        except:
            raise Exception('cannot get duration in traffic')

        return now, time_to_commute
