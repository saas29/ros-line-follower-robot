
from setuptools import setup
import os
from glob import glob

package_name = 'simple_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        # launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),

        # robot arm model
        (os.path.join('share', package_name, 'models', 'arm_1dof'),
            glob('models/arm_1dof/*')),

        # track model files
        (os.path.join('share', package_name, 'models', 'track'),
            glob('models/track/*.sdf') + glob('models/track/*.config')),

        # track material scripts
        (os.path.join('share', package_name, 'models', 'track', 'materials', 'scripts'),
            glob('models/track/materials/scripts/*')),

        # track textures
        (os.path.join('share', package_name, 'models', 'track', 'materials', 'textures'),
            glob('models/track/materials/textures/*')),

        # worlds
        (os.path.join('share', package_name, 'worlds'),
            glob('worlds/*')),

        # rviz
        (os.path.join('share', package_name, 'rviz'),
            glob('rviz/*.rviz')),

        # config
        (os.path.join('share', package_name, 'config'),
            glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leo',
    maintainer_email='amanyamy@gmail.com',
    description='Simple robot description for Gazebo simulation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_commander = simple_robot_description.joint_commander:main',
        ],
    },
)


