class ParkingLot:
  _instance=None

  def __init__(self):
    if ParkingLot._instance is not None:
      print('Parking Lot is a singleton')
    else:
      ParkingLot._instance=self
      # logic 
  @staticmethod
  def getinstance():
    if ParkingLot._instance is None:
      ParkingLot()
    return ParkingLot._instance  
