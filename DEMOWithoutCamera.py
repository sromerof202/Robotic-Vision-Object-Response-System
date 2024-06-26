from lib64 import jkrc
import math

# Connect to robot
robot = jkrc.RC("10.5.5.100")  
robot.login()
robot.power_on()
robot.enable_robot()
PI = 3.1415926

# Robot movement function
def move_robot():
    steps = [
         #1.
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #Pick start position
        {'move_type': 'linear', 'pos': [434.05619804325494, -642.5003246845436, -491.1178179039669, -3.0732691448715874, 0.09732520108331186, -1.620920328374446], 'execute_output': False, 'output_params': None},    
        {'move_type': 'linear', 'pos': [436.5486892783714, -637.3472356287502, -511.97667731497256, -3.089762192457776, 0.0469504380667461, -1.6043828586469289], 'execute_output': True, 'output_params': (1, 1, 1)},        
        {'move_type': 'linear', 'pos': [436.54643749144714, -637.3405960567902, -445.5781288441781, -3.089770272108181, 0.04696862990496213, -1.6043851147650572], 'execute_output': True, 'output_params': (1, 1, 0)},
        {'move_type': 'joint', 'pos':  [-0.15966795596019726, 0.1611305418733685, -1.9933365244454444, -3.231540989118124, -1.8697481893153989, 0.9646467937028447], 'execute_output': False, 'output_params': None}, #ready to place downside
        {'move_type': 'linear', 'pos': [394.1187650057215, -853.2460448602235, -386.0254762087825, -1.5290094956123501, -0.8021888997804472, -2.323927828122327], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos': [398.17476109589234, -857.3304501618516, -383.88860918971733, -1.5125059699481849, -0.8034579817345171, -2.336001032204984], 'execute_output': True, 'output_params': (1, 0, 1)},
        {'move_type': 'linear', 'pos': [375.85920217626017, -835.2402506321998, -389.13916949424726, -1.56709078217559, -0.7951005385570099, -2.2978646821634285], 'execute_output': True, 'output_params': (1, 0, 0)},
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #back to Pick start position

        
        #2.
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #Pick start position
        {'move_type': 'linear', 'pos': [383.26877704373726, -572.2577478865985, -486.97561511104357, 3.135700459872386, 0.035596859023384865, 1.5431296829259702], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos': [380.5984848828369, -579.5899701260172, -511.35380492121266, 3.108478533995385, -0.01402377043231914, 1.5205880526325153], 'execute_output': True, 'output_params': (1, 1, 1)},
        {'move_type': 'linear', 'pos': [380.6065573582272, -579.595713736943, -467.35171691448664, 3.1084603824188193, -0.014023317043613634, 1.520567711596768], 'execute_output': True, 'output_params': (1, 1, 0)},
        {'move_type': 'joint', 'pos':  [-0.15966795596019726, 0.1611305418733685, -1.9933365244454444, -3.231540989118124, -1.8697481893153989, 0.9646467937028447], 'execute_output': False, 'output_params': None}, #ready to place downside
        {'move_type': 'linear', 'pos': [386.9035021438682, -860.9102517970193, -295.43852870441526, 1.6049866603457834, 0.8133439662756955, 0.9446120240887813], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos': [391.005809688394, -865.1749075489394, -293.3983962491975, 1.586967467068555, 0.8172578977929856, 0.930691446338305], 'execute_output': True, 'output_params': (1, 0, 1)},
        {'move_type': 'linear', 'pos': [374.5677087196897, -849.9139467687135, -294.997218302507, 1.6065219293002004, 0.8031167318144916, 0.9387277552777502], 'execute_output': True, 'output_params': (1, 0, 0)},
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #back to Pick start position
        
        #3.
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #Pick start position
        {'move_type': 'linear', 'pos': [324.5435768183384, -529.952360492864, -494.9671563339725, -3.1257413884675778, 0.07063157580870509, -1.6077089828545728], 'execute_output': False, 'output_params': None},    
        {'move_type': 'linear', 'pos': [324.96972786797716, -527.527128987785, -511.46282597263803, -3.1304233559283654, 0.04357285238099681, -1.6215594708644823], 'execute_output': True, 'output_params': (1, 1, 1)},        
        {'move_type': 'linear', 'pos': [324.96838416145494, -527.5267542688918, -446.6611349863177, -3.1304383577608355, 0.043571241413274696, -1.6215791326617777], 'execute_output': True, 'output_params': (1, 1, 0)},
        {'move_type': 'joint', 'pos':  [-0.15966795596019726, 0.1611305418733685, -1.9933365244454444, -3.231540989118124, -1.8697481893153989, 0.9646467937028447], 'execute_output': False, 'output_params': None}, #ready to place downside
        {'move_type': 'linear', 'pos':  [394.2317328434325, -852.4399830500768, -221.24668986959787, -1.4739607486461819, -0.8020822588260071, -2.3408937850011786], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos':  [397.84773313281505, -856.3940788015514, -221.404206588099, -1.47993892583591, -0.804216704906533, -2.338477100955521], 'execute_output': True, 'output_params': (1, 0, 1)},
        {'move_type': 'linear', 'pos': [380.98753652642887, -841.0751118135838, -233.43774743008268, -1.576469962110015, -0.7975303982046471, -2.2753763559970315], 'execute_output': True, 'output_params': (1, 0, 0)},
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #back to Pick start position
    

        #4.
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #Pick start position
        {'move_type': 'linear', 'pos': [260.5465425315866, -470.7700792407256, -489.65313603357623, -3.0849457867957217, 0.03360996450436922, -1.592579318109448], 'execute_output': False, 'output_params': None},    
        {'move_type': 'linear', 'pos': [264.83669844339505, -470.0160873784381, -512.3270426082273, -3.1122150822652115, 0.017785021073428522, -1.619855963826343], 'execute_output': True, 'output_params': (1, 1, 1)},  
        {'move_type': 'linear', 'pos': [266.0692665733109, -474.71653646985914, -459.77075028670464, -3.1145961598292424, 0.057826736030841035, -1.6067628282637647], 'execute_output': True, 'output_params': (1, 1, 0)},
        {'move_type': 'joint', 'pos':  [3.0198547165327128, 1.1063502502051896, -2.182519568853192, -3.1029622340578515, -0.8536538016527417, 4.093560153875675], 'execute_output': False, 'output_params': None}, #ready to place upperside
        {'move_type': 'linear', 'pos': [403.7282827794441, -836.1339243556001, -128.01388417835744, -1.5957079026923557, -0.6957033599610677, -2.2656738124964106], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos': [408.04432982792355, -842.7895034794025, -130.87369229440205, -1.5832713228500095, -0.6965193913231613, -2.2806913552120323], 'execute_output': True, 'output_params': (1, 0, 1)},  
        {'move_type': 'linear', 'pos': [388.4429533815426, -829.8835709901568, -189.05872772251612, -2.0991171233613763, -0.6348214599048203, -1.9858478261679247], 'execute_output': True, 'output_params': (1, 0, 0)},
        {'move_type': 'joint', 'pos':  [0.04127162628898471, 0.08636081125085662, -2.098642012062073, -3.1324195521071614, -0.46536481790795686, 0.810385867765326], 'execute_output': False, 'output_params': None}, #back to Pick start position
       
        '''       
        
         '''
        
    ]
    
    for step in steps:
        if step['move_type'] == 'linear':
            robot.linear_move(step['pos'], 0, True, 100)
        elif step['move_type'] == 'joint':
            robot.joint_move(step['pos'], 0, True, 10)
        
        if step['execute_output']:
            robot.set_digital_output(*step['output_params'])  # Unpack and execute with dynamic parameters

move_robot()
robot.logout()