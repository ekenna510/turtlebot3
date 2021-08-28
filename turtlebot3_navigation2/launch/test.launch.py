import os
import launch

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    param_file_name = TURTLEBOT3_MODEL + '.yaml'
    # Declare the launc parameter
    DeclareLaunchArgument(
        'params',
         default_value = 'c:\home',
        description = 'Argument for child launch file'),



    run_rqt_arg = DeclareLaunchArgument(
        name="run_rqt",
        default_value="True",
        description="Launch RQT?")
    run_rviz_arg = DeclareLaunchArgument(
        name="run_rviz",
        default_value="False",
        description="Launch RVIZ?")
    
    #run_rqt_arg.default_value
    param_dir = LaunchConfiguration(
        'params',
        default=os.path.join(
            get_package_share_directory('turtlebot3_navigation2'),
            'param',
            param_file_name))
    print('param_file_name' ,param_file_name)
    #e = param_dir.variable_name
    # f=param_dir.perform(self)
    l=launch.substitutions.LaunchConfiguration('param')

    #b=e[0]
    #c=b.describe()
    print("zz")
    print("params " , l)
    b=run_rviz_arg.default_value[0].describe()
    print("run_rviz_arg.default_value",b)
    
    print(run_rqt_arg.name," default ", run_rqt_arg.default_value[0].describe())  
    print(" ")  
    print("globals", globals())
    print(" ")  
    print("locals",locals())
    print(" ")  
    print("dir", dir(LaunchDescription))
    print(" ")  
    print("dir", dir(launch))
    #c=run_rqt_arg.visit()
    #print(c)

    #d=run_rqt_arg.name
    #print(d)
#    d=param_dir.__format__
    #print(launch.substitution.LaunchConfiguration('params')   )   
    #print(h)


    return LaunchDescription([
])           
