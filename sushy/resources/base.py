# Copyright 2017 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc

import six
from six.moves import http_client

from sushy import exceptions


@six.add_metaclass(abc.ABCMeta)
class ResourceBase(object):

    def __init__(self, connector, path=''):
        self._conn = connector
        self._path = path
        self._json = None
        self.refresh()

    def refresh(self):
        resp = self._conn.get(path=self._path)
        if resp.status_code == http_client.NOT_FOUND:
            raise exceptions.ResourceNotFoundError(resource=self._path)

        self._json = resp.json()
        self._parse_attributes()

    @property
    def json(self):
        return self._json

    @property
    def path(self):
        return self._path

    @abc.abstractmethod
    def _parse_attributes(self):
        """Parse the attributes of a resource

        This method should be overwritten and is responsible for parsing
        all the attributes of a resource.
        """
