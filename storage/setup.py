#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: setup.py,v 0.2.3.4 2013-02-27 09:56:56 gaelL Exp $
#
# Copyright (C) 2010-2013  Gaël Lambert (gaelL) <gael.lambert@enovance.com>
#
# This file is part of numeter
#
# Numeter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
from distutils.command.install_data import install_data
import shutil

class my_install(install_data):
    def run(self):
        install_data.run(self)
        for script in self.get_outputs():
            # Rename name.init in name
            if script.endswith(".init"):
                shutil.move(script, script[:-5])
            if script.endswith(".default"):
                shutil.move(script, script[:-8])

if __name__ == '__main__':

    setup(name='redmon-storage',
          cmdclass={"install_data": my_install},
          version='0.2.3.10',
          description='Numeter Storage',
          long_description="""Numeter is a new graphing solution (like Cacti for \
          example) made by some guys working at eNovance. Poller and collector are \
          written in Python and datas are stored in a Redis DB. The webapp is written in PHP.\
          Documentation is available here: https://numeter.readthedocs.org""",
          author='Gaël Lambert (gaelL)',
          author_email='gael.lambert@enovance.com',
          maintainer='Gaël Lambert (gaelL)',
          maintainer_email='gael.lambert@enovance.com',
          keywords=['numeter','graphing','poller','collector', 'storage'],
          url='https://github.com/enovance/numeter',
          license='GNU Affero General Public License v3',
          scripts = ['storage/numeter-storage', 'storage/numeter-storaged'],
          packages = [''],
          package_dir = {'':'storage/module'},
          #package_data={'': ['storage/numeter_storage.py']},
          #data_files = [('/etc', ['etc/numeter.conf']),
          #              ('/etc/logrotate.d', ['etc/logrotate.d/numeter']),
          #              ('share/doc/numeter',['README', 'COPYING', 'CHANGES']),
          #              ('share/man/man1/', ['man/numeter.1']) ],
          data_files = [('/etc/numeter', ['storage/numeter_storage.cfg','storage/collector-list']), 
                        #              ('/etc/nginx/sites-available', ['storage/storage-web/numeter-storage-web']) ,
                        #              ('/etc/uwsgi/apps-available', ['storage/storage-web/numeter-storage-uwsgi.ini']) ,
                        ('/usr/share/numeter/storage', ['storage/storage-web/numeter_uwsgi.py']) ,
                        ('/var/log/numeter', '') ,
                        ('/etc/init.d', ['storage/numeter-storage.init']),
                        ('/etc/default', ['storage/numeter-storage.default']),
                        ('/var/lib/numeter/rrds', ''),
                        #('/etc/cron.d', ['storage/numeter-storage-cron'])
                        ],
          classifiers=[
              'Development Status :: 4 - Beta',
              'Environment :: Console',
              'Intended Audience :: Advanced End Users',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: GNU Affero General Public License v3',
              'Operating System :: POSIX',
              'Programming Language :: Python',
              'Topic :: System :: Monitoring'

          ],
         )
