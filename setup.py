from setuptools import setup

package_name = 'panda_gripper_action_client'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Peter David Fagan',
    author_email='peterdavidfagan@gmail.com',
    maintainer='Peter David Fagan',
    maintainer_email='peterdavidfagan@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='An action client for interacting with Panda gripper.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
)
