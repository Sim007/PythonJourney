#
# read the data from the URL and print it
#
import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://beterbediend.rws.nl')
webUrl  = urllib.request.urlopen('https://geoserver.gelderland.nl/geoserver/ngr_c/wfs?request=GetFeature&service=WFS&version=1.1.0&typeName=InVv_Kwaliteitsnet_goederen_p&outputFormat=json')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)