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
            data = data.split(',')[0:10]
            SensorData(device_id=str(data[0]),
                       temp=float(data[1]),
                       humidity=float(data[2]),
                       dewpoint=float(data[3]),
                       pressure=float(data[4]),
                       light=float(data[5]),
                       wind_speed=float(data[6]),
                       wind_direction=float(data[7]),
                       rainfall=float(data[8]),
                       battery_level=float(data[9])).put()
            self.response.set_status(204)
        else:
            self.response.set_status(403)

class CSVHandler(webapp2.RequestHandler):
    def get(self):
       csv = [  sensorData.timestamp.strftime("%Y-%m-%d %H:%M:%S")+','+str(sensorData.temp)+','+str(sensorData.device_id) for sensorData in SensorData.query().order(-SensorData.timestamp).fetch(1000) if sensorData.temp > -1000.0 and sensorData.temp < 80.0 ]
       self.response.headers['Content-Type'] = 'text/csv'
       self.response.out.write( "date,temp,id\n"+"\n".join(csv) )

app = webapp2.WSGIApplication([('/log', LoggingHandler),
                               ('/data', CSVHandler)], debug=True)
