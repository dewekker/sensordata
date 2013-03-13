import webapp2
from google.appengine.ext import ndb

class SensorData(ndb.Model):
    device_id = ndb.StringProperty()
    temp = ndb.FloatProperty()
    humidity = ndb.FloatProperty()
    dewpoint = ndb.FloatProperty()
    pressure = ndb.FloatProperty()
    light = ndb.FloatProperty()
    wind_speed = ndb.FloatProperty()
    wind_direction = ndb.FloatProperty()
    rainfall = ndb.FloatProperty()
    battery_level = ndb.FloatProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

#  @classmethod
#  def query_book(cls, ancestor_key):
#    return cls.query(ancestor=ancestor_key).order(-cls.date)

class LoggingHandler(webapp2.RequestHandler):
    def get(self):
        data = self.request.get('data',None)
        if data is not None:
            data = data.split(',')[1:10]
            id = self.request.get('id')
            SensorData(device_id=id,
                       temp=float(data[0]),
                       humidity=float(data[1]),
                       dewpoint=float(data[2]),
                       pressure=float(data[3]),
                       light=float(data[4]),
                       wind_speed=float(data[5]),
                       wind_direction=float(data[6]),
                       rainfall=float(data[7]),
                       battery_level=float(data[8])).put()
            self.response.set_status(204)
        else:
            self.response.set_status(403)

class CSVHandler(webapp2.RequestHandler):
    def get(self):
       csv = [  sensorData.timestamp.strftime("%Y-%m-%d %H:%M:%S")+','+str(sensorData.temp) for sensorData in SensorData.query().order(-SensorData.timestamp).fetch(1000) if sensorData.temp != -1000.0 and sensorData.temp < 80.0 ]
       self.response.headers['Content-Type'] = 'text/csv'
       self.response.out.write( "date,temp\n"+"\n".join(csv) )

app = webapp2.WSGIApplication([('/log', LoggingHandler),
                               ('/data', CSVHandler)], debug=True)
