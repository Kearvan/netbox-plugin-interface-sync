from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='netbox-interface-sync',
    version='0.3.0',
    description='Syncing interfaces with the interfaces from device type for NetBox devices (NetBox 4.5 compatible fork)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Victor Golovanenko',
    author_email='drygdryg2014@yandex.com',
    maintainer='Kearvan mcTorbins',
    maintainer_email='kearvan@mail.ru',
    license='GPL-3.0',
    install_requires=['attrs>=21.1.0'],
    packages=["netbox_interface_sync"],
    package_data={"netbox_interface_sync": ["templates/netbox_interface_sync/*.html"]},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: NetBox',
        'Framework :: NetBox :: 4.5',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
)
