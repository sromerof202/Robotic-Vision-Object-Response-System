from lib64 import jkrc
import math

# Connect to robot
robot = jkrc.RC("192.168.0.77")  
robot.login()
robot.power_on()
robot.enable_robot()
PI = 3.1415926

# Robot movement function
def move_robot():
    steps = [
        {'move_type': 'linear', 'pos': [267.2914605678354, -740.2594871196947, -423.96106116660224, 3.1172763536266808, -0.0006966521259419739, -1.5514729313797895], 'execute_output': False, 'output_params': None}, #Pick start position
        {'move_type': 'linear', 'pos': [294.62876283165343, -771.8500603962474, -501.75422683035526, -3.098471133758355, -0.07106005324527828, -1.5804889962792563], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos': [294.9306333608298, -772.4663616602309, -511.8925847030589, -3.0954128148002895, -0.07399727662424732, -1.580997452113136], 'execute_output': True, 'output_params': (1, 1, 1)},
        {'move_type': 'linear', 'pos': [267.2914605678354, -740.2594871196947, -423.96106116660224, 3.1172763536266808, -0.0006966521259419739, -1.5514729313797895], 'execute_output': True, 'output_params': (1, 1, 0)},#Pick start position
        {'move_type': 'joint', 'pos':  [-0.038447509026332684, 0.4799707802861966, -2.1794636718658755, 0.0254236876150258, 1.77757874778098, -5.473506472294243], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos': [384.04431815931326, -860.4570379200748, -222.0045051412481, 1.4921925880341578, 0.795148173811235, 0.7056251089885117], 'execute_output': False, 'output_params': None},
        {'move_type': 'linear', 'pos': [388.2603400983529, -864.6270738459632, -220.6657097549594, 1.4854052238725803, 0.7940850086946193, 0.700854771583217],'execute_output': True, 'output_params': (1, 0, 1)},
        {'move_type': 'linear', 'pos': [356.7903896974555, -833.3346322654879, -225.78118563669108, 1.533428988237279, 0.8006262002128549, 0.7339489882423433],'execute_output': True, 'output_params': (1, 0, 0)},
        {'move_type': 'joint', 'pos':  [-0.01968015811256286, 0.29959623808033864, -1.8957131035314683, 1.9420128488625232, -0.0031812116276100644, -4.316753033153635], 'execute_output': False, 'output_params': None}, #Pick start position
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