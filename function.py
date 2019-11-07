import sys
import os
import volkswagencarnet
import jsonpickle

class VWCarnet(object):
    def __init__(self, args):
      vw = volkswagencarnet.Connection(args['username'], args['password'])
      if not vw._login():
        print('Failed to login with user %s, check your credentials.' % args['username'])
        sys.exit(1)

      # fetch vehicles
      vw.update()

      # we only support 1 vehicle at this time
      self.vehicle = list(vw.vehicles)[0]

def lambda_handler(event, context):
  print('lambda_handler() - event: %s', event)

  info = {
    'username': os.environ['USER'],
    'password': os.environ['PASS']
  }

  # create carnet instance and login
  carnet = VWCarnet(info)
  result = {}

  # available methods on the veichle
  availableMethods = [
    'start_charging',
    'start_climatisation',
    'start_window_heater',
    'stop_charging',
    'stop_climatisation',
    'stop_window_heater'
  ]
  
  try:
    action = event['queryStringParameters']['action']

    if action in availableMethods:
      print('action: %s', action)
      result = getattr(carnet.vehicle, action)()
      
  except Exception as e:
    print('ERROR', e)
    action = 'none'

  return {
    'statusCode': 200,
    'body': jsonpickle.encode({
      'taskStatus': result,
      'veichle': carnet.vehicle.data
    })
  }

# when running locally ...
if __name__ == '__main__':
    try:
      # right now, the lambda handler is configured
      # with a queryStringParameter command from AWS API Gateway.
      event = {
        'queryStringParameters': {
          'action': 'start_climatisation'
        }
      }

      res = lambda_handler(event, {})
      print(res)
    except KeyboardInterrupt:
      print('Aborting...')
      sys.exit(1)
