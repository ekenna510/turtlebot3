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
    m=launch.LaunchDescription()


    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    m.add_entity(use_sim_time)

    param_file_name = TURTLEBOT3_MODEL + '.yaml'
    # Declare the launc parameter
    n=DeclareLaunchArgument(
        'params',
         default_value = 'c:\home',
        description = 'Argument for child launch file')
    m.add_entity(n)



    run_rqt_arg = DeclareLaunchArgument(
        name="run_rqt",
        default_value="True",
        description="Launch RQT?")
    m.add_entity(run_rqt_arg)

    run_rviz_arg = DeclareLaunchArgument(
        name="run_rviz",
        default_value="False",
        description="Launch RVIZ?")
    m.add_entity(run_rviz_arg)
    #run_rqt_arg.default_value
    param_dir = LaunchConfiguration(
        'params',
        default=os.path.join(
            get_package_share_directory('turtlebot3_navigation2'),
            'param',
            param_file_name))
    m.add_entity(param_dir)
    print('param_file_name' ,param_file_name)
    #e = param_dir.variable_name
    # f=param_dir.perform(self)
    l=launch.substitutions.LaunchConfiguration('params')
    m.add_entity(l)
    #b=e[0]
    #c=b.describe()
    print("zz")
    print("params " , l)
    b=run_rviz_arg.default_value[0].describe()
    print("run_rviz_arg.default_value",b)
    
    #print(run_rqt_arg.name," default ", run_rqt_arg.default_value[0].describe())  
    #print(" ")  
    #print("globals", globals())
    #print(" ")  
    #print("locals",locals())
    #print(" ")  
    #print("dir launchdescription ", dir(LaunchDescription))
    #print(" ")  
    #print("dir launch ", dir(launch))
    #c=run_rqt_arg.visit()
    #print(c)
    #print(" ")  
    print("dir m ",dir(m))
    print(" ")      
    o=m.get_launch_arguments(False)
    print("o ",o[0],o.count)
    print(" zzzzz")    
    #d=run_rqt_arg.name
    #print(d)
    #    d=param_dir.__format__
    #print(launch.substitution.LaunchConfiguration('params')   )   
    #print(h)

    return m
    #return LaunchDescription([
         
