from SpecImports import *
LobbyParent = 10014
BoilerParent = 10030
PipeLeftParent = 10023
PipeRightParent = 10032
OilParent = 10034
ControlParent = 10037
DuctParent = 10036
CenterSiloBattleCellParent = 10064
CenterSiloParent = 20095
SigRoomParent = 20058
WestSiloParent = 20094
WestSiloBattleCellParent = 10047
EastSiloParent = 20096
EastSiloBattleCellParent = 10068
LobbyCell = 0
BoilerCell = 1
PipeLeftCell = 2
PipeRightCell = 3
OilCell = 4
ControlCell = 5
DuctCell = 6
CenterSiloCell = 7
SigRoomCell = 8
WestSiloCell = 9
EastSiloCell = 10
BattleCells = {LobbyCell: {'parentEntId': LobbyParent,
             'pos': Point3(0, 0, 0)},
 BoilerCell: {'parentEntId': BoilerParent,
              'pos': Point3(0, 0, 0)},
 OilCell: {'parentEntId': OilParent,
           'pos': Point3(0, 0, 0)},
 ControlCell: {'parentEntId': ControlParent,
               'pos': Point3(0, 0, 0)},
 CenterSiloCell: {'parentEntId': CenterSiloBattleCellParent,
                  'pos': Point3(0, 0, 0)},
 PipeLeftCell: {'parentEntId': PipeLeftParent,
                'pos': Point3(0, 0, 0)},
 PipeRightCell: {'parentEntId': PipeRightParent,
                 'pos': Point3(0, 0, 0)},
 DuctCell: {'parentEntId': DuctParent,
            'pos': Point3(0, 0, 0)},
 SigRoomCell: {'parentEntId': SigRoomParent,
               'pos': Point3(0, 0, 0)},
 WestSiloCell: {'parentEntId': WestSiloBattleCellParent,
                'pos': Point3(0, 0, 0)},
 EastSiloCell: {'parentEntId': EastSiloBattleCellParent,
                'pos': Point3(-20, -10, 0)}}
CogData = [{'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 6,
  'battleCell': LobbyCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 6,
  'battleCell': LobbyCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 6,
  'battleCell': LobbyCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'cc',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 6,
  'battleCell': LobbyCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'cc',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 7,
  'battleCell': BoilerCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'walk',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 6,
  'battleCell': BoilerCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'walk',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 7,
  'battleCell': BoilerCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'walk',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 6,
  'battleCell': BoilerCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 6,
  'battleCell': OilCell,
  'pos': Point3(-2, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 7,
  'battleCell': OilCell,
  'pos': Point3(2, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 6,
  'battleCell': OilCell,
  'pos': Point3(6, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 7,
  'battleCell': OilCell,
  'pos': Point3(-6, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 7,
  'battleCell': ControlCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 7,
  'battleCell': ControlCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 7,
  'battleCell': ControlCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 7,
  'battleCell': ControlCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'nd',
  'parentEntId': CenterSiloParent,
  'boss': 1,
  'level': 14,
  'battleCell': CenterSiloCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'gh',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 8,
  'battleCell': CenterSiloCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 7,
  'battleCell': CenterSiloCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm', # mingler or gladhander
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 8,
  'battleCell': CenterSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'nd',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 7,
  'battleCell': WestSiloCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'gh',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 6,
  'battleCell': WestSiloCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'gh',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 7,
  'battleCell': WestSiloCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'nd',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 6,
  'battleCell': WestSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'nd',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 7,
  'battleCell': EastSiloCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'gh',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 7,
  'battleCell': EastSiloCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'gh',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 7,
  'battleCell': EastSiloCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 7,
  'battleCell': EastSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeLeftCell,
  'pos': Point3(-6, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeLeftCell,
  'pos': Point3(2, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeLeftCell,
  'pos': Point3(-2, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeLeftCell,
  'pos': Point3(6, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeRightCell,
  'pos': Point3(-6, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeRightCell,
  'pos': Point3(2, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeRightCell,
  'pos': Point3(-2, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 7,
  'battleCell': PipeRightCell,
  'pos': Point3(6, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 6,
  'battleCell': DuctCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 6,
  'battleCell': DuctCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 6,
  'battleCell': DuctCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 6,
  'battleCell': DuctCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 7,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 8,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 7,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'nd',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 8,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = [{'type': 'cc',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 2,
  'battleCell': LobbyCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20009,
  'skeleton': 0,
  'joinParent': 20018},
 {'type': 'cc',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 2,
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20076,
  'skeleton': 0,
  'joinParent': 20019},
 {'type': 'tm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 2,
  'battleCell': BoilerCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20077,
  'skeleton': 0,
  'joinParent': 20019},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 3,
  'battleCell': OilCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60133,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 4,
  'battleCell': OilCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60135,
  'skeleton': 0},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 2,
  'battleCell': ControlCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20039,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 2,
  'battleCell': ControlCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20049,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 2,
  'battleCell': ControlCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20075,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 3,
  'battleCell': CenterSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20103,
  'skeleton': 0},
 {'type': 'gh',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 5,
  'battleCell': CenterSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 3,
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20104,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 3,
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20105,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 3,
  'battleCell': PipeLeftCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 4,
  'battleCell': PipeLeftCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 3,
  'battleCell': PipeRightCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 4,
  'battleCell': PipeRightCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 2,
  'battleCell': DuctCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20038,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 2,
  'battleCell': DuctCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20067,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 3,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 4,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
