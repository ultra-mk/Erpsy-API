from flask_pymongo import MongoClient
import random as rdm
from string import ascii_uppercase, digits

mongo = MongoClient('localhost', 27017)
db = mongo['erpsy']
collection = db['parts']


NOUNS = ('Resistor', 'Potentiometer', 'Capacitor',
         'Inductor', 'Oscillator', 'Relay', 'Transformer', 'Battery', 'Integrated Circuit',
         'Display', 'Condenser', 'Reactor', 'Isolator', 'Control Knob', 'PWB', 'Diode',
         'Thermistor', 'CMOS', 'Timer', 'Comparator', 'Regulator', 'Amplifier', 'Cerebra', 'Cerebro',
         'Extremis', 'Inducer', 'Centrifuge', 'Nanoparticulate')

ADJECTIVES = ('Active', 'Arc', 'DC', 'Fused', 'Passive',
              'Electromechanical', 'Constant Current', 'MOSFET', 'Incandescent',
              'Diode', 'MIS', 'Piezoelectrical', 'Choke', 'Solenoid', 'Selenium',
              'Distributed', 'Voltage Regulation', 'Light Emitting', 'Variable Capacitance',
              'Carbon Film', 'Metal Film', 'Variable', 'CDS', 'NTC', 'PTC', 'CTR', 'Electrolytic',
              'Tantalum', 'Ceramic', 'Multilayer', 'Polystyrene', 'Polypropylene', 'Mica', 'Repulsing',
              'Mandroid', 'Sonic', 'Orbital', 'Nano', 'Negator', 'Enervation', 'Intensifier', 'Adamantium',
              'Vibranium')

DESCRIPTIONS = ('FLIP-FLOP, 2 CIRCUITS', 'Logic IC Case Style',
                'PDIP', 'No. of Pins: 14', 'Case Style: PDIP', 'Single Transmitter/Receiver',
                'RS-422/RS-485', '8-Pin PDIP Tube', 'XOR Gate', '4-Element', '2-IN Bipolar',
                '14-Pin PDIP,XOR Gate', '4-Element 2-IN', 'Bipolar 14-Pin', 'PDIP XOR Gate',
                'IBUS', 'JIS', 'DC Block Type', 'Electrical Coil Sensor', 'Type 76553', 'Fiber Optic Circuit',
                'Constant Input Resistance', 'Constant Output resistance', 'TI', 'Stark Industries Model',
                'Reed Richards Design', 'Later Design Type', 'Reference 22320f', 'Von Doom Captive Design',
                'McCoy Style Conversion', 'Cho Model', 'Log Counter Implementatoon', 'MK VI', 'MKVII',
                'MacTaggert Implementation', 'Pym Particle Reduction', 'Bannertech', 'Technovore',
                'StarkVision', 'J-RICE', 'Starsky')


def number(style=None):
    if not style:
        return str(rdm.randint(10000000, 99999999))
    else:
        return _number_style(style)


def name():
    return '{0} {1}'.format(rdm.choice(ADJECTIVES), rdm.choice(NOUNS))


def description():
    return '{0} {1}'.format(rdm.choice(DESCRIPTIONS), rdm.choice(DESCRIPTIONS))


def _number_style(style):
    style = list(style)
    return ''.join([rdm.choice(digits) if i == '#' else rdm.choice(ascii_uppercase) if i == 'A' else i for i in style])


def seed_parts():
    for i in range(0, 1000):
        collection.insert_one({"part_number": number(), "part_name": name(),
                               "description": description()})
    mongo.close()
    return'{} parts have been seeded in the db.'.format(1000)
