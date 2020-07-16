from toontown.suit import SuitDNA
import types
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
from otp.otpbase import OTPGlobals
PartsPerSuit = (17,
 14,
 12,
 10)
PartsPerSuitBitmasks = (131071,
 130175,
 56447,
 56411)
AllBits = 131071
MinPartLoss = 2
MaxPartLoss = 4
MeritsPerLevel = ((100,
  130,
  160,
  190,
  380),
 (150,
  190,
  230,
  270,
  540),
 (250,
  300,
  350,
  400,
  800),
 (370,
  430,
  490,
  550,
  1100),
 (515,
  585,
  655,
  725,
  1450),
 (700,
  780,
  860,
  940,
  1880),
 (905,
  1005,
  1105,
  1205,
  2500),
 (1300,
  1700,
  2100,
  2500,
  2900,
  3300,
  3700,
  4100,
  4500,
  4900,
  5300,
  12500,
  0),
 (65,
  95,
  125,
  155,
  310),
 (100,
  140,
  180,
  220,
  450),
 (175,
  225,
  275,
  325,
  650),
 (300,
  360,
  420,
  480,
  960),
 (400,
  470,
  540,
  610,
  1220),
 (550,
  630,
  710,
  790,
  1580),
 (750,
  840,
  930,
  1020,
  2040),
 (950,
  1250,
  1550,
  1850,
  2150,
  2450,
  2750,
  3050,
  3350,
  3650,
  3950,
  8000,
  0),
 (40,
  60,
  80,
  100,
  200),
 (70,
  100,
  130,
  160,
  320),
 (140,
  180,
  220,
  260,
  520),
 (250,
  300,
  350,
  400,
  800),
 (380,
  440,
  500,
  560,
  1120),
 (530,
  600,
  670,
  740,
  1480),
 (700,
  780,
  860,
  940,
  2000),
 (900,
  1100,
  1300,
  1500,
  1700,
  1900,
  2100,
  2300,
  2500,
  2700,
  2900,
  6000,
  0),
 (20,
  40,
  60,
  80,
  160),
 (50,
  80,
  110,
  140,
  280),
 (90,
  130,
  170,
  210,
  420),
 (140,
  190,
  240,
  290,
  580),
 (200,
  260,
  320,
  380,
  760),
 (275,
  350,
  425,
  500,
  1000),
 (400,
  500,
  600,
  700,
  1500),
 (650,
  775,
  900,
  1025,
  1150,
  1300,
  1450,
  1600,
  1750,
  1900,
  2100,
  4500,
  0))
leftLegUpper = 1
leftLegLower = 2
leftLegFoot = 4
rightLegUpper = 8
rightLegLower = 16
rightLegFoot = 32
torsoLeftShoulder = 64
torsoRightShoulder = 128
torsoChest = 256
torsoHealthMeter = 512
torsoPelvis = 1024
leftArmUpper = 2048
leftArmLower = 4096
leftArmHand = 8192
rightArmUpper = 16384
rightArmLower = 32768
rightArmHand = 65536
upperTorso = torsoLeftShoulder
leftLegIndex = 0
rightLegIndex = 1
torsoIndex = 2
leftArmIndex = 3
rightArmIndex = 4
PartsQueryShifts = (leftLegUpper,
 rightLegUpper,
 torsoLeftShoulder,
 leftArmUpper,
 rightArmUpper)
PartsQueryMasks = (leftLegFoot + leftLegLower + leftLegUpper,
 rightLegFoot + rightLegLower + rightLegUpper,
 torsoPelvis + torsoHealthMeter + torsoChest + torsoRightShoulder + torsoLeftShoulder,
 leftArmHand + leftArmLower + leftArmUpper,
 rightArmHand + rightArmLower + rightArmUpper)
PartNameStrings = TTLocalizer.CogPartNames
SimplePartNameStrings = TTLocalizer.CogPartNamesSimple
PartsQueryNames = ({1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: PartNameStrings[6],
  128: PartNameStrings[7],
  256: PartNameStrings[8],
  512: PartNameStrings[9],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[16]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[16]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]})
suitTypes = PythonUtil.Enum(('NoSuit', 'NoMerits', 'FullSuit'))

def getNextPart(parts, partIndex, dept):
    dept = dept2deptIndex(dept)
    needMask = PartsPerSuitBitmasks[dept] & PartsQueryMasks[partIndex]
    haveMask = parts[dept] & PartsQueryMasks[partIndex]
    nextPart = ~needMask | haveMask
    nextPart = nextPart ^ nextPart + 1
    nextPart = nextPart + 1 >> 1
    return nextPart


def getPartName(partArray):
    index = 0
    for part in partArray:
        if part:
            return PartsQueryNames[index][part]
        index += 1


def isSuitComplete(parts, dept):
    dept = dept2deptIndex(dept)
    for p in xrange(len(PartsQueryMasks)):
        if getNextPart(parts, p, dept):
            return 0

    return 1

def getTotalMerits(toon, index):
    from toontown.battle import SuitBattleGlobals
    cogIndex = toon.cogTypes[index] + SuitDNA.suitsPerDept * index
    cogTypeStr = SuitDNA.suitHeadTypes[cogIndex]
    cogBaseLevel = SuitBattleGlobals.SuitAttributes[cogTypeStr]['level']
    cogLevel = toon.cogLevels[index] - cogBaseLevel
    cogLevel = max(min(cogLevel, len(MeritsPerLevel[cogIndex]) - 1), 0)
    return MeritsPerLevel[cogIndex][cogLevel]


def getTotalParts(bitString, shiftWidth = 32):
    sum = 0
    for shift in xrange(0, shiftWidth):
        sum = sum + (bitString >> shift & 1)

    return sum


def asBitstring(number):
    array = []
    shift = 0
    if number == 0:
        array.insert(0, '0')
    while pow(2, shift) <= number:
        if number >> shift & 1:
            array.insert(0, '1')
        else:
            array.insert(0, '0')
        shift += 1

    str = ''
    for i in xrange(0, len(array)):
        str = str + array[i]

    return str


def asNumber(bitstring):
    num = 0
    for i in xrange(0, len(bitstring)):
        if bitstring[i] == '1':
            num += pow(2, len(bitstring) - 1 - i)

    return num


def dept2deptIndex(dept):
    if type(dept) == types.StringType:
        dept = SuitDNA.suitDepts.index(dept)
    return dept
